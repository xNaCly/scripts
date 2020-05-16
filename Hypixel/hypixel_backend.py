# things to display:
# name
# rank
# first and last login
# social medias

import requests
import json
from config import api_key as key
from config import base_url as url




def name_to_uudi(username):
    burl = "https://api.mojang.com/users/profiles/minecraft/{}".format(
        username)
    r = requests.get(burl)
    if r.status_code == 200:
        r_json = json.loads(r.content)
        uuid = r_json["id"]
        return uuid
    else:
        uuid = False
        return uuid


def uuid_to_name(uuid):
    burl = "https://sessionserver.mojang.com/session/minecraft/profile/{}".format(
        uuid)
    r = requests.get(burl)
    a = json.loads(r.content)
    name = a["name"]
    return name


def hypixel_main_request(uuid, key, url):
    url = url + f"skyblock/profile?key={key}&profile={uuid}"
    r = requests.get(url)
    skyblockUserObject = json.loads(r.text)
    return skyblockUserObject


def test():
    uuid = name_to_uudi("xnacly")
    url = f"https://api.hypixel.net/skyblock/profile?key={key}&profile={uuid}"
    r = requests.get(url)
    with open("test.txt", "w") as f:
        f.write(r.text)
