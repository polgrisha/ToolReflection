import transformers
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer, GenerationMixin
from transformers.generation.utils import GenerationMode
from peft import PeftModel
import torch
import sys

from utils.callbacks import Iteratorize, Stream, StopSequenceCriteria
from helpers.ssl import no_ssl_verification


if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

try:
    if torch.backends.mps.is_available():
        device = "mps"
except:  # noqa: E722
    pass

class LLM(GenerationMixin):
    @staticmethod
    def load_llm_tokenizer(
        base_model, lora_weights=None, load_8bit=None, 
        load_in_4bit=None, load_from_local=None
    ) -> tuple[transformers.LlamaTokenizer, transformers.LlamaForCausalLM]:
        with no_ssl_verification():
            tokenizer = LlamaTokenizer.from_pretrained(
                base_model,
                local_files_only=load_from_local,
            )
        if device == "cuda":
            with no_ssl_verification():
                print(f"{load_8bit=}")
                print(f"{load_in_4bit=}")
                model = LlamaForCausalLM.from_pretrained(
                    base_model,
                    load_in_8bit=load_8bit,
                    load_in_4bit=load_in_4bit,
                    torch_dtype=torch.float16,
                    device_map="auto",
                    local_files_only=load_from_local,
                )
            if lora_weights is not None:
                model = PeftModel.from_pretrained(
                    model,
                    lora_weights,
                    torch_dtype=torch.float16,
                )
                print(f"Loaded LORA")
        elif device == "mps":
            model = LlamaForCausalLM.from_pretrained(
                base_model,
                device_map={"": device},
                torch_dtype=torch.float16,
            )
            if lora_weights is not None:
                model = PeftModel.from_pretrained(
                    model,
                    lora_weights,
                    device_map={"": device},
                    torch_dtype=torch.float16,
                )
        else:
            model = LlamaForCausalLM.from_pretrained(
                base_model, device_map={"": device}, low_cpu_mem_usage=True
            )
            if lora_weights is not None:
                model = PeftModel.from_pretrained(
                    model,
                    lora_weights,
                    device_map={"": device},
                )
        # unwind broken decapoda-research config
        model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
        model.config.bos_token_id = 1
        model.config.eos_token_id = 2

        if not load_8bit and not load_in_4bit:
            model.half()  # seems to fix bugs for some users.

        model.eval()
        return tokenizer, model

    def __init__(
        self,
        base_model,
        lora_weights=None,
        load_8bit=None,
        load_in_4bit=None,
        load_from_local=None,
    ) -> None:
        tokenizer, model = self.load_llm_tokenizer(
            base_model=base_model, lora_weights=lora_weights, 
            load_8bit=load_8bit, load_in_4bit=load_in_4bit, 
            load_from_local=load_from_local
        )
        self.tokenizer = tokenizer
        self.model = model

    def generate(self, prompt: str, generate_params: dict = None, 
                 stop_sequences=None):
        input_ids = self.tokenizer(prompt, return_tensors="pt")[
            "input_ids"
        ].to(device)

        if stop_sequences is None:
            stop_sequences = [self.tokenizer.eos_token]
        if generate_params is None:
            generate_params = {
                "input_ids": input_ids,
                "num_beams": 5,
                "return_dict_in_generate": True,
                "output_scores": True,
                "max_new_tokens": 512
            }
        else:
            generate_params.update({"input_ids": input_ids})

        def generate_with_callback(callback=None, **kwargs):
            kwargs.setdefault(
                "stopping_criteria", transformers.StoppingCriteriaList()
            )
            kwargs["stopping_criteria"].append(Stream(callback_func=callback))
            kwargs["stopping_criteria"].append(
                StopSequenceCriteria(stop_sequences, self.tokenizer)
            )
            with torch.no_grad():
                self.model.generate(**kwargs)

        def generate_with_streaming(**kwargs):
            return Iteratorize(generate_with_callback, kwargs, callback=None)

        with generate_with_streaming(**generate_params) as generator:
            for output in generator:
                if output[-1] in [self.tokenizer.eos_token_id]:
                    break

                decoded_output = self.tokenizer.decode(
                    output, skip_special_tokens=True
                )
                prompt = self.tokenizer.decode(
                    self.tokenizer.encode(prompt), skip_special_tokens=True
                )
                response = decoded_output.removeprefix(prompt)
                yield response

                is_end_of_gen = False
                for s in stop_sequences:
                    if s in response:
                        is_end_of_gen = True
                        response = response[: response.index(s) + len(s)]
                if is_end_of_gen:
                    yield response
                    break

    @torch.inference_mode()
    def generate_eval_(self, prompt: str, generation_config: GenerationConfig):
        input_ids = self.tokenizer(prompt, return_tensors="pt")[
            "input_ids"
        ].to(device)
        output_ids = input_ids.tolist()[0]
        stop_token_ids = [self.tokenizer.eos_token_id]
        past_key_values = out = token = None
        generation_mode = self._get_generation_mode(generation_config, None)
        for i in range(generation_config.max_new_tokens):
            if i == 0:
                out = self.model(input_ids, use_cache=True)
            else:
                out = self.model(torch.as_tensor([[token]], device=device), use_cache=True, past_key_values=past_key_values)
            logits = out.logits
            past_key_values = out.past_key_values
            last_token_logits = logits[0, -1, :]


            if generation_mode == GenerationMode.GREEDY_SEARCH:  # greedy
                token = int(torch.argmax(last_token_logits))
            else:
                probs = torch.softmax(last_token_logits, dim=-1)
                token = int(torch.multinomial(probs, num_samples=1))

            output_ids.append(token)
            if token in stop_token_ids:
                break

            decoded_output = self.tokenizer.decode(
                    output_ids,
                    skip_special_tokens=True,
                    spaces_between_special_tokens=False,
                )
            response = decoded_output.removeprefix(prompt)
            yield response
        yield response