import unittest
from typing import List


# https://leetcode.com/problems/jump-game-ii

class Solution:
    def longestJump(self, nums: List[int], start_position) -> int:
        i, offset, best = start_position - 1, 1, start_position - 1
        while i >= 0:
            if nums[i] >= offset:
                best = i
            i -= 1
            offset += 1
        return best

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        index, jump_count = n - 1, 0
        while index > 0:
            index = self.longestJump(nums, index)
            jump_count += 1
        return jump_count


class TestStringMethods(unittest.TestCase):

    def test_a1(self):
        solution = Solution()

        self.assertEqual(1, solution.longestJump([2, 3, 1, 1, 4], 4))

    def test_a2(self):
        solution = Solution()

        self.assertEqual(1, solution.longestJump([2, 3, 0, 1, 4], 4))

    def test_a(self):
        solution = Solution()

        self.assertEqual(2, solution.jump([2, 3, 1, 1, 4]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(2, solution.jump([2, 3, 0, 1, 4]))


if __name__ == "__main__":
    unittest.main()
