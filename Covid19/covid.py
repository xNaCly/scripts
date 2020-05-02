import requests
import json
import os

"""{
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

def requestStats():
	try:
		r = requests.get("https://api.covid19api.com/summary")
		rr = json.loads(str(r.text))
		return rr
	except:
		print("! While trying to establish a internet-connection, \nan error occured, \ntry disabling your firewall, or adding this program to the whitelist !")
		exit()

RESPONSE = requestStats()

def globalStats():
	rr = RESPONSE
	for x in rr['Global']:
		print(f"{x}: {rr['Global'][x]}")
	print(rr['Date'])

def displayAllCoutries():
	rr = RESPONSE
	for x in rr['Countries']:
		print(f"{x['Country']} | {x['CountryCode']}")

def displayOneCountry(Country):
	rr = RESPONSE
	
	for x in rr['Countries']:
		if x['Country'].lower() == Country.lower(): #== Country or x['Slug'] == Country or x['CountryCode'] == Country:
			for y in x:
				print(f"{y}: {x[y]}")
			break

def main():
	print("""
+- COVID19 - info - script -+
			+-xnacly-+	
arguments: global, allCountries, oneCountry
	\n\n
	""")
	cmd = input()
	if cmd == "global":
		globalStats()
		fallbackFun()
	elif cmd == "allCountries":
		displayAllCoutries()
		fallbackFun()	
	elif cmd == "oneCountry":
		coun = input("Country: ")
		displayOneCountry(coun)
		fallbackFun()

def fallbackFun():
	input("\nPress any Button to get back... ")
	os.system("cls")
	main()

main()