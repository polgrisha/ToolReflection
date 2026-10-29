import sys
sys.path.append('../')
from utils import load_openapi_spec, analyze_openapi_spec
import json
from agent.convert_request import call_api_function
from utils import load_openapi_spec, escape
from agent.tools import Tool, GetDetailsTool, tool_projection

def load_tools(api_data):
    # server_url = "http://127.0.0.1:5679"
    server_url = None
    openapi_spec = load_openapi_spec(api_data["Documentation"], replace_refs=True)
    components_descriptions = escape(api_data["Function_Description"]["components"])
    tools = dict()
    for idx, func_name in enumerate(api_data["Function_Projection"]):
        description = escape(api_data["Function_Description"][func_name])
        if idx == len(api_data["Function_Projection"]) - 1:
            description += components_descriptions
        path, method = api_data["Function_Projection"][func_name]
        tools[func_name] = Tool(
            base_url=server_url + "/" + api_data["Name"] if server_url else None,
            func_name=func_name,
            openapi_spec=openapi_spec,
            path=path,
            method=method,
            description=description,
            retrieval_available="retrieval" in api_data.get("external_tools", [])
        )
    return tools

real_tools = json.load(open('data/eval_real.json', 'r'))
tools = load_tools(real_tools[0])
test_tool = tools['PublicHolidayIsTodayPublicHoliday']
print(test_tool._run('{\"countryCode\": \"cn\", \"offset\": 1}'))