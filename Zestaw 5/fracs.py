# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 5
# Zadanie 2

import math
import unittest


def test(frac):
    if not isinstance(frac, list) or len(frac) != 2 or frac[1] == 0:
        raise ValueError("Podano zla liczbe")


def skracanie(frac):
    test(frac)
    dzielnik = math.gcd(frac[0], frac[1])
    return [frac[0] / dzielnik, frac[1] / dzielnik]


def add_frac(frac1, frac2):
    test(frac1)
    test(frac2)

    liczik1 = frac1[0] * frac2[1]
    liczik2 = frac2[0] * frac1[1]
    return skracanie([liczik1 + liczik2, frac1[1] * frac2[1]])


def sub_frac(frac1, frac2):
    test(frac1)
    test(frac2)

    liczik1 = frac1[0] * frac2[1]
    liczik2 = frac2[0] * frac1[1]
    return skracanie([liczik1 - liczik2, frac1[1] * frac2[1]])


def mul_frac(frac1, frac2):
    test(frac1)
    test(frac2)

    return skracanie([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    test(frac1)
    test(frac2)
    if is_zero(frac2):
        raise ValueError("Nie wolno dzielic przez zero")

    return skracanie([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac):
    test(frac)

    if frac[0] * frac[1] > 0:
        return True
    return False


def is_zero(frac):
    test(frac)

    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2):
    test(frac1)
    test(frac2)

    liczik1 = frac1[0] * frac2[1]
    liczik2 = frac2[0] * frac1[1]
    if liczik1 == liczik2:
        return 0
    elif liczik1 > liczik2:
        return -1
    return 1


def frac2float(frac):
    test(frac)

    return float(frac[0] / frac[1])


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])
        self.assertEqual(add_frac([10, 3], [1, 2]), [23, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(sub_frac([10, 3], [1, 2]), [17, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-1, 2], [1, 2]), [-1, 4])
        self.assertEqual(mul_frac([10, 3], [1, 2]), [5, 3])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(div_frac([10, 3], [1, 2]), [20, 3])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 3]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([-1, 3]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, 3]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 1 / 2)
        self.assertEqual(frac2float([-1, 3]), -1 / 3)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
