# https://leetcode.com/problems/move-zeroes

import unittest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        zero_count = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                zero_count += 1
            else:
                i += 1
        nums.extend([0] * zero_count)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        a = [0, 1, 0, 3, 12]
        Solution().moveZeroes(a)
        self.assertEqual([1, 3, 12, 0, 0], a)

    def test_b(self):
        a = [0]
        Solution().moveZeroes(a)
        self.assertEqual([0], a)

    def test_c(self):
        a = [0, 0, 1]
        Solution().moveZeroes(a)
        self.assertEqual([1, 0, 0], a)
