import unittest
from typing import List


# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end, max_area = 0, len(height) - 1, 0
        while start < end:
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(49, Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_b(self):
        self.assertEqual(1, Solution().maxArea([1, 1]))


if __name__ == "__main__":
    unittest.main()
