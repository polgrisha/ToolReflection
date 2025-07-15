import requests
import json
import re


def process_url(info, input_dict):
    url = info.get("url", "")
    print("Unformatted url: " + url)
    f_args = list(re.findall("\{\w*\}", url))
    for i in range(len(f_args)):
        f_args[i] = f_args[i].strip("\{\} \n")
    if len(f_args) > 0:
        try:
            url = url.format(**{key: input_dict[key] for key in f_args})
        except:
            print("Error: Cannot format url")
        try:
            for key in f_args:
                input_dict.pop(key)
        except:
            print("Error: lack of required parameter for f-string url")
    return url, input_dict
        

def args_to_dict(**kwargs):
    global dict_params
    dict_params = locals()["kwargs"]
    
# def str_to_dict_args(s):
#     keywords = ["False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class", 
#             "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", 
#             "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"]
#     code = f"args_to_dict({s})" 
#     matches = re.findall("|".join([f"{key} =" for key in keywords]), code)
#     if matches is not None:
#         new_old_keys = [(match[:-2]*2, match[:-2]) for match in matches]
#         for match in matches:
#             code = re.sub(match[:-2], match[:-2]*2, code)
#     exec(code)
#     global dict_params
#     for key in new_old_keys:
#         dict_params[key[1]] = dict_params[key[0]]
#         dict_params.pop(key[0])
    
#     print(f"Tool input dict: {dict_params}")
#     return dict_params

def str_to_dict_args(s):
    return json.loads(s)

def _finish(finish_input):
        try:
            dict_input = str_to_dict_args(finish_input)
        except:
            return "\nError: incorrect arguments.\n"
        if dict_input.get("return_type", "") == "give_answer":
            if dict_input.get("final_answer") is not None:
                #Here we can do anything with final answer
                response = f"\n\nThe final answer is:\n{dict_input.get('final_answer')}\n"
        elif dict_input.get("return_type", '') == "give_up_and_restart":
            response = "\n\nModel gave up.\n"
        else:
            response = "Error: Incorrect format of 'Finish' tool"
        return response


def get_response(tool_info, tool_input, url=None, host=None, 
                 key="e45ecc963bmsh840c44cfde0d03fp1e83d5jsn76cdc37a3b08", 
                 toolbench_key=None):
    if toolbench_key is None:
        try:
            headers = {
                "X-RapidAPI-Key": key,
                "X-RapidAPI-Host": host
            }
        except:
            response = "Error: Wrong tool arguments format"
            return response
        try:
            print(f"\nUrl: {url}\nHeaders: {headers}\nParams: {tool_input}")
            response = requests.get(url, headers=headers, params=tool_input)
            print("\nGot server response:")
            
            return response.text if len(response.text) < 768 else response.text[:768]
        except:
            response = "Error: Cannot get response from the server"  
    else:
        service_url = "http://8.218.239.54:8080/rapidapi"
        # method = tool_info["method"].lower() if tool_info.get("method") is not None else "get"
        # request = getattr(requests, method)
        try:
            payload = {
                "category": tool_info.get("category", tool_info.get("category_name")),
                "tool_name": tool_info["tool_name"],
                "api_name": tool_info["api_name"],
                "tool_input": tool_input,
                "strip": "truncate",
                "toolbench_key": toolbench_key
            }
            headers = {"toolbench_key": toolbench_key}
        except: 
            response = "Error: Wrong tool arguments format"
            return response
        try:
            response = requests.post(service_url, json=payload, 
                                            headers=headers, timeout=5)
            return response.text if len(response.text) < 512 else response.text[:512]
        except:
            response = "Error: Cannot get response from the server"
    return response
        


def call_tool(tool: str = None, tool_input: str = '', 
              tool_to_url_data_path="toolbenchv2_pangu_apis_urls.jsonl", **kwargs):
    
    with open(tool_to_url_data_path, "r", encoding="utf-8") as f:
        tool_to_url = json.load(f)
    if tool is None:
        api_response = "Error: wrong action format"
    elif tool.lower().strip() == "finish":
        api_response = _finish(tool_input)
    else:
        info = tool_to_url.get(tool, None)
        if info is not None:
            url = info.get("url", "")
            try:
                input_dict = str_to_dict_args(tool_input)
            except:
                req_params = info["required_parameters"]
                if len(req_params) == 1:
                    input_dict = {info["required_parameters"][0]: tool_input}
                else:
                    api_response = "Error: wrong arguments format."
                    return api_response
            try:
                url, input_dict = process_url(info, input_dict)
                #url = "http://8.218.239.54:8080/rapidapi"
            except:
                api_response = "Error: wrong arguments for f-string url"
                print(f"Tool output: {api_response}")
                return api_response
                
            api_response = get_response(tool_info=info, 
                                        tool_input=input_dict, 
                                        url=url, host=info.get("host"),
                                        **kwargs)
        else:
            api_response = "Error: Wrong call format or unavailable tool"
    print(f"Tool output: {api_response}")
    return api_response

