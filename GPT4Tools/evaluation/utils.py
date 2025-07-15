import json
from pathlib import Path
from .pint_api import PintAPI
from .flights_api import FlightScheduleService
from .geocoder_api import GeocoderAPI
from .nutrition_api import NutritionAnalysis
from .timeconversion_api import TimeConverterAPI

def load_thirty_tools():
    api_format_fpath = Path(__file__).parent / 'Thirty_tools/api_format_new_params_and_usage_example.json'
    api_format = json.load(open(api_format_fpath))

    def format_name(api_name:str) -> str:
        # NutritionAnalysis.analyze -> nutritionanalysis_analyze
        new_name = api_name.replace('.', '_').lower()
        return new_name

    def format_api_example(api_example:str) -> str:
        splitted = api_example.split('(', 1)
        return format_name(splitted[0]) + '(' + splitted[1]
    
    tools = []
    for item in api_format:
        print(item)
        tool = {
            'func': eval(item['api_name']),
            # 'func_name': item['api_name'],
            'func_name': format_name(item['api_name']),
            'description_retrieval': item['api_description']
        }
        # examples = "\n".join(format_api_example(example['api_call']) for example in item['api_examples'][:2])
#         p = """
# API Name: {func_name}
# API Parameter: {parameter_info}
# API Description: {description}
# API Call Examples: {examples}
#         """.format(
#                 func_name=tool['func_name'],
#                 parameter_info = item['api_parameter'],
#                 description=item['api_description'],
#                 examples=examples
#             )
        p = """
API Name: {func_name}
API Parameter: {parameter_info}
API Description: {description}
API Usage Example: {examples}
        """.format(
                func_name=tool['func_name'],
                parameter_info = item['api_parameter'],
                description=item['api_description'],
                examples=item['usage_example']
            )
        tool['description_prompt'] = p
        tools.append(tool)

    return tools