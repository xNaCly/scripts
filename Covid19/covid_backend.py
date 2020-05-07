import requests
import json

# make leaderboards
# format numbers better: (rn: 1000000) --> (after: 1.000.000)

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

	rr = RESPONSE
	c = ""
	x = 0
	for x in rr['Global']:
		# if x == 'TotalConfirmed':
		# 	c += f"{x}: {rr['Global'][x]}\n*estimated number is approx. x4 higher*\n"
		# 	break
		c += f"{x}: {rr['Global'][x]}\n"
	c += f"\nGlobalLethalityRate : {round((rr['Global']['TotalDeaths']*100)/rr['Global']['TotalConfirmed'], 2)}%\n*not accurate, because there are not tested infectious cases*"
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
				if y == 'Date':
					break
				if y == 'NewConfirmed':
					c += "\n"
				c += f"{y}: {x[y]}\n"
			c += f"\nDeaths relative to Global: {round((x['TotalDeaths']*100)/rr['Global']['TotalDeaths'], 2)}%\n"
			c += f"Cases relative to Global: {round((x['TotalConfirmed']*100)/rr['Global']['TotalConfirmed'], 2)}%"
			c += f"\nRecovered relative to Global: {round((x['TotalRecovered']*100)/rr['Global']['TotalRecovered'], 2)}%"
			c += f"\nLethality rate in {x['Country']}: {round((x['TotalDeaths']*100)/x['TotalConfirmed'], 2)}% \n*not accurate, because there are not tested infectious cases*"
			break
		if x['Slug'].lower() == Country.lower():
			for y in x:
				if y == 'Date':
					break
				if y == 'NewConfirmed':
					c += "\n"
				c += f"{y}: {x[y]}\n"
			c += f"\nDeaths relative to Global: {round((x['TotalDeaths']*100)/rr['Global']['TotalDeaths'], 2)}%\n"
			c += f"Cases relative to Global: {round((x['TotalConfirmed']*100)/rr['Global']['TotalConfirmed'], 2)}%"
			c += f"\nRecovered relative to Global: {round((x['TotalRecovered']*100)/rr['Global']['TotalRecovered'], 2)}%"
			c += f"\nLethality rate in {x['Country']}: {round((x['TotalDeaths']*100)/x['TotalConfirmed'], 2)}% \n*not accurate, because there are not tested infectious cases*"
			break
		if x['CountryCode'].lower() == Country.lower():
			for y in x:
				if y == 'Date':
					break
				if y == 'NewConfirmed':
					c += "\n"
				c += f"{y}: {x[y]}\n"
			c += f"\nDeaths relative to Global: {round((x['TotalDeaths']*100)/rr['Global']['TotalDeaths'], 2)}%\n"
			c += f"Cases relative to Global: {round((x['TotalConfirmed']*100)/rr['Global']['TotalConfirmed'], 2)}%"
			c += f"\nRecovered relative to Global: {round((x['TotalRecovered']*100)/rr['Global']['TotalRecovered'], 2)}%"
			c += f"\nLethality rate in {x['Country']}: {round((x['TotalDeaths']*100)/x['TotalConfirmed'], 2)}% \n*not accurate, because there are not tested infectious cases*"
			break
	if c == "":
		c = "Country not found - try using `c!countries` for a list of all available countries"
	return c


# def displayLeaderBoards():

# 	c = ""
# 	if Type == "deaths":
# 		# get all deaths
# 		# sort by highest
# 		# display top five: CountryName | DeathAmount
# 		for x in rr['Countries']:

# 		return c
# 	elif Type == "recovered":
# 		return c		
# 	elif Type == "cases":
# 		return c
