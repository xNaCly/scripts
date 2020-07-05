import os
import json

user = os.getlogin()
chromepath = f"C:\\Users\\{user}\\AppData\\Local\\Chromium\\Application"

with open(".\\extensions.csv", "a") as f:
	filepath = os.listdir(chromepath)[0]
	for file in os.listdir(f"{chromepath}{filepath}\\Extensions"):
		try:
			mainfest = json.loads(open(f"{chromepath}{filepath}\\Extensions\\{file}\\manifest.json").read())
		except:
			continue
		f.write(f"{file}," + mainfest["name"] + "," + mainfest["description"] + "," + mainfest["version"] + "\n") 
