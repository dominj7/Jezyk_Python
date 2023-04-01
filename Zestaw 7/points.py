# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 6
# Zadanie 2

import math
import unittest


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def __hash__(self):
        return hash((self.x, self.y))


# Kod testujacy modul
class TestPoint(unittest.TestCase):

    def setUp(self):
        self.zero = Point(0, 0)

    def test_str_point(self):
        self.assertEqual(Point(5, 8).__str__(), "(5, 8)")
        self.assertEqual(Point(2, -3).__str__(), "(2, -3)")
        self.assertEqual(Point(100, 0).__str__(), "(100, 0)")

    def test_repr_point(self):
        self.assertEqual(Point(5, 8).__repr__(), "Point(5, 8)")
        self.assertEqual(Point(2, -3).__repr__(), "Point(2, -3)")
        self.assertEqual(Point(100, 0).__repr__(), "Point(100, 0)")

    def test_eq_points(self):
        self.assertTrue(Point(2, 4) == Point(2, 4))
        self.assertFalse(Point(0, 0) == Point(21, 4))

    def test_ne_points(self):
        self.assertFalse(Point(2, 4) != Point(2, 4))
        self.assertTrue(Point(0, 0) != Point(21, 4))

    def test_add_points(self):
        self.assertEqual(Point(5, 8) + Point(2, 4), Point(7, 12))
        self.assertEqual(Point(2, -3) + Point(2, 4), Point(4, 1))
        self.assertEqual(Point(100, 0) + Point(-100, 100), Point(0, 100))

    def test_sub_points(self):
        self.assertEqual(Point(5, 8) - Point(2, 4), Point(3, 4))
        self.assertEqual(Point(2, -3) - Point(2, 4), Point(0, -7))
        self.assertEqual(Point(100, 0) - Point(-100, 100), Point(200, -100))

    def test_mul_points(self):
        self.assertEqual(Point(5, 8) * Point(2, 4), 42)
        self.assertEqual(Point(2, -3) * Point(2, 4), -8)
        self.assertEqual(Point(100, 0) * Point(-100, 100), -10000)

    def test_cross_points(self):
        self.assertEqual(Point(5, 8).cross(Point(2, 4)), 4)
        self.assertEqual(Point(2, -3).cross(Point(2, 4)), 14)
        self.assertEqual(Point(100, 0).cross(Point(-100, 100)), 10000)

    def test_length_point(self):
        self.assertEqual(round(Point(5, 8).length(), 2), 9.43)
        self.assertEqual(round(Point(2, -3).length(), 2), 3.61)
        self.assertEqual(round(Point(100, 0).length(), 2), 100)

    def tes_hash_point(self): pass

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
