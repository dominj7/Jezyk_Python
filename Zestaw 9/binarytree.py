# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 9
# Zadanie 6

import unittest


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def count_leafs(top):
        if top is None:
            return 0
        leafs = 0
        if top.left is not None:
            leafs += top.left.count_leafs()
        if top.right is not None:
            leafs += top.right.count_leafs()
        if top.left is None and top.right is None:
            leafs += 1
        return leafs

    def count_total(top):
        if top is None:
            return 0
        total = top.data
        if top.left is not None:
            total += top.left.count_total()
        if top.right is not None:
            total += top.right.count_total()
        return total


class TestBinaryTree(unittest.TestCase):

    def test_count_leafs(top):
        left = Node(2)
        right = Node(301)
        root = Node(97, left, right)
        top.assertEqual(root.count_leafs(), 2)

    def test_count_total(top):
        left = Node(2)
        right = Node(301)
        root = Node(97, left, right)
        top.assertEqual(root.count_total(), 400)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
