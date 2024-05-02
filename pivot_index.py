# https://leetcode.com/problems/find-pivot-index

import unittest
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        if s == 0:
            return 0
        current_sum = 0
        for i in range(len(nums)):
            if 2 * current_sum == (s - nums[i]):
                return i
            current_sum += nums[i]

        return -1


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(3, Solution().pivotIndex([1, 7, 3, 6, 5, 6]))

    def test_b(self):
        self.assertEqual(-1, Solution().pivotIndex([1, 2, 3]))

    def test_c(self):
        self.assertEqual(0, Solution().pivotIndex([2, 1, -1]))

    def test_d(self):
        self.assertEqual(-1, Solution().pivotIndex([-1] * 6))
