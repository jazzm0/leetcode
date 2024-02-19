# https://leetcode.com/problems/max-number-of-k-sum-pairs

import unittest
from typing import List, Optional


class Solution:

    def get(self, key: int, counts: dict) -> Optional[int]:
        if key in counts:
            counts[key] = counts[key] - 1
            if counts[key] == 0:
                del counts[key]
            return key
        return None

    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        operations = 0
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        while len(counts) > 0:
            key = next(iter(counts))
            self.get(key, counts)
            diff = k - key
            if self.get(diff, counts):
                operations += 1
        return operations


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(2, Solution().maxOperations([1, 2, 3, 4], 5))

    def test_b(self):
        self.assertEqual(1, Solution().maxOperations([3, 1, 3, 4, 3], 6))
