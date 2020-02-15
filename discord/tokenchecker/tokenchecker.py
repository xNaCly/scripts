import requests
import json
def main_main():
	auth = input("Token: ")
	#write_db(auth)
	payload = {'Authorization':f'{auth}'}
	r = requests.get('https://discordapp.com/api/v6/users/@me', headers=payload)
	x = json.loads(r.content)
	print(json.dumps(x, indent=4))
	input('\npress any button to continue... ')
	main_main_main()

#def write_db(token):
	#f = open("auth","a")
	#f.write("{0}\n".format(token))
	#f.close()

def main_main_main():
	main_main()

main_main()
