import requests
import config


def toolbench_request(params):
	headers = {"toolbench_key": config.TOOLBENCH_KEY}
	return requests.post(config.TOOLBENCH_SERVICE_URL, json=params, headers=headers, timeout=15)


def rapidapi_request(url, host):
	headers = {
    	"X-RapidAPI-Key":config.RAPID_API_KEY,
    	"X-RapidAPI-Host": host	
    }

	return requests.get(url, headers=headers)