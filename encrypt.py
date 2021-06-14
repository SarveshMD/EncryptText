import json
import getpass
import pyperclip

jsonFile = open("keys.json").read()
keys = json.loads(jsonFile)

while True:
    pwd = getpass.getpass()
    encryptedPWD = str()
    if len(pwd) < 8:
        print(
            "WARNING: Length of password is less than 8 characters. This password might be easier to crack"
        )
        print("Recommended password size is at least 8 characters.")
        option = input("Do you want to change the password (y/n Default is y) ?  ")
        if option.lower() != "n":
            continue
    pwdList = list(pwd)
    for item in pwdList:
        encryptedPWD += keys[item]
    break

print()
print("~~~~MENU~~~~")
print("Enter 1 to print the encrypted password on the screen")
print("Enter 2 to copy the encrypted password to the clipboard")
print("Enter 3 to copy the encrypted password to the clipboard and print it on the screen")
print("Invalid response means 1")
option = input()
if option == "1":
    print(encryptedPWD)
elif option == "2":
    pyperclip.copy(encryptedPWD)
else:
    print(encryptedPWD)
