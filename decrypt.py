import json
import getpass
import pyperclip

jsonFile = open("keys.json").read()
keys = json.loads(jsonFile)

decryptedPWD = str()
pwd = getpass.getpass(prompt="Enter encrypted password: ")
encryptedPWDList = list()


if len(pwd) % 8 != 0:
    print("The encrypted password isn't in proper format")

else:
    lenOfEncryptedPWD = len(pwd) // 8
    rest = pwd[0:]
    for _ in range(lenOfEncryptedPWD):
        part = rest[:8]
        rest = rest[8:]
        encryptedPWDList.append(part)

    for singleChar in encryptedPWDList:
        print(singleChar)
        for key, value in keys.items():
            if singleChar == value:
                decryptedPWD += key

    if len(decryptedPWD) < 1:
        print("We couldn't find any matching decryption keys !")
    else:
        print()
        print("~~~~MENU~~~~")
        print("Enter 1 to print the decrypted password on the screen")
        print("Enter 2 to copy the decrypted password to the clipboard")
        print("Enter 3 to copy the decrypted password to the clipboard and print it on the screen")
        print("Invalid response means 1")
        option = input()
        if option == "1":
            print(decryptedPWD)
        elif option == "2":
            pyperclip.copy(decryptedPWD)
        else:
            print(decryptedPWD)
