# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 12
# Zadanie 1

from random import randint

n, k = 100, 10
random_list = [randint(0, k - 1) for i in range(n)]


def linear_search(L, left, right, element):
    results = list()
    i = left
    while i <= right:
        if L[i] == element:
            results.append(i)
            try:
                results += linear_search(L, i + 1, right, element)
            finally:
                return results
        i += 1
    return None


e = randint(0, k - 1)
print('Lista: ', random_list)
print('Szukany element: ', e)
print('Element znaleziono na indeksach: ', linear_search(random_list, 0, n - 1, e))
