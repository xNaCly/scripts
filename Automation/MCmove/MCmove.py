import os
import shutil

# get current User as name [string]
user = os.getlogin()

 # path to minecraft mod folder
path = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"

# get current working dir
oldpath = os.getcwd() 

print(f"start moving files from:\n{oldpath}\nto\n{path}\n")
# iterate trough all files in oldpath
for file in os.listdir(): 
	# split files into array --> test.jar => ["test", "jar"]
	y = file.split(".")

	# check if file ending is "jar", using len()-1 if other "." are in the file name --> betterframes (1.8.9).jar => ["betterframes ", "(1", "8", "9)", "jar"]
	if y[len(y)-1] == "jar":
		# move file from oldpath to modpath
		shutil.move(f"{oldpath}\\{file}", f"{path}\\mods\\{file}")
		print(f"moved {file}")
	
	if y[len(y)-1] == "zip":
		# move file from oldpath to txpath
		shutil.move(f"{oldpath}\\{file}", f"{path}\\resourcepacks\\{file}")
		print(f"moved {file}")

print("finished moving")