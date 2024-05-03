# https://leetcode.com/problems/unique-number-of-occurrences
import unittest
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in range(len(arr)):
            counts[arr[i]] = counts.get(arr[i], 0) + 1
        seen = set()
        for v in counts.values():
            if v in seen:
                return False
            seen.add(v)
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))

    def test_b(self):
        self.assertEqual(True, Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

    def test_c(self):
        self.assertEqual(False, Solution().uniqueOccurrences([1, 2]))
