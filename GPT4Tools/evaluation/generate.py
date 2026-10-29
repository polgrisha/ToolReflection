import os
import json
import sys

import fire
import torch
import transformers
from LLM import LLM

from utils.prompter import PrompterGPT4Tools
from helpers.ssl import no_ssl_verification
from .utils import load_thirty_tools
from .coderunner import CodeRunner
from ToolLibrary.utils import extract_code

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


def prepare_tools() -> list[dict]:
    tool_library: list[dict] = load_thirty_tools()
    return tool_library


def prepare_tools_for_runner(tool_list: list) -> dict:
    tool_dict = {}
    for tool in tool_list:
        tool_dict[tool["func_name"]] = tool["func"]
    return tool_dict


def main(
    test_data_path: str,
    base_model: str = '',
    lora_weights: str = '',
    output_path: str = '',
    prompt_template_path: str = '',
    load_8bit: bool = True,
    load_4bit: bool = False,
    load_from_local: bool = True,
    max_new_tokens_default: int = 512,
):
    with open(test_data_path, "r") as fin:
        test_data = json.load(fin)
    with open(prompt_template_path, 'r') as f:
        template = f.read()
    
    llm = LLM(
        base_model=base_model,
        lora_weights=lora_weights,
        load_8bit=load_8bit,
        load_in_4bit=load_4bit,
        load_from_local=load_from_local,
    )
    generate_params = {
        "return_dict_in_generate": True,
        "output_scores": True,
        "max_new_tokens": max_new_tokens_default,
    }

    with no_ssl_verification():
        prompter = PrompterGPT4Tools(template)
        tools = prepare_tools_for_runner(prepare_tools())
        runner = CodeRunner()
        runner.add_tools(tools)
        prompts = []
        for item in test_data:
            prompt = prompter.generate_prompt(item)

            prompt += "Thought: Do I need to use a tool? Yes\n"
        
            steps = 0
            while True:
                stop_sequences = ['Output:', llm.tokenizer.eos_token]
                res = llm.generate(prompt, stop_sequences=stop_sequences)
                for response in res:
                    pass
                print(response)
                code = extract_code(response)
                execution_result = runner.run(code)
                # adding execution result to prompt
                execution_result = str(execution_result)
                encoded_execution_result = llm.tokenizer.encode(execution_result, add_special_tokens=False)
                max_exec_result_len = generate_params['max_new_tokens'] // 2
                if len(encoded_execution_result) >= max_exec_result_len:
                        encoded_execution_result = encoded_execution_result[:max_exec_result_len]
                execution_result = llm.tokenizer.decode(encoded_execution_result)
                prompt += response + ' ' + execution_result + '\n'
                if not 'EXEC ERROR' in execution_result or 'Thought: Do I need to use a tool? No' in execution_result:
                    break
                else:
                    steps += 1
                if steps == 3:
                    break
            stop_sequences = ['Output:', llm.tokenizer.eos_token]
            if 'Thought: Do I need to use a tool? Yes' in prompt:
                res = llm.generate(prompt, stop_sequences=stop_sequences)
                for response in res:
                    pass
                prompt += response
            prompts.append({'output': prompt})
            with open(output_path, 'w') as f:
                json.dump(prompts, f)

if __name__ == "__main__":
    fire.Fire(main)
