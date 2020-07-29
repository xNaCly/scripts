from pypresence import Presence
import time
config = None
with open("prefs", "r") as f:
    config = f.read()
    config = config.split("\n")
timer = int(time.time())
RPC = Presence(config[0].split("=")[1])
RPC.connect()
time.sleep(2)
while True:
    RPC.update(
        state=config[1].split("=")[1], 
        start=timer, 
        large_image=config[2].split("=")[1],
        large_text=config[3].split("=")[1], 
        small_image=config[4].split("=")[1],
        small_text=config[5].split("=")[1]
    )
    time.sleep(15)