# xnacly
from pypresence import Presence
from win32gui import GetWindowText, GetForegroundWindow
import time


def log(process):
    date = time.asctime(time.localtime(time.time()))
    f = open("log", "a")
    f.write(process + " | " + str(date) + "\n")
    f.close()


timer = int(time.time())
RPC = Presence("651125823457329152")
RPC.connect()
time.sleep(2)

while True:
    windowstring = GetWindowText(GetForegroundWindow())

    if len(windowstring) >= 125:
        windowstring = "error - task string too long"

    if windowstring == "":
        windowstring = "error 404"

    RPC.update(state=f"{windowstring}", start=timer, large_image="uwu",
                   large_text=f"{windowstring}", small_image="uwu", small_text="made by xnacly#6370")

    print(windowstring + " | " + str(timer))

    log(windowstring)
    time.sleep(15)