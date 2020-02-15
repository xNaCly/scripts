from textwrap import wrap
import subprocess


def starting():
    return start()


def start():
    file = input("Filename: ")
    action = input("Action: [remove/wrap]: ")

    if action == "wrap":
        return wraping(file)

    if action == "remove":
        return remove(file)


def remove(file1):
    f = open(f"{file1}", "r")
    txt = f.read().upper()
    f.close()

    txt1 = txt.replace("'", "")
    txt2 = txt1.replace("[", "")
    txt3 = txt2.replace("]", "")
    txt4 = txt3.replace(",", "")
    o = open("file.txt", "w")
    o.write(str(txt4))
    subprocess.run(['clip.exe'], input=txt4.encode('utf-16'), check=True)
    o.close()


def wraping(file2):
    f = open(f"{file2}", "r")
    txt = f.read().upper()
    f.close()

    text = wrap(txt, 2)
    o = open("file.txt", "w")
    o.write(str(text))
    o.close()
    remove(file2)


starting()
