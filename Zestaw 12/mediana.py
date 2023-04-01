# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 12
# Zadanie 3

import unittest


def mediana_sort(L, left, right):
    wycinek_listy = L[left: right]
    wycinek_listy.sort()
    n = len(wycinek_listy)
    if n % 2 == 0:
        return wycinek_listy[(n // 2) - 1]    # mediana dolna
    return wycinek_listy[((n + 1) // 2) - 1]


class TestList(unittest.TestCase):

    def test_mediana(self):
        L = [pow(-2, i) for i in range(11)]             # [1, -2, 4, -8, 16, -32, 64, -128, 256, -512, 1024]
        self.assertEqual(mediana_sort(L, 0, 11), 1)     # [-512, -128, -32, -8, -2, 1, 4, 16, 64, 256, 1024]
        self.assertEqual(mediana_sort(L, 0, 10), -2)    # [-512, -128, -32, -8, -2, 1, 4, 16, 64, 256]
        self.assertEqual(mediana_sort(L, 3, 6), -8)     # [-32, -8, 16]


if __name__ == '__main__':
    unittest.main()
