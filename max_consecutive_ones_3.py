import unittest
from typing import List


# https://leetcode.com/problems/max-consecutive-ones-iii
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end, zero_count, ans = 0, 0, 0, 0

        while end < len(nums):
            if nums[end] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            ans = max(ans, end - start + 1)
            end += 1

        return ans


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(6, Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

    def test_b(self):
        self.assertEqual(10, Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))

    def test_c(self):
        self.assertEqual(4, Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 0))
