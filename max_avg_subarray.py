# https://leetcode.com/problems/maximum-average-subarray-i/

import unittest
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = max_avg = sum(nums[:k])
        for i in range(k, len(nums)):
            avg = avg - nums[i - k] + nums[i]
            max_avg = max(max_avg, avg)
        return max_avg / k


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(12.75000, Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))

    def test_b(self):
        self.assertEqual(5.0000, Solution().findMaxAverage([5], 1))

    def test_c(self):
        self.assertEqual(-1.0000, Solution().findMaxAverage([-1], 1))

    def test_d(self):
        self.assertEqual(4.0000, Solution().findMaxAverage([0, 4, 0, 3, 2], 1))
