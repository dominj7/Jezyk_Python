# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 11
# Zadanie 4

from lists import a
from sort import *
from timeit import timeit
from matplotlib import pyplot as plt


def time(functions, number_of_elements):
    results = []
    for function in functions:
        result = []
        for n in number_of_elements:
            L = a(n)
            result.append(timeit(lambda: function(L, 0, n - 1), number=1))
        results.append(result)
    return results
    
    
print('Sortuję...')

N1 = [10 ** 2, 10 ** 3, 10 ** 4]
N2 = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

# Sortowanie listy zawierajacej wiecj niz 10^4 elementow mniej wydajnymi algorytmami trwa zbyt dlugo
first = time([selectsort, bubblesort], N1)
second = time([mergesort, quicksort], N2)

for i in range(5):
    print('Dla n = ', N2[i])
    if i < 3:
        print('\tSelection Sort: ', first[0][i])
        print('\tBubble Sort: ', first[1][i])
    print('\tMerge Sort: ', second[0][i])
    print('\tQuick Sort: ', second[1][i])


plt.plot(N1, first[0], label='Selection Sort')
plt.plot(N1, first[1], label='Bubble Sort')
plt.xlabel('Liczba elementow')
plt.ylabel('Czas')
plt.legend()
plt.show()


plt.plot(N2, second[0], label='Merge Sort')
plt.plot(N2, second[1], label='Quick Sort')
plt.xlabel('Liczba elementow')
plt.ylabel('Czas')
plt.legend()
plt.show()
