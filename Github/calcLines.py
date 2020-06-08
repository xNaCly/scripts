import requests
import json

repoLink = "Flam3rboy/gykivideo"
repoLink = repoLink.split("/")
path = f"https://api.github.com/repos/{repoLink[0]}/{repoLink[1]}/stats/contributors"

r = requests.get(path)
repoAct = json.loads(r.text)
totalLines = 0
for x in repoAct:
	for y in x["weeks"]:
		totalLines = totalLines + y["a"]

print(totalLines)
