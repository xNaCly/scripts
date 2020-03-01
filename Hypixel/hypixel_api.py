# things to display:
# name
# rank
# first and last login
# social medias

import requests
import json
import requests
import colorama
from os import system as s
from config import api_key as key
from config import base_url as url
from colorama import Fore, Back, Style
colorama.init()

def rerun():
    s("cls")
    start()

def name_to_uudi(username):
    burl = "https://api.mojang.com/users/profiles/minecraft/{}".format(username)
    r = requests.get(burl)
    if r.status_code == 200:
        r_json = json.loads(r.content)
        uuid = r_json["id"]
        s("cls")
        print("Username " + Fore.GREEN +
              f"{username}" + Style.RESET_ALL + " found connected with")
        print(Fore.GREEN + f"{uuid}")
        return uuid
    else:
        print(Fore.RED + "There was a Problem, either wrong 'Username' or no internet connection" +
              Style.RESET_ALL + "\n")
        input("continue: ")
        rerun()

def hypixel_main_request(uuid, key, url):
    url = url + f"skyblock/profile?key={key}&profile={uuid}"
    r = requests.get(url)
    a = json.loads(r.text)

def start():
    name = input("Username: ")
    if name:
        uuid = name_to_uudi(name)
        hypixel_main_request(uuid, key, url)
    else:
        return rerun()
    
start()
