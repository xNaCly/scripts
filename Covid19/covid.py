import requests
import json
response_object = """{
	"Global":{
		"NewConfirmed":83608,
		"TotalConfirmed":2400051,
		"NewDeaths":5534,
		"TotalDeaths":165012,
		"NewRecovered":31584,
		"TotalRecovered":623259
		},
	"Date":"2020-04-20T17:48:21Z"
	}"""
r = requests.get("https://api.covid19api.com/summary")
rr = json.loads(str(r.text))
print("\n")
for x in rr['Global']:
	print(f"{x}: {rr['Global'][x]}")
print(rr['Date'])
