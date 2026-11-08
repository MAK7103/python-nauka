import json

with open("zadania.json", "r", encoding="utf-8") as plik:
    zadania = json.load(plik)

print(zadania)
print(zadania[0])