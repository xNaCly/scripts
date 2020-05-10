import requests
import json
from time import sleep as s

def errorLogger(error):
	with open("log", "a") as f:
		f.write(f"\n\n{error}")

def makeReadable(number):
	if type(number) != int:
		return number
	numberstring = str(number)
	newNumberstring = ""
	for x in numberstring:
		if len(numberstring) == 7:
			newNumberstring += x
			if len(newNumberstring) == 1:
				newNumberstring += "."
			if len(newNumberstring) == 5:
				newNumberstring += "."		
		if len(numberstring) == 6:
			newNumberstring += x
			if len(newNumberstring) == 3:
				newNumberstring += "."
		if len(numberstring) == 5:
			newNumberstring += x
			if len(newNumberstring) == 2:
				newNumberstring += "."
		if len(numberstring) == 4:
			newNumberstring += x
			if len(newNumberstring) == 1:
				newNumberstring += "."
	return newNumberstring

def requestStats():
	try:
		r = requests.get("https://api.covid19api.com/summary")
		returner = json.loads(str(r.text))
		return returner
	except Exception as e:
		print("! While trying to establish a internet-connection, \nan error occured, \ntry disabling your firewall, or adding this program to the whitelist !")
		errorLogger(e)

RESPONSE = requestStats()

def globalStats():
	rr = RESPONSE
	c = ""
	x = 0
	for x in rr['Global']:
		if x == 'NewConfirmed':
			continue
		if x == 'NewDeaths':
			continue
		if x == 'NewRecovered':
			continue
		c += f"{x}: {makeReadable(rr['Global'][x])}\n"
	c += f"\nCurrently ill: {makeReadable(rr['Global']['TotalConfirmed'] - (rr['Global']['TotalDeaths'] + rr['Global']['TotalRecovered']))} | {round((rr['Global']['TotalConfirmed'] - (rr['Global']['TotalDeaths'] + rr['Global']['TotalRecovered'])) * 100/rr['Global']['TotalConfirmed'])}%\n"
	c += f"\nGlobalLethalityRate : {round((rr['Global']['TotalDeaths']*100)/rr['Global']['TotalConfirmed'], 2)}%\n*not accurate, because there are not tested infectious cases*"
	return c

def displayAllCountries():
	rr = RESPONSE
	c = ""
	for x in rr['Countries']:
		c += f"{x['Country']} | {x['CountryCode']}\n"
	return c

def displayOneCountry(Country):
	rr = RESPONSE
	c = ""
	for x in rr['Countries']:
		if x['Country'].lower() == Country.lower():
			for y in x:
				if y == 'Date':
					continue
				if y == 'NewConfirmed':
					continue
				if y == 'NewDeaths':
					continue
				if y == 'NewRecovered':
					continue
				if y == 'TotalConfirmed':
					c += "\n"
				c += f"{y}: {makeReadable(x[y])}\n"
			c += f"Currently ill: {makeReadable(x['TotalConfirmed'] - (x['TotalDeaths'] + x['TotalRecovered']))} | {round((x['TotalConfirmed'] - (x['TotalDeaths'] + x['TotalRecovered'])) * 100/x['TotalConfirmed'])}%\n"
			c += f"\nDeaths from Global: {round((x['TotalDeaths']*100)/rr['Global']['TotalDeaths'], 2)}%\n"
			c += f"Cases from Global: {round((x['TotalConfirmed']*100)/rr['Global']['TotalConfirmed'], 2)}%"
			c += f"\nRecovered from Global: {round((x['TotalRecovered']*100)/rr['Global']['TotalRecovered'], 2)}%"
			c += f"\nLethality rate in {x['Country']}: {round((x['TotalDeaths']*100)/x['TotalConfirmed'], 2)}% \n*not accurate, because there are not tested infectious cases*"
			break
		if x['Slug'].lower() == Country.lower():
			for y in x:
				if y == 'Date':
					continue
				if y == 'NewConfirmed':
					continue
				if y == 'NewDeaths':
					continue
				if y == 'NewRecovered':
					continue
				if y == 'TotalConfirmed':
					c += "\n"
				c += f"{y}: {makeReadable(x[y])}\n"
			c += f"Currently ill: {makeReadable(x['TotalConfirmed'] - (x['TotalDeaths'] + x['TotalRecovered']))} | {round((x['TotalConfirmed'] - (x['TotalDeaths'] + x['TotalRecovered'])) * 100/x['TotalConfirmed'])}%\n"
			c += f"\nDeaths from Global: {round((x['TotalDeaths']*100)/rr['Global']['TotalDeaths'], 2)}%\n"
			c += f"Cases from Global: {round((x['TotalConfirmed']*100)/rr['Global']['TotalConfirmed'], 2)}%"
			c += f"\nRecovered from Global: {round((x['TotalRecovered']*100)/rr['Global']['TotalRecovered'], 2)}%"
			c += f"\nLethality rate in {x['Country']}: {round((x['TotalDeaths']*100)/x['TotalConfirmed'], 2)}% \n*not accurate, because there are not tested infectious cases*"
			break
		if x['CountryCode'].lower() == Country.lower():
			for y in x:
				if y == 'Date':
					continue
				if y == 'NewConfirmed':
					continue
				if y == 'NewDeaths':
					continue
				if y == 'NewRecovered':
					continue
				if y == 'TotalConfirmed':
					c += "\n"
				c += f"{y}: {makeReadable(x[y])}\n"
			c += f"Currently ill: {makeReadable(x['TotalConfirmed'] - (x['TotalDeaths'] + x['TotalRecovered']))} | {round((x['TotalConfirmed'] - (x['TotalDeaths'] + x['TotalRecovered'])) * 100/x['TotalConfirmed'])}%\n"
			c += f"\nDeaths from Global: {round((x['TotalDeaths']*100)/rr['Global']['TotalDeaths'], 2)}%"
			c += f"\nCases from Global: {round((x['TotalConfirmed']*100)/rr['Global']['TotalConfirmed'], 2)}%"
			c += f"\nRecovered from Global: {round((x['TotalRecovered']*100)/rr['Global']['TotalRecovered'], 2)}%"
			c += f"\nLethality rate in {x['Country']}: {round((x['TotalDeaths']*100)/x['TotalConfirmed'], 2)}% \n*not accurate, because there are not tested infectious cases*"
			break
	if c == "":
		c = "Country not found - try using `c!countries` for a list of all available countries"
	return c

def displayLeaderboards(Type):
	Type.lower()
	if Type == "deaths":
		typestring = "TotalDeaths"
	elif Type == "cases":
		typestring = "TotalConfirmed"
	elif Type == "recovered":
		typestring = "TotalRecovered"
	else: 
		typestring = "TotalConfirmed"
	numberarray = []
	for x in RESPONSE['Countries']:
		for y in x:
			if y == typestring:
				numberarray.append(x[typestring])
				break
	numberarray.sort(reverse=True)
	y = 0
	topFive = []
	for x in numberarray:
		if y == 5:
			break
		topFive.append(x)
		y = y + 1
	finalTopFive = ""
	for x in topFive:
		for y in RESPONSE['Countries']:
			if x == y[typestring]:
				finalTopFive += f"{y['Country']}: {makeReadable(x)}\n"
	return finalTopFive