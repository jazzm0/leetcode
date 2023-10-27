import unittest
from random import randint


# https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:
    data = set()

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        exists = val not in self.data
        self.data.add(val)
        return exists

    def remove(self, val: int) -> bool:
        exists = val in self.data
        self.data.remove(val)
        return exists

    def getRandom(self) -> int:
        return list(self.data)[randint(0, len(self.data) - 1)]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        solution = RandomizedSet()

        self.assertEqual(True, solution.insert(1))
        self.assertEqual(True, solution.insert(2))
        self.assertEqual(False, solution.insert(1))
        self.assertEqual(True, solution.remove(2))
        self.assertEqual(1, solution.getRandom())


if __name__ == "__main__":
    unittest.main()
