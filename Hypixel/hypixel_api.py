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
    burl = "https://api.mojang.com/users/profiles/minecraft/{}".format(
        username)
    r = requests.get(burl)
    if r.status_code == 200:
        r_json = json.loads(r.content)
        uuid = r_json["id"]
        s("cls")
        print("Username " + Fore.GREEN +
              f"{username}" + Style.RESET_ALL + " found connected with")
        print(Fore.GREEN + f"{uuid}\n" + Style.RESET_ALL)
        return uuid
    else:
        print(Fore.RED + "There was a Problem, either wrong 'Username' or no internet connection" +
              Style.RESET_ALL + "\n")
        input("continue: ")
        rerun()


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
    a = json.loads(r.text)

    def printy(des, content):
        contenter = a["profile"]["members"][uuid][content]
        print(des + ": " + Fore.GREEN + str(contenter) + Style.RESET_ALL)
    printy("Fairy Souls", "fairy_souls_collected")
    printy("Total Bosses", "death_count")
    print("\nPets:")
    for pet in a["profile"]["members"][uuid]["pets"]:
        if pet["tier"] == "COMMON":
            Raretiyy = Fore.WHITE
        if pet["tier"] == "UNCOMMON":
            Raretiyy = Fore.GREEN
        if pet["tier"] == "RARE":
            Raretiyy = Fore.BLUE
        if pet["tier"] == "EPIC":
            Raretiyy = '\033[0;95m'
        print("Name: " + Fore.GREEN + str(pet["type"]).replace("_", " ") + Style.RESET_ALL + "\nxp: " + Fore.GREEN + str(
            pet["exp"]) + Style.RESET_ALL)
        print("Rarity: ", Raretiyy, pet["tier"] + Style.RESET_ALL + "\n")
    # printy()


def start():
    name = input("Username: ")
    if name:
        uuid = name_to_uudi(name)
        hypixel_main_request(uuid, key, url)
        # uuid_to_name(uuid)
    else:
        return rerun()


start()
