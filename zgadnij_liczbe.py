import random

def wczytaj_liczbe(komunikat):
    while True:
        try:
            return(int(input(komunikat)))
        except ValueError:
            print("To nie jest liczba, spróbuj jeszcze raz.")

def wczytaj_maksimum():
    while True:
        maksimum = wczytaj_liczbe("Do jakiej liczby gramy? (10 / 100 / 1000): ")
        if maksimum in [10, 100, 1000]:
            return maksimum
        print("Wybierz 10, 100 lub 1000!")

wygrane = 0
przegrane = 0

while True:
    maksimum = wczytaj_maksimum()
    
    if maksimum <= 10:
        limit = 4
    elif maksimum <= 100:
        limit = 7
    else:
        limit = 10
    
    tajna = random.randint(1, maksimum)
    proby = 0

    while True:
        strzal = wczytaj_liczbe(f"Zgadnij liczbę od 1 do {maksimum}: ")
        proby += 1

        if strzal == tajna:
            print("Brawo! Zgadłeś w", proby, "próbach.")
            wygrane += 1
            break

        if strzal < tajna:
            print("Za mało!")
        else:
            print("Za dużo!")

        if proby >= limit:
            print("Przegrałeś, liczba to", tajna)
            przegrane += 1
            break

    odpowiedz = input("Zagrać jeszcze raz? (t/n): ")
    if odpowiedz != "t":
        break

print("Wygrane:", wygrane, "Przegrane:", przegrane)