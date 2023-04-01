# Dominik Juszczyk
# Python 3.8
# Jezyk Python grupa nr 2
# Zestaw 9
# Zadanie 2

import unittest


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def search(self, data):
        if self.is_empty():
            return None
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        return None

    def find_min(self):
        if self.is_empty():
            return None
        min_node = self.head
        node = self.head
        while node is not None:
            if node.data < min_node.data:
                min_node = node
            node = node.next
        return min_node

    def find_max(self):
        if self.is_empty():
            return None
        max_node = self.head
        node = self.head
        while node is not None:
            if node.data > max_node.data:
                max_node = node
            node = node.next
        return max_node

    def reverse(self):
        prev = None
        node = self.head
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.head = prev


class TestList(unittest.TestCase):

    def test_search(self):
        l = SingleList()
        n1 = Node(20)
        n2 = Node(10, n1)
        l.insert_head(n2)
        self.assertEqual(l.search(10), n2)
        self.assertEqual(l.search(20), n1)
        self.assertEqual(l.search(30), None)

    def teest_find_min(self):
        l = SingleList()
        n1 = Node(20)
        n2 = Node(10, n1)
        l.insert_head(n2)
        self.assertEqual(l.find_min(), n2)
        self.assertEqual(SingleList().find_min(), None)

    def test_find_max(self):
        l = SingleList()
        n1 = Node(20)
        n2 = Node(10, n1)
        l.insert_head(n2)
        self.assertEqual(l.find_max(), n1)
        self.assertEqual(SingleList().find_max(), None)

    def test_reverse(self):
        l = SingleList()
        n1 = Node(20)
        n2 = Node(10, n1)
        l.insert_head(n2)
        l.reverse()
        self.assertEqual(l.head, n1)
        self.assertEqual(l.tail, n2)


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

