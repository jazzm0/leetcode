import unittest
from typing import List


# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i in range(len(nums)):
            if nums[i] in indexes and i - indexes[nums[i]] <= k:
                return True
            indexes[nums[i]] = i
        return False


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_b(self):
        self.assertEqual(True, Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))


if __name__ == "__main__":
    unittest.main()
