import requests
import json
def main_main():
	auth = input("Token: ")
	payload = {'Authorization':f'{auth}'}
	r = requests.get('https://discordapp.com/api/v6/users/@me', headers=payload)
	x = json.loads(r.content)
	print(json.dumps(x, indent=4))
	input('\npress any button to continue... ')
	main_main_main()
def main_main_main():
	main_main()

main_main()
