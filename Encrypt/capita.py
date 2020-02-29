# project CAPITA
# xnacly 18/01/2020
from cryptography.fernet import Fernet
from os import system as s
from time import sleep as ß

standardkey = ""


def key():
    key = Fernet.generate_key()
    f = open("key.CAPITA", "wb")
    f.write(key)
    f.close()
    s("cls")
    print("wrote key to key.Capita file, save it somewhere else")
    ß(3)
    main()


def encrFile(key):
    filename = input("FileName or FileLocation (with ending): >> ")
    f = open(filename)
    content = f.read()
    f.close()

    contentenc = content.encode()
    F = Fernet(key)
    endfile = F.encrypt(contentenc)

    f = open(filename + ".CAPITA", "w")
    f.write(endfile.decode())
    f.close()
    s("cls")
    print("encrFile success")
    ß(3)
    main()


def decrFile(key):
    filename = input("FileName or FileLocation (with ending): >> ")
    f = open(filename)
    content = f.read()
    f.close()

    contentenc = content.encode()
    F = Fernet(key)
    endfile = F.decrypt(contentenc)

    f = open(filename.strip(".CAPITA"), "w")
    f.write(endfile.decode())
    f.close()
    s("cls")
    print("decrFile success")
    ß(3)
    main()


def main():
    s("cls")
    print("""
CAPITA -- v0.1 alpha

-- commands -- 
key     -> get a key
encrypt -> a file
decrypt -> a file

--------------------
	""")
    inputcommand = input("command: >> ")

    if inputcommand == "key":
        key()
    elif inputcommand == "encrypt":
        inputkey = input("key: >> ")
        encrFile(inputkey)
    elif inputcommand == "decrypt":
        inputkey = input("key: >> ")
        decrFile(inputkey)
    else:
        print("command isn't definded")
        ß(2)
        main()


if __name__ == '__main__':
    main()
