# things to display:
# name
# rank
# first and last login
# social medias


import requests
import json
from config import api_key as key
from config import base_url as url


def rerun():
    start()


def name_to_uudi(username):
    burl = "https://api.mojang.com/users/profiles/minecraft/{}".format(
        username)
    r = requests.get(burl)
    if r.status_code == 200:
        r_json = json.loads(r.content)
        return r_json["id"]
    else:
        print("There was a Problem, either wrong 'Username' or no internet connection")


def hypixel_main_request(uuid, key, url):
    # url = url + f"player?key={key}&uuid={uuid}"
    url = url + f"skyblock/profile?key={key}&profile={uuid}"
    r = requests.get(url)
    # a = json.loads(r.text)
    # b = json.dumps(a, indent=4)
    # print(b)
    # profile id in player.stats.skyblock
    # player stats in skyblock.members.{uuid} ✅


def start():
    name = input("Username: ")
    if name:
        uuid = name_to_uudi(name)
        hypixel_main_request(uuid, key, url)
    else:
        return rerun()


start()
