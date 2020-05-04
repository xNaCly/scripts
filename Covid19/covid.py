import requests
import json
import os



def errorLogger(error):
	with open("log", "a") as f:
		f.write(f"\n\n{error}")


def requestStats():
	try:
		r = requests.get("https://api.covid19api.com/summary")
		rr = json.loads(str(r.text))
		return rr
	except Exception as e:
		print("! While trying to establish a internet-connection, \nan error occured, \ntry disabling your firewall, or adding this program to the whitelist !")
		errorLogger(e)
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