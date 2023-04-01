# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 7
# Zadanie 3

from points import Point
import unittest


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1.__eq__(other.pt1) & self.pt2.__eq__(other.pt2)

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (self.pt2 - self.pt1).x * (self.pt2 - self.pt1).y

    def move(self, x, y):
        new_pt1 = self.pt1 + Point(x, y)
        new_pt2 = self.pt2 + Point(x, y)
        return Rectangle(new_pt1.x, new_pt1.y, new_pt2.x, new_pt2.y)

    def intersection(self, other):  # czesc wspolna prostokatow
        pt1 = Point(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y))
        pt2 = Point(min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        return Rectangle(pt1.x, pt1.y, pt2.x, pt2.y)

    def cover(self, other):  # prostąkąt nakrywający oba
        pt1 = Point(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y))
        pt2 = Point(max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        return Rectangle(pt1.x, pt1.y, pt2.x, pt2.y)

    def make4(self):  # zwraca krotkę czterech mniejszych
        bottom_left = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y)
        top_right = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y)
        bottom_right = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y)
        top_left = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y)
        return top_left, top_right, bottom_left, bottom_right


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def test_str_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).__str__(), "[(1, 2), (3, 4)]")
        self.assertEqual(Rectangle(-1, 2, 5, 3).__str__(), "[(-1, 2), (5, 3)]")
        self.assertEqual(Rectangle(10, -2, 12, 0).__str__(), "[(10, -2), (12, 0)]")

    def test_repr_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).__repr__(), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(Rectangle(-1, 2, 5, 3).__repr__(), "Rectangle(-1, 2, 5, 3)")
        self.assertEqual(Rectangle(10, -2, 12, 0).__repr__(), "Rectangle(10, -2, 12, 0)")

    def test_eq_rectangles(self):
        self.assertTrue(Rectangle(2, 4, 3, 5) == Rectangle(2, 4, 3, 5))
        self.assertFalse(Rectangle(-1, -2, 0, 0) == Rectangle(2, 4, 3, 5))

    def test_ne_rectangles(self):
        self.assertFalse(Rectangle(2, 4, 3, 5) != Rectangle(2, 4, 3, 5))
        self.assertTrue(Rectangle(-1, -2, 0, 0) != Rectangle(2, 4, 3, 5))

    def test_center_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).center(), Point(2, 3))
        self.assertEqual(Rectangle(-1, 2, 5, 3).center(), Point(2, 2.5))
        self.assertEqual(Rectangle(10, -2, 12, 0).center(), Point(11, -1))

    def test_area_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).area(), 4)
        self.assertEqual(Rectangle(-1, 2, 5, 3).area(), 6)
        self.assertEqual(Rectangle(10, -2, 12, 0).area(), 4)

    def test_move_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).move(1, 1), Rectangle(2, 3, 4, 5))
        self.assertEqual(Rectangle(-1, 2, 5, 3).move(0, 20), Rectangle(-1, 22, 5, 23))
        self.assertEqual(Rectangle(10, -2, 12, 0).move(-2, 0), Rectangle(8, -2, 10, 0))

    def test_intersection(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).intersection(Rectangle(2, 3, 4, 5)), Rectangle(2, 3, 3, 4))
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, 4).intersection(Rectangle(5, 6, 7, 8))

    def test_cover(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).cover(Rectangle(2, 3, 4, 5)), Rectangle(1, 2, 4, 5))
        self.assertEqual(Rectangle(1, 2, 3, 4).cover(Rectangle(5, 6, 7, 8)), Rectangle(1, 2, 7, 8))

    def make4(self):
        tup = (Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4), Rectangle(1, 2, 2, 3), Rectangle(2, 2, 3, 3))
        self.assertEqual(Rectangle(1, 2, 3, 4).make4(), tup)
        tup = (Rectangle(2, 4, 3, 5), Rectangle(3, 4, 4, 5), Rectangle(2, 3, 3, 4), Rectangle(3, 3, 4, 4))
        self.assertEqual(Rectangle(2, 3, 4, 5).make4(), tup)

    def tearDown(self): pass

    
if __name__ == '__main__':
    unittest.main()
