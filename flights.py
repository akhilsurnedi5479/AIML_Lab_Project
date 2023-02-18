import requests
import json
import config
params = {
	'access_key': config.api_key,
	'adults':	1,
	'origin':	'MAD',
	'destination':	'FCO',
	'departureDate':	'2023-02-28'

}

#?access_key=YOUR_ACCESS_KEY&adults=1&origin=MAD&destination=FCO&departureDate=2023-02-28
url = "https://app.goflightlabs.com/search-best-flights"
api_result = requests.get(url, params)

api_response = api_result.json()
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(api_response, f, ensure_ascii=False, indent=4)
print(api_response)

# headers = {
# 	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
# 	"X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
# print(response.url)
