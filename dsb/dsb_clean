import pydsb
import requests
import json
def auth(url):
    r = requests.get(url)
    a = json.loads(r.content)
    global b, c
    b, c = a["ab"], a["cd"]
def get_plans(usrnme, pw):
    dsb = pydsb.PyDSB(usrnme, pw)
    d = dsb.get_plans()
    for e in d:
        print(e["uploaded_date"])
        print(e["url"] + "\n")
auth("https://raw.githubusercontent.com/xnacly1/auth/master/noauth")
get_plans(b, c)
