import os
import json

with open("extensions.csv", "a") as f:
	for file in os.listdir():
		try:
			mainfest = json.loads(open(f"{file}\\manifest.json").read())
		except:
			continue
		f.write(f"{file}," + mainfest["name"] + "," + mainfest["description"] + "," + mainfest["version"] + "\n") 
