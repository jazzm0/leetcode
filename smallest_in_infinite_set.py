import unittest

from sortedcontainers import SortedSet


# https://leetcode.com/problems/smallest-number-in-infinite-set

class SmallestInfiniteSet:

    def __init__(self):
        self.ss = SortedSet([x for x in range(1, 1001)])

    def popSmallest(self) -> int:
        return self.ss.pop(0)

    def addBack(self, num: int) -> None:
        return self.ss.add(num)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        smallest = SmallestInfiniteSet()
        self.assertEqual(1, smallest.popSmallest())
        self.assertEqual(2, smallest.popSmallest())
        self.assertEqual(3, smallest.popSmallest())
        self.assertEqual(4, smallest.popSmallest())
        smallest.addBack(1)
        self.assertEqual(1, smallest.popSmallest())
        self.assertEqual(5, smallest.popSmallest())
