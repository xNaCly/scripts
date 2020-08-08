import secrets
import string

service = input("service-name: ")
username = ''.join(secrets.choice(string.ascii_letters)for i in range(6))
password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(20))
with open("generated", "a") as f:
    f.write("\n" + service + ":" + username + "," + password)
