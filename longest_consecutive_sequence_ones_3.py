import unittest
from typing import List


# https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        negative_positions = []
        while i < len(nums):
            element = nums[i]
            count = 0
            while i < len(nums) and nums[i] == element:
                count += 1
                del nums[i]
            if element == 0:
                count *= -1
                negative_positions.append(i)
            nums.insert(i, count)
            i += 1
        return 0


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(6, Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

    def test_b(self):
        self.assertEqual(10, Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))


if __name__ == "__main__":
    unittest.main()
