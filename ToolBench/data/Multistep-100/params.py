import random
import pandas as pd
import re
from collections import defaultdict
random.seed(11)

linked_params = ["city&1", "state&1", "watch_brandName", "watch_family", "watch_model", "city&2", "state&2"]


def load_params(param_values_file):
	param_values = pd.read_csv(param_values_file, sep="\t")
	param_values_dict = {}
	for param_name in param_values.columns:
		param_values_dict[param_name] = list([p for p in list(param_values[param_name]) if str(p) != 'nan'])
	return param_values_dict


def extract_template_params(template):
	return re.findall("\[.*?\]", template)


def extract_params(templates):
	res_templates = defaultdict(list)
	for tid, template in templates.items():
		for t in template:
			params = extract_template_params(t["template"])
			params = [p[1:-1] for p in params]
			res_templates[tid].append({"template": t["template"], "params": params})
	return res_templates


def get_param_values(params, param_values):
	params_single = []
	params_linked = []
	for param in params:
		if param in linked_params:
			params_linked.append(param)
		else:
			params_single.append(param)
	res_params = get_param_values_single(params_single, param_values)
	linked_param_groups = divide_params_into_groups(params_linked)
	for group in linked_param_groups:
		res_params.update(get_param_values_linked(group, param_values))
	return res_params


def unify_param_name(param):
	return param.split("&")[0]


def get_param_values_single(params, param_values):
	res_params = {}
	for param in params:
		value = random.choice([p for p in list(param_values[unify_param_name(param)]) if str(p) != 'nan'])
		res_params[param] = value
	return res_params


def get_param_values_linked(params, param_values):
	res_params = {}
	min_length = find_min_value(param_values, params)
	index = random.randint(0, min_length-1)
	for param in params:
		res_params[param] = param_values[unify_param_name(param)][index]
	return res_params


def find_min_value(param_values, params):
	min_length = 1000
	for param in params:
		param = unify_param_name(param)
		if len(param_values[param]) < min_length:
			min_length = len(param_values[param])
	return min_length

def divide_params_into_groups(params):
	groups = [[]]
	for param in params:
		if len(param.split('&')) == 1:
			groups[0].append(param)
		else:
			idx = int(param.split('&')[1])
			if len(groups) < idx + 1:
				groups.append([])
			groups[idx].append(param)
	return groups