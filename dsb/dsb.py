"""
>---	Simple dsb-script	---<
request dsb plans using https://raw.githubusercontent.com/xNaCly/auth/master/config.json?token=ALMDHGO2KFJA34ARICR7VH26JE7VK
writes them to a file

"""
import pydsb
import requests
import uuid
def w_fi(salt, date, content):
	date = date.replace(" ", "--")
	date = date.replace(":", "-")
	content = content.replace("\\r", " ")
	content = content.replace("\\b", " ")
	content = content.replace("\\n", " ")
	content = content.replace("b'", " ")
	content = content.replace('\\xdc','Ue')
	content = content.replace('\\xfc','ue')
	content = content.replace('\\xf6','oe')
	f = open(str(date)+"._"+salt +".html", "w")
	f.write(str(content))
	f.close()
def auth(url):
    r = requests.get(url)
    a = json.loads(r.content)
    global b, c
    b, c = a["username"], a["password"]
def get_plans(usrnme, pw):
    dsb = pydsb.PyDSB(usrnme, pw)
    d = dsb.get_plans()
    for e in d:
        plan_url = e["url"]
        date = e["uploaded_date"]
        rr = requests.get(plan_url)
        print(rr.status_code)
        salty = str(uuid.uuid4())
        w_fi(salty, date, str(rr.content))
auth("https://raw.githubusercontent.com/xNaCly/auth/master/config.json?token=ALMDHGO2KFJA34ARICR7VH26JE7VK")
get_plans(b, c)
