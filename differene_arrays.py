# https://leetcode.com/problems/find-the-difference-of-two-arrays
import unittest
from typing import List


class Solution:
    def unique_nums(self, nums1: List[int], unique_nums2: set[int]) -> list[int]:
        return list(set([n for n in nums1 if n not in unique_nums2]))

    def findDifference(self, nums1: List[int], nums2: List[int]) -> list[list[int]]:
        return [self.unique_nums(nums1, set(nums2)), self.unique_nums(nums2, set(nums1))]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([[1, 3], [4, 6]], Solution().findDifference([1, 2, 3], [2, 4, 6]))
