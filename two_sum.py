import unittest
from typing import List


# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            indexes[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in indexes and indexes[target - nums[i]] != i:
                return [i, indexes[target - nums[i]]]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([0, 1], Solution().twoSum([2, 7, 11, 15], 9))

    def test_b(self):
        self.assertEqual([1, 2], Solution().twoSum([3, 2, 4], 6))


if __name__ == "__main__":
    unittest.main()
