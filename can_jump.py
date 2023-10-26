import unittest
from typing import List


# https://leetcode.com/problems/jump-game

class Solution:
    def canJumpFromPosition(self, nums: List[int], position: int) -> bool:
        i = position - 1
        offset = 1
        while i >= 0:
            if nums[i] > offset or (nums[i] == offset and position == len(nums) - 1):
                return True
            offset += 1
            i -= 1
        return False

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        for i in range(n):
            if nums[i] == 0 and not self.canJumpFromPosition(nums, i):
                return False
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(True, solution.canJump([2, 3, 1, 1, 4]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(False, solution.canJump([3, 2, 1, 0, 4]))

    def test_c(self):
        solution = Solution()

        self.assertEqual(True, solution.canJump([2, 0, 0]))


if __name__ == "__main__":
    unittest.main()
