import unittest
from typing import List


# https://leetcode.com/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        if n == 0 or n == 1:
            return n
        longest, start = 1, 0
        while start < n:
            j = start
            while j < n - 1:
                if nums[j + 1] - nums[j] != 1:
                    break
                j += 1
            longest = max(longest, j - start + 1)
            start = j + 1
        return longest


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test_b(self):
        self.assertEqual(9, Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

    def test_c(self):
        self.assertEqual(3, Solution().longestConsecutive([1, 2, 0, 1]))


if __name__ == "__main__":
    unittest.main()
