import unittest
from typing import List


# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        a = [1, 2, 3, 4, 5, 6, 7]
        solution.rotate(a, 3)

        self.assertEqual([5, 6, 7, 1, 2, 3, 4], a)


if __name__ == "__main__":
    unittest.main()
