import tkinter as t
import requests
from config import key as k
"""
flam3rboy.tk:25555

zum starten:
/start
wenn erfolgreich response = OK
wenn nicht response != OK

/stop
wenn erfolgreich response = OK
wenn nicht response != OK

/logs
um logs zu zeigen
"""

r = t.Tk()

base_url = "http://flam3rboy.tk:25555"

def show_logs():
	headers = {'Authorization':k}
	re = requests.get(base_url + "/logs", headers=headers)
	logs = re.text
	with open("log","w") as f:
		f.write("\n\n" + logs)
	if re.status_code == 200:
		kek["text"] = "Success"
	else:
		kek["text"] = "Error"
def start_server():
	headers = {'Authorization':k}
	re = requests.get(base_url + "/start", headers=headers)
	if re.status_code == 200:
		kek["text"] = "Success"
	else:
		kek["text"] = "Error"

def stop_server():
	headers = {'Authorization':k}
	re = requests.get(base_url + "/stop", headers=headers)
	if re.status_code == 200:
		kek["text"] = "Success"
	else:
		kek["text"] = "Error"

r.title("Minecraft Server Client")
r.geometry("400x220")
t.Label(r, text="Client to Start/Stop or show Logs of the flam3rboy.tk minecraft server", width=250).pack()
t.Button(r, text="Start Server", width=250, command=start_server).pack()
t.Button(r, text="Stop Server", width=250, command=stop_server).pack()
t.Button(r, text="Show Logs", width=250, command=show_logs).pack()
kek = t.Label(r, text="status", width=250)
kek.pack()

r.mainloop()
