import math

def wczytaj_liczbe(komunikat):
    while True:
        try:
            return(int(input(komunikat)))
        except ValueError:
            print("To nie jest liczba, spróbuj jeszcze raz.")

while True:
    dzialanie = input("Jakie działanie chcesz zrobić? (+, -, *, /, ^2, p, !, q = wyjście): ")
    
    if dzialanie == "q":
        break

    if dzialanie not in ["+", "-", "*", "/", "^2", "p", "!"]:
        print("Nieznane działanie")

    
    liczba1 = wczytaj_liczbe("Podaj liczbę 1: ")

    if dzialanie in ["+", "-", "*", "/", "^2", "p", "!"]:
        liczba2 = wczytaj_liczbe("Podaj liczbę 2: ")
    
    if dzialanie == "+":
        print("Suma tych liczb to:", liczba1 + liczba2)
    elif dzialanie == "-":
        print("Różnica tych liczb to:", liczba1 - liczba2)
    elif dzialanie == "*":
        print("Iloczyn tych liczb to:", liczba1 * liczba2)
    elif dzialanie == "/":
        if liczba2 == 0:
            print("Nie można dzielić przez 0!")
        else:
            print("Iloraz tych liczb to:", liczba1 / liczba2)
    elif dzialanie == "^2":
        print("Kwadrat liczby", liczba1, "to:", liczba1 ** 2)
    elif dzialanie == "!":
        if liczba1 < 0:
            print("Nie można liczyć silni z liczby ujemnej!")
        else:
            print("Silnia z", liczba1, "to:", math.factorial(liczba1))
    elif dzialanie == "p":
        if liczba1 < 0:
            print("Nie można liczyć pierwiastka z liczby ujemnej!")
        else:
            print("Pierwiastek z", liczba1, "to:", math.sqrt(liczba1))

