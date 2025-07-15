import os
import sys
sys.path.insert(0, './')
sys.path.insert(0, './toolbench')
sys.path.insert(0, './toolbench/inference')
os.environ["CUDA_VISIBLE_DEVICES"]="0, 1"

import argparse
import json
from tqdm import tqdm
from toolbench.inference.Downstream_tasks.rapidapi import pipeline_runner
from toolbench.inference.Downstream_tasks.rapidapi import rapidapi_wrapper
from toolbench.inference.Downstream_tasks.rapidapi import get_white_list
from toolbench.inference.Algorithms.single_chain import single_chain
from toolbench.inference.LLM.tool_llama_lora_model import ToolLLaMALoRA
from toolbench.inference.LLM.tool_llama_model import ToolLLaMA
from toolbench_eval_utils import call_tool
from toolbench.model.model_adapter import get_conversation_template

parser = argparse.ArgumentParser()
parser.add_argument('--backbone_model', type=str, default="toolllama", required=False, help='chatgpt_function or davinci or toolllama')
parser.add_argument('--openai_key', type=str, default="", required=False, help='openai key for chatgpt_function or davinci model')
parser.add_argument('--model_path', type=str, default="your_model_path/", required=False, help='')
parser.add_argument('--tool_root_dir', type=str, default="your_tools_path/", required=True, help='')
parser.add_argument("--lora", action="store_true", help="Load lora model or not.")
parser.add_argument('--lora_path', type=str, default="your_lora_path if lora", required=False, help='')
parser.add_argument('--max_observation_length', type=int, default=1024, required=False, help='maximum observation length')
parser.add_argument('--observ_compress_method', type=str, default="truncate", choices=["truncate", "filter", "random"], required=False, help='observation compress method')
parser.add_argument('--method', type=str, default="CoT@1", required=False, help='method for answer generation: CoT@n,Reflexion@n,BFS,DFS,UCT_vote')
parser.add_argument('--input_query_file', type=str, default="", required=False, help='input path')
parser.add_argument('--output_answer_file', type=str, default="",required=False, help='output path')
parser.add_argument('--toolbench_key', type=str, default="",required=False, help='your toolbench key to request rapidapi service')
parser.add_argument('--rapidapi_key', type=str, default="",required=False, help='your rapidapi key to request rapidapi service')
parser.add_argument('--use_rapidapi_key', action="store_true", help="To use customized rapidapi service or not.")

model_path = 'data/model/ToolLLaMA-2-7b'
args = parser.parse_args(['--model_path', model_path, 
                          '--input_query_file', 'data/toolformer_data_convertion/eval/G1_eval_query.json',
                          '--output_answer_file', 'data/answer/test_toollama_2',
                          '--toolbench_key', '2TLxGfLkzebcy7trDP4RzqcbnuAFypTHbKlRNvYCGuVsn5Svv3',
                          '--tool_root_dir', 'data/toolenv/tools'])

with open('data/self_correction/train_data_cleaned_g1_callable.json', 'r') as f:
    all_callable_examples = json.load(f)

backbone_model = ToolLLaMA(model_name_or_path=args.model_path)

messages = []
for item in all_callable_examples[3]['conversations'][:2]:
    msg = {'role': item['from'], 'content': item['value']}
    messages.append(msg)

backbone_model.change_messages(messages)
res = backbone_model.parse(functions=None, process_id=0)

print(res)

def make_prediction(backbone_model, messages):
    conv = get_conversation_template(backbone_model.template)
    roles = {"system": conv.roles[0], "user": conv.roles[1], "function": conv.roles[2], "assistant": conv.roles[3]}
    prompt = ''
    for message in messages:
        role = roles[message['from']]
        content = message['value']
        prompt += f"{role}: {content}\n"
    prompt += "Assistant:\n"
    print(prompt)
    prediction = backbone_model.prediction(prompt)
    return prediction

res = make_prediction(backbone_model, all_callable_examples[3]['conversations'][:2])
print(res)

