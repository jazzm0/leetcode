import unittest
from typing import List


# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)

        ans = 0
        arrow = -1

        for point in sorted(points, key=lambda x: x[1]):
            if point[0] > arrow:
                ans += 1
                arrow = point[1]

        return ans


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(2, Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))

    def test_b(self):
        self.assertEqual(2, Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))

    def test_c(self):
        self.assertEqual(2, Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))

    def test_d(self):
        self.assertEqual(2, Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))


if __name__ == "__main__":
    unittest.main()
