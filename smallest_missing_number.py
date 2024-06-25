# https://leetcode.com/problems/first-missing-positive/

import unittest
from typing import List


class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     nums = set(nums)
    #     m = max(nums)
    #     if m < 1:
    #         return 1
    #     for i in range(1, m):
    #         if i not in nums:
    #             return i
    #     return m + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        m = max(nums)
        if m < 1:
            return 1

        n = 1
        for i in range(len(nums)):
            if nums[i] < 1:
                continue
            if nums[i] == n:
                n += 1
        return n


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(3, Solution().firstMissingPositive([1, 2, 0]))

    def test_b(self):
        self.assertEqual(2, Solution().firstMissingPositive([3, 4, -1, 1]))

    def test_c(self):
        self.assertEqual(2, Solution().firstMissingPositive([3, 4, -1, 1]))

    def test_d(self):
        self.assertEqual(3, Solution().firstMissingPositive([2, 1]))

    def test_e(self):
        self.assertEqual(2, Solution().firstMissingPositive([0, -1, 3, 1]))

    def test_f(self):
        self.assertEqual(3, Solution().firstMissingPositive([0, 2, 2, 1, 1]))
