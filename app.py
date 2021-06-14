import json

jsonFile = open("keys.json", "r").read()
keys = json.loads(jsonFile)


def decrypt(pwd):
    decryptedPWD = str()
    encryptedPWDList = list()
    if len(pwd) % 8 != 0:
        print("The encrypted password isn't in proper format")
        exit()
    lenOfEncryptedPWD = len(pwd) // 8
    rest = pwd[0:]
    for _ in range(lenOfEncryptedPWD):
        part = rest[:8]
        rest = rest[8:]
        encryptedPWDList.append(part)

    for singleChar in encryptedPWDList:
        for key, value in keys.items():
            if singleChar == value:
                decryptedPWD += key
    return decryptedPWD


def encrypt(pwd):
    encryptedPWD = str()
    pwdList = list(pwd)
    for item in pwdList:
        encryptedPWD += keys[item]
    return encryptedPWD


if __name__ == "__main__":
    while True:
        print("~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~")
        print("1. Encrypt something")
        print("2. Decrypt something")
        print("3. Create a random password")
        print("4. Quit")
        print(" : ", end="")
        option = input()
        if option == "1":
            exec(open("encrypt.py").read())
        elif option == "2":
            exec(open("decrypt.py").read())
        elif option == "3":
            exec(open("randomPass.py").read())
        else:
            exit()
