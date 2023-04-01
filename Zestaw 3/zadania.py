# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 3


# Zadanie 3
def zad3():
    print("\tZadanie 3")
    for x in range(30):
        if x % 3 != 0:
            print("\t\t", x)


# Zadanie 4
def zad4():
    print("\tZadanie 4")
    while True:
        x = input("\t\tPodaj liczbe rzeczywista: ")
        try:
            x = float(x)
        except ValueError:
            if x == "stop":
                break
            print("\t\t\tPodano zla wartosc!")
        else:
            print("\t\t\tPodana liczba:\n\t\t\t\t", x)
            print("\t\t\tTrzecia potega podanej liczby:\n\t\t\t\t", pow(x, 3))


# Zadanie 5
def zad5():
    print("\tZadanie 5")
    miarka = ""
    dlugosc_miarki = int(input("\t\tPodaj dlugosc miarki: "))

    for i in range(dlugosc_miarki):
        miarka += "|...."
    miarka += "|\n"

    for i in range(dlugosc_miarki):
        if len(str(i)) == 1 and i != 9:
            miarka += str(i) + "    "
        else:
            miarka += str(i) + "   "

    miarka += str(dlugosc_miarki)
    print(miarka)


# Zadanie 6
def zad6():
    print("\tZadanie 6")
    wysokosc = int(input("\t\tPodaj wysokosc prostokata: "))
    szerokosc = int(input("\t\tPodaj szerokosc prostokata: "))
    prostokat = ""

    for i in range(wysokosc):
        string_pomocniczy = ""
        for j in range(szerokosc):
            prostokat += "+---"
            string_pomocniczy += "|   "
        prostokat += "+\n"
        string_pomocniczy += "|\n"
        prostokat += string_pomocniczy

    for i in range(szerokosc):
        prostokat += "+---"
    prostokat += "+"
    print(prostokat)


# Zadamie 8
def zad8():
    print("\tZadanie 8")
    sekwencja1 = [1, 2, 4, 5, 7, 8, 10]
    sekwencja2 = [2, 3, 5, 7, 11]
    print("\t\ta)\n\t\t\t", list(set(sekwencja1) & set(sekwencja2)))  # iloczyn zbiorow
    print("\t\tb)\n\t\t\t", list(set(sekwencja1) | set(sekwencja2)))  # suma zbiorow


# Zadanie 9
def zad9():
    print("\tZadanie 9")
    lista = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    sumy = list(sum(x) for x in lista)
    print("\t\tLista sekwencji:\n\t\t\t", lista)
    print("\t\tLista sum:\n\t\t\t", sumy)


# Zadanie 10
def zad10():
    print("\tZadanie 10")
    # Pierwszy sposob:
    rzymskie = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabskie = [1, 5, 10, 50, 100, 500, 1000]
    D1 = dict(zip(rzymskie, arabskie))
    print("\t\tSlownik stworzony pierwszym sposobem:\n\t\t\t", D1)

    # Drugi sposob:
    rzymskie = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabskie = [1, 5, 10, 50, 100, 500, 1000]
    D2 = {}
    for (i, j) in zip(rzymskie, arabskie):
        D2[i] = j
    print("\t\tSlownik stworzony drugim sposobem:\n\t\t\t", D2)
