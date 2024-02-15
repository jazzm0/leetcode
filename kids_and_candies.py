# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

import unittest
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [x + extraCandies >= max_value for x in candies]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([True, True, True, False, True], Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))

    def test_b(self):
        self.assertEqual([True, False, False, False, False], Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
