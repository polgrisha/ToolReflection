import json
import requests
import os

import sys
sys.path.append('../')
sys.path.append('../toolbench/inference')
import os
import json
import re
import time
import glob

tool_names = []
cate_names = []

tool_name_to_category_dict = dict()
for cat_path in glob.glob('data/toolbench_new_1311/toolenv/tools/*'):
    cat_name = cat_path.split('/')[-1]
    for tool_path in glob.glob(cat_path + '/*'):
        tool_name = tool_path.split('/')[-1]
        tool_name_to_category_dict[tool_name] = cat_name

def make_toolbench_request(action_name, action_input):
    service_url = "http://8.218.239.54:8080/rapidapi"
    toolbench_key = "2TLxGfLkzebcy7trDP4RzqcbnuAFypTHbKlRNvYCGuVsn5Svv3"

    try:
        api_name, tool_name = action_name.split('_for_', 1)
        category = tool_name_to_category_dict[tool_name]
    except:
        api_name, tool_name = "", ""
        category = ""

    payload = {
        "category": category,
        "tool_name": tool_name,
        "api_name": api_name,
        "tool_input": action_input,
        "strip": "truncate",
        "toolbench_key": toolbench_key
    }

    headers = {"toolbench_key": toolbench_key}

    try:
        response = requests.post(service_url, json=payload, headers=headers, timeout=15)
    except:
        return json.dumps({"error": "timeout error", "response": ""}), 12
    if response.status_code != 200:
        return json.dumps({"error": f"request invalid, data error. status_code={response.status_code}", "response": ""}), 12
    try:
        response = response.json()
    except:
        print(response)
        return json.dumps({"error": f"request invalid, data error", "response": ""}), 12
    
    if response["error"] == "API not working error...":
        status_code = 6
    elif response["error"] == "Unauthorized error...":
        status_code = 7
    elif response["error"] == "Unsubscribed error...":
        status_code = 8
    elif response["error"] == "Too many requests error...":
        status_code = 9
    elif response["error"] == "Rate limit per minute error...":
        print("Reach api calling limit per minute, sleeping...")
        time.sleep(10)
        status_code = 10
    elif response["error"] == "Message error...":
        status_code = 11
    else:
        status_code = 0
        return json.dumps(response), status_code
                    
    return json.dumps({"error": f"No such function name: {action_name}", "response": ""}), 1


def detect_error(content: str):
    error_message = re.findall('{"error": ?"([\s\S]*)", "response"', content)
    if len(error_message) == 0:
        error_message = re.findall('{error: ?"([\s\S]*)"', content)
    assert len(error_message) == 1
    error_message = error_message[0]

    if "response" in content and not re.search("\}\s?$", content):
        content = content + "}"
        if not re.search("[\"']\}$", content):
            content = content[:-1] + "\"" + "}"

    if "API not working" in error_message or \
        "Unauthorized" in error_message or \
        "Unsubscribed" in error_message or \
        "Request timeout" in error_message or \
        "Blocked" in error_message or \
        "unavailable" in error_message.lower() or \
        "request invalid, data error. status_code=5" in error_message or \
        "'status': 5" in content:
        return "Request error"
    
    if "No such function name:" in error_message:
        return "Wrong API error"
    
    if "Rate limit per minute" in error_message:
        return "Rate limit error"
    
    if "request invalid, data error" in error_message and "status_code=" not in error_message:
        return "Invalid format error"
    
    try:
        json_response = json.loads(content)

        if "Message error..." in error_message and json_response.get("response") is not None:
            return json_response.get("response")

        if (not json_response.get('response') or \
                 json_response.get("response") is None or \
                 json_response.get("response") == "[]") and \
                not json_response.get("error"):
            return "Empty output"
        
        if json_response["error"].strip():
            return json_response["error"]    
    except: pass

    return False