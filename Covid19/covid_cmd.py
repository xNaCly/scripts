import requests
import json
import os
from sys import platform
from covid_backend import displayAllCountries, globalStats, displayOneCountry
clearstring = ""
if platform == "win32":
	clearstring = "cls"
else:
	clearstring = "clear"
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
		print(globalStats())
		fallbackFun()
	elif cmd == "2":
		print(displayAllCountries())
		fallbackFun()	
	elif cmd == "3":
		coun = input("Country: ")
		print(displayOneCountry(coun))
		fallbackFun()
	elif cmd == "3":
		coun = input("Leaderboards: ")
		print(displayOneCountry(coun))
		fallbackFun()
def fallbackFun():
	input("\nPress any Button to get back... ")
	os.system(clearstring)
	main()
main()
