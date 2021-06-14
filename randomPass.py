import random
import pyperclip
import chars

duplicateAllChars = chars.allChars

password = list()
while True:
    lenOfPWD = input("Enter the length of random password: ")
    try:
        lenOfPWD = int(lenOfPWD)
        break
    except:
        print("Invalid length of random password. ")
        continue

for _ in range(lenOfPWD):
    digitOfKey = random.choice(duplicateAllChars)
    password.append(digitOfKey)
    duplicateAllChars.remove(digitOfKey)
random.shuffle(password)
password = "".join(password)

print()
print("~~~~MENU~~~~")
print("Enter 1 to print the generated password on the screen")
print("Enter 2 to copy the generated password to the clipboard")
print("Enter 3 to copy the generated password to the clipboard and print it on the screen")
print("Invalid response means 1")
option = input()
if option == "1":
    print(password)
elif option == "2":
    pyperclip.copy(password)
else:
    print(password)
