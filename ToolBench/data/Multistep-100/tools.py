import requests
import config
import utils
import json

toolbench_service_url = "http://8.218.239.54:8080/rapidapi"


def get_math_fact_for_numbers(number):
    payload = {
        "category": 'Education', 
        "tool_name": 'numbers', 
        "api_name": 'get_math_fact',
        "tool_input": json.dumps({"number": number}), 
        "strip": 'truncate', 
        "toolbench_key": config.TOOLBENCH_KEY}

    return utils.oolbench_request(payload)


def artist_for_deezer(artist):
    url = f"https://deezerdevs-deezer.p.rapidapi.com/artist/{artist}"
    host = "deezerdevs-deezer.p.rapidapi.com"
    return utils.rapidapi_request(url, host)


def metric_kilograms_for_body_mass_index_bmi_calculator(weight, height):
    payload = {
        "category": 'Health_and_Fitness',
        "tool_name": 'body_mass_index_bmi_calculator',
        "api_name": 'metric_kilograms',
        "tool_input": json.dumps({"weight": weight, "height": height}),
        "strip": 'truncate',
        "toolbench_key": config.TOOLBENCH_KEY}
    return utils.toolbench_request(payload)


def weight_category_for_body_mass_index_bmi_calculator(bmi):
    payload = {
        "category": 'Health_and_Fitness', 
        "tool_name": 'body_mass_index_bmi_calculator', 
        "api_name": 'weight_category', 
        "tool_input": json.dumps({"bmi": bmi}), 
        "strip": 'truncate', 
        "toolbench_key": config.TOOLBENCH_KEY}

    return utils.toolbench_request(payload)


def get_watches_by_brand_family_model_for_watch_database(watch_brandName, watch_family, watch_model):
    url = f"https://watch-database1.p.rapidapi.com/all-watches-by/brandname/{watch_brandName}/family/{watch_family}/model/{watch_model}"
    host = "watch-database1.p.rapidapi.com"
    return utils.rapidapi_request(url, host)

# def get_watches_by_brand_family_model_for_watch_database(watch_brandName, watch_family, watch_model):
#     payload = {
#         "category": 'Database', 
#         "tool_name": 'watch_database', 
#         "api_name": 'get_watches_by_brand_family_model', 
#         "tool_input": json.dumps("watch_brandName": watch_brandName,
#                                  "watch_family": watch_family,
#                                  "watch_model"), 
#         "strip": 'truncate', 
#         "toolbench_key": config.TOOLBENCH_KEY}

#     return utils.toolbench_request(payload)

def get_media_links_for_watch_database(watch_id):
    url = "https://watch-database1.p.rapidapi.com/watch-media-links-by-id/224833"
    host = "watch-database1.p.rapidapi.com"
    return utils.rapidapi_request(url, host)


def v1_celebrity_for_celebrity_by_api_ninjas(artist_name):
    payload = {
            "category": 'Entertainment', 
            "tool_name": 'Celebrity by API-Ninjas', 
            "api_name": '/v1/celebrity', 
            "tool_input": json.dumps({"name": artist_name}), 
            "strip": 'truncate', 
            "toolbench_key": config.TOOLBENCH_KEY}
    return utils.toolbench_request(payload)


def get_date_fact_for_numbers(month, day):
    payload = {
            "category": 'Education', 
            "tool_name": 'Numbers', 
            "api_name": 'Get date fact', 
            "tool_input": json.dumps({"month": month, "day": day}), 
            "strip": 'truncate', 
            "toolbench_key": config.TOOLBENCH_KEY}
    return utils.toolbench_request(payload)


def get_distance_by_city_state_country_for_great_circle_math_api(city1, state1, city2, state2):
    payload = {
            "category": 'Travel', 
            "tool_name": 'Great Circle Math Api', 
            "api_name": 'get_distance_by_city_state_country',
            "tool_input": json.dumps({"city1": city1, "state1": state1, \
                "city2": city2, "state2": state2, \
                "country1": "us", "country2": "us"}), 
            "strip": 'truncate', 
            "toolbench_key": '2TLxGfLkzebcy7trDP4RzqcbnuAFypTHbKlRNvYCGuVsn5Svv3'}
    return utils.toolbench_request(payload)  


def convert_from_one_unit_of_measure_to_another_for_measurement_units_converter(value, input_unit, output_unit):
    payload = {
            "category": 'Tools', 
            "tool_name": 'Measurement Units Converter', 
            "api_name": 'Convert from one unit of measure to another', 
            "tool_input": json.dumps({"value": value, "input_unit": input_unit, "output_unit": output_unit}), 
            "strip": 'truncate', 
            "toolbench_key": '2TLxGfLkzebcy7trDP4RzqcbnuAFypTHbKlRNvYCGuVsn5Svv3'}
    return utils.toolbench_request(payload)


def imperial_pounds_for_body_mass_index_bmi_calculator(weight, height):
    payload = {
        "category": 'Health_and_Fitness',
        "tool_name": 'body_mass_index_bmi_calculator',
        "api_name": 'imperial_pounds',
        "tool_input": json.dumps({"weight": weight, "height": height}),
        "strip": 'truncate',
        "toolbench_key": config.TOOLBENCH_KEY}
    return utils.toolbench_request(payload)


def hsl_to_rgb_convexity(h, s, l):
    payload = {
        "category": 'Tools',
        "tool_name": 'Convexity',
        "api_name": 'hsl_to_rgb',
        "tool_input": json.dumps({"h": h, "s": s, "l": l}),
        "strip": 'truncate',
        "toolbench_key": config.TOOLBENCH_KEY}
    return utils.toolbench_request(payload)


def get_math_fact_for_numbers(number):
    payload = {
            "category": 'Education', 
            "tool_name": 'numbers', 
            "api_name": 'get_math_fact',
            "tool_input": json.dumps({"number": number}), 
            "strip": 'truncate', 
            "toolbench_key": '2TLxGfLkzebcy7trDP4RzqcbnuAFypTHbKlRNvYCGuVsn5Svv3'}
    return utils.toolbench_request(payload)


def track_for_deezer(track_id):
    url = f"https://deezerdevs-deezer.p.rapidapi.com/track/{track_id}"
    host = "deezerdevs-deezer.p.rapidapi.com"
    return utils.rapidapi_request(url, host)


def album_for_deezer(album_id):
    url = f"https://deezerdevs-deezer.p.rapidapi.com/album/{album_id}"
    host = "deezerdevs-deezer.p.rapidapi.com"
    return utils.rapidapi_request(url, host)


def genre_for_deezer(genre_id):
    url = f"https://deezerdevs-deezer.p.rapidapi.com/track/{genre_id}"
    host = "deezerdevs-deezer.p.rapidapi.com"
    return utils.rapidapi_request(url, host)


# def v1_celebrity_for_celebrity_by_api_ninjas(artist):
#     payload = {
#         "category": 'Entertainment', 
#         "tool_name": 'Celebrity by API-Ninjas', 
#         "api_name": '/v1/celebrity', 
#         "tool_input": json.dumps({"name": artist}), 
#         "strip": 'truncate', 
#         "toolbench_key": config.TOOLBENCH_KEY}
#     return utils.toolbench_request(payload, host)
