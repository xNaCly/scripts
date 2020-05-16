# things to display:
# name
# rank
# first and last login
# social medias

import requests
import json
from datetime import datetime

from config import api_key as key
from config import base_url as url


def makeReadable(number):
	number = round(number)
	numberstring = str(number)
	newNumberstring = ""
	for x in numberstring:
		if len(numberstring) == 7:
			newNumberstring += x
			if len(newNumberstring) == 1:
				newNumberstring += "."
			if len(newNumberstring) == 5:
				newNumberstring += "."		
		if len(numberstring) == 6:
			newNumberstring += x
			if len(newNumberstring) == 3:
				newNumberstring += "."
		if len(numberstring) == 5:
			newNumberstring += x
			if len(newNumberstring) == 2:
				newNumberstring += "."
		if len(numberstring) == 4:
			newNumberstring += x
			if len(newNumberstring) == 1:
				newNumberstring += "."
	return newNumberstring


def timeStampToDate(timestamp):
    d = str(datetime.fromtimestamp(round(timestamp/1000)))
    return d

# username => string

# return object:
"""
{
  "name": "xnacly",
  "id": "2fdd2a195bf042f18c3c7e784f985a47"
}
"""
def name_to_uudi(username):
    burl = "https://api.mojang.com/users/profiles/minecraft/{}".format(
        username)
    r = requests.get(burl)
    if r.status_code == 200:
        r_json = json.loads(r.content)

        return r_json

    else:

        uuid = False
        return uuid

# uuid => string/integer

# return object:
"""
{
  "id" : "2fdd2a195bf042f18c3c7e784f985a47",
  "name" : "xnacly",
  "properties" : [ {
    "name" : "textures",
    "value" : "ewogICJ0aW1lc3RhbXAiIDogMTU4OTY1NDk2MjU0OCwKICAicHJvZmlsZUlkIiA6ICIyZmRkMmExOTViZjA0MmYxOGMzYzdlNzg0Zjk4NWE0NyIsCiAgInByb2ZpbGVOYW1lIiA6ICJ4bmFjbHkiLAogICJ0ZXh0dXJlcyIgOiB7CiAgICAiU0tJTiIgOiB7CiAgICAgICJ1cmwiIDogImh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDY0YWM1Y2FjM2RiNDQxYWRkNzJlYjZiOGRlMzg1MWMyY2MxMWVkOWU0MjE3NWY0ZDhmMzhjMjliNGMxNWYwOSIKICAgIH0KICB9Cn0="
  } ]
}
"""
def uuid_to_name(uuid):
    burl = "https://sessionserver.mojang.com/session/minecraft/profile/{}".format(
        uuid)
    r = requests.get(burl)
    nameobject = json.loads(r.content)

    return nameobject


# uuid => string/integer
# key  => hypixelAPI-key

# return object (simplified):

def hypixel_main_request(uuid):

    r = requests.get(f"{url}skyblock/profile?key={key}&profile={uuid}")
    skyblockUserObject = json.loads(r.text)

    return skyblockUserObject


# user => uuid/name
def format_object(userIDorName):
    userid = name_to_uudi(userIDorName)
    if userid == False:
        userid = uuid_to_name(userIDorName)
    
    user = hypixel_main_request(userid["id"])

    balance = makeReadable(user["profile"]["banking"]["balance"])
    purse = makeReadable(user["profile"]["members"][userid["id"]]["coin_purse"])


    memberarray = []
    for members in user["profile"]["members"]:
        memberarray.append(members)
    
    newMemberArray = []
    for member in memberarray:
        userobject = uuid_to_name(member)
        newMemberArray.append(userobject["name"])
        
    memberarray = newMemberArray
    finalUserObject = {
        "name": userid["name"],
        "uuid": userid["id"],
        "lastsave": timeStampToDate(user["profile"]["members"][userid["id"]]["last_save"]),
        "members": memberarray,
        "balance": balance,
        "purse": purse,
        "skills":{
            "combat":"",
            "mining":"",
            "foraging":"",
            "fishing":"",
            "farming":"",
            "alchemy":"",
            "enchanting":"",
            "taming":"",
            "rune":"",
            "carpentry":""
        }
    }
    finalUserObject = str(finalUserObject).replace("\'", "\"")
    return finalUserObject


def testREMOVEAFTERFINISH():
    final = json.loads(format_object("xnacly"))
    finall = json.dumps((final), indent=2)
    print(finall)

testREMOVEAFTERFINISH()
