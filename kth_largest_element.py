import unittest
from typing import List


# https://leetcode.com/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(5, Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))

    def test_b(self):
        self.assertEqual(4, Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
