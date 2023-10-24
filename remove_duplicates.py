import unittest
from typing import List


# https://leetcode.com/problems/remove-element

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(set(nums))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        self.assertEqual(5, solution.removeDuplicates(a))


if __name__ == "__main__":
    unittest.main()
