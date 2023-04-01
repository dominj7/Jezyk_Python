# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 3

import zadania

while True:
    zadanie = input("\nPodaj numer zadania:\nq == wyjscie\n")
    try:
        zadanie = int(zadanie)
    except ValueError:
        if zadanie == 'q':
            break
        print("\tNie ma takiego zadania")
    else:
        if zadanie == 3:
            zadania.zad3()
        elif zadanie == 4:
            zadania.zad4()
        elif zadanie == 5:
            zadania.zad5()
        elif zadanie == 6:
            zadania.zad6()
        elif zadanie == 8:
            zadania.zad8()
        elif zadanie == 9:
            zadania.zad9()
        elif zadanie == 10:
            zadania.zad10()
        else:
            print("\tNie ma takiego zadania")
