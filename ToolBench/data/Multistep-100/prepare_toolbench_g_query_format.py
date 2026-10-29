from argparse import ArgumentParser
import json
import os


def load_json(file_name):
	with open(file_name) as f:
		return json.load(f)


def load_jsonl(file_name):
	data = []
	with open(file_name) as f:
		for line in f:
			data.append(json.loads(line))
	return data


def load_dataset(input_dir):
	data = []
	files = os.listdir(input_dir)
	for file in files:
		data.extend(load_jsonl(os.path.join(input_dir, file)))
	return data


def prepare_api(api):
	return {
        "category_name": api["category"],
        "tool_name": api["tool_name"],
        "api_name": api["api_name"],
        "api_description": api["description"],
        "required_parameters": api["required_parameters"],
        "optional_parameters": api["optional_parameters"],
        "method": api["method"]
    }


def prepare_dataset(dataset, api_to_url):
	res_dataset = []
	for data in dataset:
		print(data)
		api_list = []
		relevant_apis = []
		api = data["assistant1_tool_name"]
		print(api)
		api = prepare_api(api_to_url[api])
		api_list.append(api)
		relevant_apis.append([api["tool_name"], api["api_name"]])
		api = data["assistant2_tool_name"]
		print(api)
		api = prepare_api(api_to_url[api])
		api_list.append(api)
		relevant_apis.append([api["tool_name"], api["api_name"]])
		if "assistant3_tool_name" in data:
			api = data["assistant1_tool_name"]
			api = prepare_api(api_to_url[api])
			api_list.append(api)
			relevant_apis.append([api["tool_name"], api["api_name"]])
		res_dataset.append({
			'query': data['user'],
			'api_list': api_list,
			'relevant APIs': relevant_apis
			})
	return res_dataset


if __name__=="__main__":
	parser = ArgumentParser()
	parser.add_argument("--api_to_urls_file", default="data/self_correction/dataset_gen/toolbenchv2_pangu_apis_urls_new.jsonl")
	parser.add_argument("--input_dataset", default="data/self_correction/dataset_gen/challenging_tasks_ground_truth/")
	parser.add_argument("--output_dataset", default="data/self_correction/dataset_gen/challenging_tasks_input/input.json")
	args = parser.parse_args()

	api_to_url = load_json(args.api_to_urls_file)
	dataset = load_dataset(args.input_dataset)
	print(f"Loaded {len(dataset)} examples")

	res_dataset = prepare_dataset(dataset, api_to_url)
	with open(args.output_dataset, "w") as out:
		json.dump(res_dataset, out, indent=4)
