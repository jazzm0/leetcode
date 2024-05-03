# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
import unittest
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        compressed = []
        i = 0
        max_count = 0
        while i < n:
            count, j = 0, 0
            for j in range(i, n):
                if nums[j] == 1:
                    count += 1
                else:
                    break
            if count > 0:
                max_count = max(max_count, count)
                compressed.append(count)
                i = j + 1
            else:
                i += 1
            compressed.append(0)

        if len(compressed) == 2:
            return compressed[0] - 1

        for i in range(1, len(compressed) - 1):
            if compressed[i] == 0 and compressed[i - 1] != 0 and compressed[i + 1] != 0:
                max_count = max(max_count, compressed[i - 1] + compressed[i + 1])
                
        return max_count


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(3, Solution().longestSubarray([1, 1, 0, 1]))

    def test_b(self):
        self.assertEqual(5, Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))

    def test_c(self):
        self.assertEqual(2, Solution().longestSubarray([1, 1, 1]))

    def test_d(self):
        self.assertEqual(4, Solution().longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]))

    def test_e(self):
        self.assertEqual(1, Solution().longestSubarray([1, 0, 0, 0, 0]))
