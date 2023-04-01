# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 4


# Zadanie 2
def make_ruler(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Podano zla wartosc")

    miarka = ""
    for i in range(n):
        miarka += "|...."
    miarka += "|\n"

    for i in range(n):
        if len(str(i)) == 1 and i != 9:
            miarka += str(i) + "    "
        else:
            miarka += str(i) + "   "

    miarka += str(n)
    return miarka


def make_grid(rows, cols):
    try:
        rows = int(rows)
        cols = int(cols)
    except ValueError:
        raise ValueError("Podano zle wartosci")

    prostokat = ""
    for i in range(rows):
        string_pomocniczy = ""
        for j in range(cols):
            prostokat += "+---"
            string_pomocniczy += "|   "
        prostokat += "+\n"
        string_pomocniczy += "|\n"
        prostokat += string_pomocniczy

    for i in range(cols):
        prostokat += "+---"
    prostokat += "+"
    return prostokat


print("Zadanie 2")
print(make_ruler(21))
print(make_grid(2, 4))


# Zadanie 3
def factorial(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Podano zla wartosc")

    silnia = 1
    for i in range(n):
        silnia *= (i + 1)

    return silnia


print("\nZadanie 3")
print(factorial(4))


# Zadanie 4
def fibonacci(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Podano zla wartosc")

    if n == 0:
        return 0

    fib0 = 0
    fib1 = 1
    for i in range(n - 1):
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib

    return fib1


print("\nZadanie 4")
print(fibonacci(19))


# Zadanie 5
def odwracanie_iteracyjne(L, left, right):
    try:
        left = int(left)
        right = int(right)
    except ValueError:
        raise ValueError("Podano zle wartosci")

    while left < right:
        element = L[left]
        L[left] = L[right]
        L[right] = element
        left += 1
        right -= 1

    return L


def odwracanie_rekurencyjne(L, left, right):
    try:
        left = int(left)
        right = int(right)
    except ValueError:
        raise ValueError("Podano zle wartosci")

    if left >= len(L) or right >= len(L):
        return L

    if left < right:
        element = L[left]
        L[left] = L[right]
        L[right] = element
        odwracanie_rekurencyjne(L, left + 1, right - 1)

    return L


Lista = [1, 2, 3, 4, 5]
print("\nZadanie 5")
print(odwracanie_iteracyjne(Lista, 0, 4))
print(odwracanie_rekurencyjne(Lista, 0, 4))


# Zadanie 6
def sum_seq(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += sum_seq(item)
        else:
            suma += item

    return suma


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("\nZadanie 6")
print(sum_seq(seq))


# Zadanie 7
def flatten(sequence):
    L = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L = L + flatten(item)
        else:
            L.append(item)

    return L


print("\nZadanie 7")
print(flatten(seq))
