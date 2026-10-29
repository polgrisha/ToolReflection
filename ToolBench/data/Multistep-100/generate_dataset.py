from argparse import ArgumentParser
from collections import defaultdict
from tqdm import tqdm
import templates
import params
import pandas as pd
import os
import re
import random
import json


templates_func = {
	1: templates.template_1,
	2: templates.template_2,
	3: templates.template_3,
	4: templates.template_4,
	5: templates.template_5,
	6: templates.template_6,
	7: templates.template_7,
	8: templates.template_8,
	9: templates.template_9,
	10: templates.template_10,
}


param_generation = {
	1: params.get_param_values,
	2: params.get_param_values,
	3: params.get_param_values,
	4: params.get_param_values,
}


def extract_template_id(file_name):
	return int(re.search("\_.+\.", file_name).group(0)[1:-1])


def load_templates(input_dir):
	templates = defaultdict(list)
	files = os.listdir(input_dir)
	for file in files:
		template_id = extract_template_id(file)
		with open(os.path.join(input_dir, file)) as f:
			for line in f:
				templates[template_id].append({"template": line.strip()})
	return templates


def create_user_query(params, template):
	for param, value in params.items():
		template = re.sub(f"\[{param}\]", str(value), template)
	return template


def generate_chains(templates, dataset, param_values):
	res_chains = []
	for tid, template_list in templates.items():
		if tid == 6:
			chain = dataset.iloc[tid - 1]
			for template in tqdm(template_list):
				values = params.get_param_values(template["params"], param_values)
				res_chain = {}
				res_chain["user"] = create_user_query(values, template["template"])
				res_chain["assistant1_tool_name"] = chain["assistant1_tool_name"]
				res_chain["assistant1_params"] = values
				res_chain["assistant2_tool_name"] = chain["assistant2_tool_name"]
				assistant = templates_func[int(tid)](values)
				res_chain.update(assistant)
				res_chains.append(res_chain)
	return res_chains


if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("--dataset_file", default="toolbench_manually_created_dataset_new.tsv")
	parser.add_argument("--templates_dir", default="templates/")
	parser.add_argument("--param_values", default="param_values_new.tsv")
	parser.add_argument("--output_dataset", default="res_dataset/toolbench_multistep_dataset_template_6.json")
	args = parser.parse_args()

	dataset = pd.read_csv(args.dataset_file, sep="\t")
	print(dataset)
	param_values = params.load_params(args.param_values)
	templates = load_templates(args.templates_dir)
	templates = params.extract_params(templates)
	res_chains = generate_chains(templates, dataset, param_values)
	with open(args.output_dataset, "w") as out:
		for res_chain in res_chains:
			out.write(f"{json.dumps(res_chain)}\n")
