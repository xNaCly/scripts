import requests
import json

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
	
	# NewConfirmed: 90841
	# TotalConfirmed: 3658565
	# NewDeaths: 4734
	# TotalDeaths: 257093
	# NewRecovered: 84832
	# TotalRecovered: 1195874
	# 2020-05-06T16:21:13Z

	rr = RESPONSE
	c = ""
	for x in rr['Global']:
		c += f"{x}: {rr['Global'][x]}\n"
	c += f"{rr['Date']}"
	return c


def displayAllCountries():
	
	# ALA Aland Islands | AX
	# Afghanistan | AF
	# Albania | AL
	# Algeria | DZ
	# American Samoa | AS
	# Andorra | AD

	rr = RESPONSE
	c = ""
	for x in rr['Countries']:
		c += f"{x['Country']} | {x['CountryCode']}\n"
	return c


def displayOneCountry(Country):

	# Country: United States of America
	# CountryCode: US
	# Slug: united-states
	# NewConfirmed: 0
	# TotalConfirmed: 1204351
	# NewDeaths: 0
	# TotalDeaths: 71064
	# NewRecovered: 0
	# TotalRecovered: 189791
	# Date: 2020-05-06T16:21:13Z

	rr = RESPONSE
	c = ""

	for x in rr['Countries']:
		if x['Country'].lower() == Country.lower(): 
			for y in x:
				c += f"{y}: {x[y]}\n"
			break
		if x['Slug'].lower() == Country.lower():
			for y in x:
				c += f"{y}: {x[y]}\n"
			break
		if x['CountryCode'].lower() == Country.lower():
			for y in x:
				c += f"{y}: {x[y]}\n"
			break

	return c


def displayLeaderBoards(Type):
	c = ""
	if Type == "deaths":
		pass
	elif Type == "recovered":
		pass
	elif Type == "cases":
		pass
