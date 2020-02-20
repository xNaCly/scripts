import pydsb
import requests
import json
from tkinter import *
def auth(url):
    r = requests.get(url)
    a = json.loads(r.content)
    global b, c
    b, c = a["ab"], a["cd"]
def get_plans(usrnme, pw):
    dsb = pydsb.PyDSB(usrnme, pw)
    d = dsb.get_plans()
    for e in d:
        v = StringVar()
        v.set(e["url"])
        Entry(r, textvariable=v, width=250).pack()
        r.geometry("1000x100")
auth("https://raw.githubusercontent.com/xnacly1/auth/master/noauth")
def packed():
	get_plans(b,c)
r = Tk()
r.title("Tkinter Test")
r.geometry("200x200")
button = Button(r, text="BUTTON", command=packed).pack()
r.mainloop()
