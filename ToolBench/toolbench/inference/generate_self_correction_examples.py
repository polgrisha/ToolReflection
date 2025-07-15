import os
import sys
import argparse
import json
from tqdm import tqdm
from toolbench.inference.Downstream_tasks.rapidapi import (
    get_white_list, 
    contain,
    rapidapi_wrapper
)
from toolbench.inference.LLM.tool_llama_lora_model import ToolLLaMALoRA
from toolbench.inference.LLM.tool_llama_model import ToolLLaMA
from toolbench_eval_utils import call_tool
from toolbench.model.model_adapter import get_conversation_template
from toolbench.utils import (
    standardize,
    change_name,
    replace_llama_with_condense
)
from toolbench.inference.utils import react_parser

def generate_prompt(conversations, idx, args):
    conv = get_conversation_template(args.template)
    roles = {"system": conv.roles[0], "user": conv.roles[1], "function": conv.roles[2], "assistant": conv.roles[3]}

    conversations
    for j, sentence in enumerate(conversations[:idx]):
        role = roles[sentence["from"]]
        conv.append_message(role, sentence["value"])
    prompt = conv.get_prompt()
    prompt = prompt[:-4] + '\nAssistant: '
    return prompt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', type=str, default='tool-llama-single-round', required=False, help='')
    parser.add_argument('--model_path', type=str, default="your_model_path/", required=True, help='')
    parser.add_argument('--ground_truth_examples_path', type=str, required=True, help='')
    parser.add_argument('--tool_descriptions_path', type=str, required=True, help='')
    parser.add_argument('--tool_root_dir', type=str, default="your_tools_path/", required=True, help='')
    parser.add_argument("--lora", action="store_true", help="Load lora model or not.")
    parser.add_argument('--lora_path', type=str, default="your_lora_path if lora", required=False, help='')
    parser.add_argument('--toolbench_key', type=str, default="",required=False, help='your toolbench key to request rapidapi service')
    parser.add_argument('--rapidapi_key', type=str, default="",required=False, help='your rapidapi key to request rapidapi service')
    parser.add_argument('--use_rapidapi_key', action="store_true", help="To use customized rapidapi service or not.")
    parser.add_argument('--max_observation_length', type=int, default=1024, required=False, help='maximum observation length')
    parser.add_argument('--observ_compress_method', type=str, default="truncate", choices=["truncate", "filter", "random"], required=False, help='observation compress method')
    args = parser.parse_args()

    replace_llama_with_condense(ratio=4)
    if args.lora:
        backbone_model = ToolLLaMALoRA(base_name_or_path=args.model_path, model_name_or_path=args.lora_path)
    else:
        backbone_model = ToolLLaMA(model_name_or_path=args.model_path)

    with open(args.ground_truth_examples_path, 'r') as f:
        ground_truth_examples = json.load(f)
    with open(args.tool_descriptions_path, 'r') as f:
        tool_descriptions = json.load(f)

    white_list = get_white_list(args.tool_root_dir)
    
    error_list = []
    for item in tqdm(ground_truth_examples):
        query = item['conversations'][1]['value'].split('\n')[1]
        data_dict = tool_descriptions[query]
        origin_tool_names = [standardize(cont["tool_name"]) for cont in data_dict["api_list"]]
        tool_des = contain(origin_tool_names, white_list)
        tool_des = [[cont["standard_tool_name"], cont["description"]] for cont in tool_des]
        wrapper = rapidapi_wrapper(data_dict, tool_des, None, args, process_id=0)

        conversations = item['conversations']
        for i, step in enumerate(item['conversations']):
            if step['from'] == 'assistant':
                prompt = generate_prompt(conversations, i, args)
                prediction = backbone_model.prediction(prompt)
                thought, action, action_input = react_parser(prediction)
                response = wrapper._step(action_name=action, action_input=action_input)
                response_message = json.loads(response[0])
                if action != 'Finish':
                    if response_message['error']:
                        error_list.append([prediction, query, i, response])
                        with open('data/self_correction/errors_g1.json', 'w') as f:
                            json.dump(error_list, f, ensure_ascii=False)





if __name__ == "__main__":
    main()