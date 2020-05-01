# xnacly
from pypresence import Presence
from win32gui import GetWindowText, GetForegroundWindow
from time import sleep as s
import time


def log(process):
    date = time.asctime(time.localtime(time.time()))
    f = open("log", "a")
    f.write(process + " | " + str(date) + "\n")
    f.close()


timer = int(time.time())
RPC = Presence("651125823457329152")
RPC.connect()
prc_name = ""  # input()
s(2)
if prc_name == "":
    while True:
        penis = GetWindowText(GetForegroundWindow())
        if penis == "":
            penis = "error 404"

        RPC.update(state=f"{penis}", start=timer, large_image="uwu",
                   large_text=f"{penis}", small_image="uwu", small_text="made by xNaCly#6370")
        print(penis + " | " + str(timer))
        log(penis)
        s(15)
else:
    while True:
        penis = prc_name
        if len(penis) >= 125:
            penis = "error - task string too long"
        RPC.update(state=f"{penis}", start=timer, large_image="uwu",
                   large_text=f"{penis}", small_image="uwu", small_text="made by xNaCly#6370")
        log(penis)
        print(penis + " | " + str(timer))
        s(15)
