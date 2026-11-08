import json
zadania = ["kupić liptona", "robić matmę"]

with open("zadania.json", "w", encoding="utf-8") as plik:
    json.dump(zadania, plik, ensure_ascii=False)