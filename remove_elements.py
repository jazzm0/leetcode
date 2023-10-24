import unittest
from typing import List


# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                if i > 0:
                    i -= 1
            else:
                i += 1
        return len(nums)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        a = [3, 2, 2, 3]

        self.assertEqual(2, solution.removeElement(a, 3))


if __name__ == "__main__":
    unittest.main()
