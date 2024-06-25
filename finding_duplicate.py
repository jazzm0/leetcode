# https://leetcode.com/problems/find-the-duplicate-number

import unittest
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(2, Solution().findDuplicate([1, 3, 4, 2, 2]))
