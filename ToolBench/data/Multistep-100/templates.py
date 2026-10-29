import tools
import json


def template_1(params):
	assistant = {}
	result = tools.metric_kilograms_for_body_mass_index_bmi_calculator(params["weight"], params["height"])
	assistant["function1"] = result.text
	result = json.loads(result.text)
	result["response"] = json.loads(result["response"].replace('\'', '\"'))
	assistant["assistant2_params"] = {"bmi": result["response"]["bmi"]}
	assistant["function2"] = tools.weight_category_for_body_mass_index_bmi_calculator(result["response"]["bmi"]).text
	return assistant


def template_2(params):
	assistant = {}
	result = tools.get_watches_by_brand_family_model_for_watch_database(**params)
	assistant["function1"] = result.text
	result = result.text.replace('\'', '\"')
	result = json.loads(result)
	print(result)
	watch_id = result[0]["id"]
	assistant["assistant2_params"] = {"id": watch_id}
	assistant["function2"] = tools.get_media_links_for_watch_database(watch_id).text
	return assistant
	

def template_3(params):
	print(params)
	assistant = {}
	result = tools.v1_celebrity_for_celebrity_by_api_ninjas(params["artist"])
	assistant["function1"] = result.text
	print(result.json())
	result = json.loads(result.text)
	result["response"] = result["response"].replace('\'', '\"')
	result["response"] = result["response"].replace("False", "\"False\"")
	result["response"] = result["response"].replace("True", "\"True\"")
	result["response"] = json.loads(result["response"])
	birthday = result["response"][0]['birthday'].split("-")
	params = {"month": birthday[1], "day": birthday[2]}
	assistant["assistant2_params"] = params
	assistant["function2"] = tools.get_date_fact_for_numbers(params["month"], params["day"]).text
	return assistant


def template_4(params):
	assistant = {}
	print(params)
	# distance_returned = False
	# i = 0
	# while not distance_returned and i < 10:
	# result = tools.get_distance_by_city_state_country_for_great_circle_math_api(city1=params["city&1"], 
	# 	state1=params["state&1"], city2=params["city&2"], state2=params["state&2"])
	result = tools.get_distance_by_city_state_country_for_great_circle_math_api(city1=params["city&1"], 
		state1=params["state&1"], city2=params["city&2"], state2=params["state&2"])
	assistant["function1"] = result.text
	result = json.loads(result.text)
	print(params)
	result["response"] = result["response"].replace('\'', '\"')
	result["response"] = json.loads(result["response"])
	distance = 	result["response"]["calculatedDist"]["distance"]
	input_unit = result["response"]["calculatedDist"]["uom"]
	if 'metric_length' in params:
		output_unit = params["metric_length"]
	else:
		output_unit = 'm'
	params = {"value": distance, "input_unit": input_unit, "output_unit": output_unit}
	assistant["assistant2_params"] = params
	assistant["function2"] = tools.convert_from_one_unit_of_measure_to_another_for_measurement_units_converter(**params).text
	return assistant


def template_5(params):
	assistant = {}
	result = tools.convert_from_one_unit_of_measure_to_another_for_measurement_units_converter(value=params["height_feet"], input_unit="ft", output_unit="in")
	assistant["assistant1_params"] = {"value": params["height_feet"], "input_unit": "ft", "output_unit": "in"}
	assistant["function1"] = result.text
	result = json.loads(result.text)
	result["response"] = result["response"].replace('\'', '\"')
	result["response"] = json.loads(result["response"])
	height = result["response"]['output']['value']
	assistant["assistant2_params"] = {'weight': params['weight'], 'height': height}
	assistant["function2"] = tools.imperial_pounds_for_body_mass_index_bmi_calculator(params['weight'], height).text
	return assistant


def template_6(params):
	assistant = {}
	print(params)
	result = tools.hsl_to_rgb_convexity(**params)
	assistant["function1"] = result.text
	result = json.loads(result.text)
	result["response"] = result["response"].replace('\'', '\"')
	result["response"] = json.loads(result["response"])
	red = result["response"]['red']
	assistant["assistant2_params"] = {'output_unit': 'm', 'input_unit': 'km', 'value': red}
	result = tools.convert_from_one_unit_of_measure_to_another_for_measurement_units_converter(**assistant["assistant2_params"])
	assistant["function2"] = result.text
	result = json.loads(result.text)
	result["response"] = result["response"].replace('\'', '\"')
	result["response"] = json.loads(result["response"])
	print(result)
	assistant["assistant3_params"] = {'number': result["response"]["output"]["value"]}
	assistant['function3'] = tools.get_math_fact_for_numbers(**assistant["assistant3_params"]).text
	return assistant


def template_7(params):
	assistant = {}
	print(params)
	result = tools.artist_for_deezer(params['artist'])
	print(result.text)
	assistant["function1"] = result.text
	# result = result.text.replace('\'', '\"')
	# result = json.loads(result)
	result = result.json()
	nb_album = result["nb_album"]
	assistant["assistant2_params"] = {"number": nb_album}
	assistant['function2'] = tools.get_math_fact_for_numbers(**assistant["assistant2_params"]).text
	return assistant


def template_8(params):
	assistant = {}
	result = tools.get_watches_by_brand_family_model_for_watch_database(**params)
	print(result.text)
	assistant["function1"] = result.text
	result = result.text.replace('\'', '\"')
	result = json.loads(result)
	movementReserve = result[0]["movementReserve"][:-2]
	params = {"value": movementReserve, "input_unit": "h", "output_unit": "s"}
	print(f"movementReserve ={movementReserve}")
	assistant["assistant2_params"] = json.dumps(params)
	assistant['function2'] = tools.convert_from_one_unit_of_measure_to_another_for_measurement_units_converter(**params).text
	return assistant


def template_9(params):
	assistant = {}
	result = tools.track_for_deezer(**params)
	assistant["function1"] = result.text
	# result = result.text.replace('\'', '\"')
	# result = json.loads(result)
	result = result.json()
	release_date = result["release_date"].split("-")
	params = {"month": release_date[1], "day": release_date[2]}
	assistant["assistant2_params"] = params
	assistant['function2'] = tools.get_date_fact_for_numbers(params["month"], params["day"]).text
	return assistant


def template_10(params):
	assistant = {}
	result = tools.album_for_deezer(**params)
	print(result.text)
	# print(result.text)
	assistant["function1"] = result.text
	# print(result.text)
	# result = result.text.replace('\'', '\"')
	# result = json.loads(result)
	result = result.json()
	print("genre_id" in result)
	# genre_id = result["genre_id"]
	# params = {"genre_id": genre_id}
	# assistant["assistant2_params"] = params
	# assistant['function2'] = tools.genre_for_deezer(**params).text
	return assistant
