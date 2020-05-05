import requests
import json
import os
from sys import platform


clearstring = ""
if platform == "linux" or platform == "linux2":
    clearstring = "clear"
elif platform == "darwin":
	clearstring = "clear"
elif platform == "win32":
	clearstring = "cls"




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
	os.system(clearstring)
	rr = RESPONSE
	for x in rr['Global']:
		print(f"{x}: {rr['Global'][x]}")
	print(rr['Date'])

def displayAllCoutries():
	os.system(clearstring)
	rr = RESPONSE
	for x in rr['Countries']:
		print(f"{x['Country']} | {x['CountryCode']}")

def displayOneCountry(Country):
	os.system(clearstring)
	rr = RESPONSE
	for x in rr['Countries']:
		if x['Country'].lower() == Country.lower(): 
			for y in x:
				print(f"{y}: {x[y]}")
			break
		if x['Slug'].lower() == Country.lower():
			for y in x:
				print(f"{y}: {x[y]}")
			break
		if x['CountryCode'].lower() == Country.lower():
			for y in x:
				print(f"{y}: {x[y]}")
			break
def main():
	print("""
+- COVID19 - info - script -+
+-xnacly-+	
arguments: 
1: global
2: allCountries
3: oneCountry
	\n\n
	""")
	cmd = input()
	if cmd == "1":
		globalStats()
		fallbackFun()
	elif cmd == "2":
		displayAllCoutries()
		fallbackFun()	
	elif cmd == "3":
		coun = input("Country: ")
		displayOneCountry(coun)
		fallbackFun()

def fallbackFun():
	input("\nPress any Button to get back... ")
	os.system(clearstring)
	main()

main()