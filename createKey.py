import random
import json
import chars

jsonFile = open("keys.json", "w")

allChars = chars.allChars

keys = dict()

for char in allChars:
    duplicateUpper = list()
    duplicateLower = list()
    duplicateNumbers = list()
    duplicateSymbols = list()
    duplicateUpper.extend(chars.alphaUpper)
    duplicateLower.extend(chars.alphaLower)
    duplicateNumbers.extend(chars.numbers)
    duplicateSymbols.extend(chars.symbols)
    key = list()
    for id in range(1, 9):
        if (id % 4) == 0:
            digitOfKey = random.choice(duplicateUpper)
            key.append(digitOfKey)
            duplicateUpper.remove(digitOfKey)
        if (id % 4) == 1:
            digitOfKey = random.choice(duplicateLower)
            key.append(digitOfKey)
            duplicateLower.remove(digitOfKey)
        elif (id % 4) == 2:
            digitOfKey = random.choice(duplicateNumbers)
            key.append(digitOfKey)
            duplicateNumbers.remove(digitOfKey)
        elif (id % 4) == 3:
            digitOfKey = random.choice(duplicateSymbols)
            key.append(digitOfKey)
            duplicateSymbols.remove(digitOfKey)
    random.shuffle(key)
    key = "".join(key)
    keys[char] = key

json.dump(keys, jsonFile, indent=4)
