import os
import shutil

user = os.getlogin()
newpath = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft\\mods"
oldpath = os.getcwd()

for x in os.listdir():
	y = x.split(".")
	if y[len(y)-1] == "jar":
		shutil.move(oldpath + f"\\{x}", newpath + f"\\{x}")