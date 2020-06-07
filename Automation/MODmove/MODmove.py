import os
import shutil

# get current User as name [string]
user = os.getlogin()

 # path to minecraft mod folder
newpath = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft\\mods"

# get current working dir
oldpath = os.getcwd() 


# iterate trough all files in oldpath
for x in os.listdir(): 
	# split files into array --> test.jar => ["test", "jar"]
	y = x.split(".")

	# check if file ending is "jar", using len()-1 if other "." are in the file name --> betterframes (1.8.9).jar => ["betterframes ", "(1", "8", "9)", "jar"]
	if y[len(y)-1] == "jar":
		# move file from oldpath to newpath
		shutil.move(oldpath + f"\\{x}", newpath + f"\\{x}")