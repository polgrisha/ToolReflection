import json
import re

import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="5"
import sys
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaForCausalLM, LlamaTokenizer
import json
import torch
import re
from tqdm import tqdm
from collections import Counter

PROMPT = '''
You are you will be given api calls from some model and api outputs from rapidapi apis. 
Sometimes api return errors. 
It is hard to parse them using rule-based methods. 
An api may respond with an empty output (it could be empty list, or an empty dict), contain a field that states it is an error or etc.
You will be given 5 examples. You should respond only "Yes" if the response does not contain errors from an api and "No" if not.
Please make shure that api returned what the api call requested. If not, return "No"
Examples:
API Call:
Thought: To fulfill the user's request for gathering user information and recent media posts from Instagram for a specific username 'nike', I previously called the 'userinfo_for_instagram_cheapest' function with the argument {"username": "nike"}. By doing so, I efficiently retrieved the desired user data, including their biography, bio links, biographical information, and other relevant details. Now, to proceed with accessing the user's recent media posts, I will call the 'user_medias_for_instagram_cheapest' function with the argument {"user_id": "113294420064920"}. This will allow me to retrieve the most recent media posts of the user 'nike' and provide the user with the requested data effectively.
Action: user_medias_for_instagram_cheapest
Action Input: {
  "user_id": "113294420064920"
}
API Response:
{"error": "", "response": "{'items': [], 'num_results': 0, 'status': 'ok'}"}
Result:
No
###
API Call:
Thought: The user requested the list of languages supported by the LanguageTool API for grammar and writing assistance. To fulfill this request, I need to call the "list_of_languages_for_languagetool" function without any arguments. By doing so, I expect to receive the complete list of supported languages. This information will be crucial for implementing multilingual support in the project, ensuring accurate grammar and writing assistance for different languages.
Action: list_of_languages_for_languagetool
Action Input: {}
API Response:
{"error": "", "response": "[{'name': 'Arabic', 'code': 'ar', 'longCode': 'ar'}, {'name': 'Asturian', 'code': 'ast', 'longCode': 'ast-ES'}, {'name': 'Belarusian', 'code': 'be', 'longCode': 'be-BY'}, {'name': 'Breton', 'code': 'br', 'longCode': 'br-FR'}, {'name': 'Catalan', 'code': 'ca', 'longCode': 'ca-ES'}, {'name': 'Catalan (Valencian)', 'code': 'ca', 'longCode': 'ca-ES-valencia'}, {'name': 'Catalan (Balearic)', 'code': 'ca', 'longCode': 'ca-ES-balear'}, {'name': 'Danish', 'code': 'da', 'longCode': 'da-DK'}, {'name': 'German', 'code': 'de', 'longCode': 'de'}, {'name': 'German (Germany)', 'code': 'de', 'longCode': 'de-DE'}, {'name': 'German (Austria)', 'code': 'de', 'longCode': 'de-AT'}, {'name': 'German (Swiss)', 'code': 'de', 'longCode': 'de-CH'}, {'name': 'Simple German', 'code': 'de-DE-x-simple-language', 'longCode': 'de-DE-x-simple-language'}, {'name': 'Greek', 'code': 'el', 'longCode': 'el-GR'}, {'name': 'English', 'code': 'en', 'longCode': 'en'}, {'name': 'English (US)', 'code': 'en', 'longCode': 'en-U..
Result:
Yes
###
API Call:
Thought: I will now call the "dividends_for_freedom_finance" function to retrieve information about dividends for the symbol "AMZN". By using the argument {"symbol": "AMZN"}, I can focus specifically on the dividends related to the stock "AMZN". This function will help me analyze the dividend history for "AMZN" and provide the user with the requested information.
Action: dividends_for_freedom_finance
Action Input: {
"symbol": "AMZN"
}
API Response:
{"error": "", "response": "{'total': 0, 'offset': 0, 'results': [], 'responseStatus': None}"}
Result:
No
###
API Call:
Thought: To gather the required information for integrating APIs into the company's website, I can call the "list_all_api_for_testing_for_my_use" function. This function will provide me with descriptions, methods, required parameters, and optional parameters for each API. With this information, I can analyze and compare the APIs to make an informed decision.
Action: list_all_api_for_testing_for_my_use
Action Input: {}
API Response:
{"error": "Unauthorized error...", "response": "{'1forge.com': {'added': '2017-05-30T08:34:14.000Z', 'preferred': '0.0.1', 'versions': {'0.0.1': {'added': '2017-05-30T08:34:14.000Z', 'info': {'contact': {'email': 'contact@1forge.com', 'name': '1Forge', 'url': 'http://1forge.com'}, 'description': 'Stock and Forex Data and Realtime Quotes', 'title': '1Forge Finance APIs', 'version': '0.0.1', 'x-apisguru-categories': ['financial'], 'x-logo': {'backgroundColor': '#24292e', 'url': 'https://api.apis.guru/v2/cache/logo/https_1forge.com_assets_images_f-blue.svg'}, 'x-origin': [{'format': 'swagger', 'url': 'http://1forge.com/openapi.json', 'version': '2.0'}], 'x-providerName': '1forge.com'}, 'updated': '2017-06-27T16:49:57.000Z', 'swaggerUrl': 'https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.json', 'swaggerYamlUrl': 'https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.yaml', 'openapiVer': '2.0', 'link': 'https://api.apis.guru/v2/specs/1forge.com/0.0.1.json'}}}, '1password.com:events': {'added': '2021-07-19...
Result:
No
###
API Call:
Thought: I need to gather user information for a specific Instagram username, 'nike', as requested by the user. They also want access to the user's recent media posts. To achieve this, I will call the 'userinfo_for_instagram_cheapest' function with the argument of {"username": "nike"}. This will help me retrieve the desired data efficiently and fulfill the user's request effectively.
Action: userinfo_for_instagram_cheapest
Action Input: {
  "username": "nike"
}
API Response:
{"error": "", "response": "{'data': {'user': {'biography': 'Spotlighting athlete* and\\xa0\ud83d\udc5f\\xa0stories\\n#BlackLivesMatter, #StopAsianHate, and #NoPrideNoSport', 'bio_links': [{'title': '', 'lynx_url': 'https://l.instagram.com/?u=https%3A%2F%2Flinkin.bio%2Fnike&e=AT063fG4N158ZbZOaZ_A32batiXwR-0Yih5XNa5wfSNPCiDo546PSV0a8mm72ElVxWgNJdgYeHNOTMMTOe_kn7R-C-f2N9ym', 'url': 'https://linkin.bio/nike', 'link_type': 'external'}], 'biography_with_entities': {'raw_text': 'Spotlighting athlete* and\\xa0\ud83d\udc5f\\xa0stories\\n#BlackLivesMatter, #StopAsianHate, and #NoPrideNoSport', 'entities': [{'user': None, 'hashtag': {'name': 'nopridenosport'}}, {'user': None, 'hashtag': {'name': 'stopasianhate'}}, {'user': None, 'hashtag': {'name': 'blacklivesmatter'}}]}, 'blocked_by_viewer': False, 'restricted_by_viewer': None, 'country_block': False, 'eimu_id': '113294420064920', 'external_url': 'https://linkin.bio/nike', 'external_url_linkshimmed': 'https://l.instagram.com/?u=https%3A%2F%2Flinkin.bio%2Fnike&e=AT04S69...
Result:
Yes
###
API Call: 
<api_call>
API Response:
<api_response>
Result:
'''
BASE_MODEL_NAME = 'data/Llama-2-7b-chat-hf'

class ErrorDetector:
    def __init__(self):
        self.model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL_NAME,
            load_in_4bit=True,
            local_files_only=True,
            device_map='auto',
        )
        self.model.config.use_cache = False
        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME, local_files_only=True)
        self.prompt = PROMPT
    
    def predict(self, api_call, api_response):
        curr_prompt = self.prompt.replace('<api_call>', str(api_call))
        curr_prompt = curr_prompt.replace('<api_response>', str(api_response))
        with torch.no_grad():
            tokenized = self.tokenizer(curr_prompt, return_tensors="pt").input_ids
            res = self.model.generate(tokenized, max_length=tokenized.shape[1] + 1)
            pred = self.tokenizer.batch_decode(res)[0].removeprefix(self.tokenizer.batch_decode(tokenized)[0])
                
        return pred != 'Yes'
