from covid_backend import RESPONSE

def displayLeaderboards(Type):
	Type.lower()
	if Type == "deaths":
		typestring = "TotalDeaths"
	elif Type == "cases":
		typestring = "TotalConfirmed"
	elif Type == "recovered":
		typestring = "TotalRecovered"

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
				finalTopFive += f"{y['Country']}: {x}\n"
	return finalTopFive


print(displayLeaderboards("deaths"))