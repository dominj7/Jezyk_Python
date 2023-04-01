# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 7
# Zadanie 5

from points import Point
import math
import unittest


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * pow(self.radius, 2)

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def greater(self, other):
        if self.radius >= other.radius:
            return self
        return other

    def cover(self, other):
        length_between_points = math.sqrt(pow(self.pt.x - other.pt.x, 2) + pow(self.pt.y - other.pt.y, 2))
        rsub = math.sqrt(pow(self.radius - other.radius, 2))
        radd = self.radius + other.radius
        # Okregi styczne/rozlaczne wewnetrznie
        if length_between_points <= rsub:
            return self.greater(other)

        if length_between_points >= radd:
            new_radius = (length_between_points + radd) / 2

            if self.pt.x == other.pt.x:
                new_x = self.pt.x
            elif self.pt.x > other.pt.x:
                new_x = self.pt.x + self.radius - new_radius
            else:
                new_x = self.pt.x - self.radius + new_radius

            if self.pt.y == other.pt.y:
                new_y = self.pt.y
            elif self.pt.y > other.pt.y:
                new_y = self.pt.y + self.radius - new_radius
            else:
                new_y = self.pt.y - self.radius + new_radius

            return Circle(new_x, new_y, new_radius)


class TestCircle(unittest.TestCase):

    def setUp(self):
        pass

    def test_repr_circle(self):
        self.assertEqual(Circle(1, 2, 3).__repr__(), "Circle(1, 2, 3)")
        self.assertEqual(Circle(-1, 2, 5).__repr__(), "Circle(-1, 2, 5)")
        self.assertEqual(Circle(10, -2, 12).__repr__(), "Circle(10, -2, 12)")

    def test_eq_circle(self):
        self.assertTrue(Circle(2, 4, 3) == Circle(2, 4, 3))
        self.assertFalse(Circle(-1, -2, 0) == Circle(2, 4, 3))

    def test_ne_circle(self):
        self.assertFalse(Circle(2, 4, 3) != Circle(2, 4, 3))
        self.assertTrue(Circle(-1, -2, 0) != Circle(2, 4, 3))

    def test_area_circle(self):
        self.assertEqual(round(Circle(1, 2, 3).area(), 2), 28.27)
        self.assertEqual(round(Circle(-1, 2, 5).area(), 2), 78.54)
        self.assertEqual(round(Circle(10, -2, 12).area(), 2), 452.39)

    def test_move_circle(self):
        self.assertEqual(Circle(1, 2, 3).move(1, 1), Circle(2, 3, 3))
        self.assertEqual(Circle(-1, 2, 5).move(0, 20), Circle(-1, 22, 5))
        self.assertEqual(Circle(10, -2, 12).move(-2, 0), Circle(8, -2, 12))

    def test_cover_circle(self):
        self.assertEqual(Circle(1, -2, 3).cover(Circle(-4, -2, 2)), Circle(-1, -2, 5))
        self.assertEqual(Circle(6, 0, 5).cover(Circle(5, 1, 1)), Circle(6, 0, 5))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
