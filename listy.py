import os, json
os.system('cls')

try:
    with open("zadania.json", "r", encoding="utf-8") as plik:
        zadania = json.load(plik)
except FileNotFoundError:
    zadania = []

def dodaj_zadania(zadania):
    tresc = input("Wpisz zadanie: ")
    zadania.append({tresc})
    zapisz_zadania(zadania)

def pokaz_zadania(zadania):
    if len(zadania) == 0:
        print("Brak zadań.")
    else:
        for numer, zadanie in enumerate(zadania, start=1):
            print("Numer zadania:", numer)
            print("-", zadanie)

def usun_zadanie_po_tekscie(zadania):
    do_usuniecia = input("Które zadanie usunąć? ")
    if do_usuniecia in zadania:
        zadania.remove(do_usuniecia)
        zapisz_zadania(zadania)
        print("Usunięto!")
    else:
        print("Nie ma takiego zadania.")

def usun_zadanie_po_numerze(zadania):
    numer_tekst = input("Podaj numer zadania do usunięcia: ")
    if numer_tekst.isdigit():
        numer = int(numer_tekst)
        if numer >= 1 and numer <= len(zadania):
            zadania.pop(numer - 1)
            zapisz_zadania(zadania)
            print("Usunięto!")
        else:
            print("Nie ma zadania o takim numerze.")
    else:
        print("To nie jest liczba.")

def zapisz_zadania(zadania):
    with open("zadania.json", "w", encoding="utf-8") as plik:
        json.dump(zadania, plik, ensure_ascii=False)

while True:
    wybor = input("1 = dodaj, 2 = pokaż, 3 = usuń, 4 = usuń po numerze, q = wyjście: ")

    if wybor == "1":
        dodaj_zadania(zadania)        
    elif wybor == "2":
        pokaz_zadania(zadania)
    elif wybor == "3":
        usun_zadanie_po_tekscie(zadania)
    elif wybor == "4":
        usun_zadanie_po_numerze(zadania)
    elif wybor == "q":
        break
    else:
        print("Nieznana opcja!")
        