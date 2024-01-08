import unittest
from typing import List


# https://leetcode.com/problems/merge-intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals)
        i = 0

        while i < len(intervals) - 1:
            if intervals[i + 1][0] <= intervals[i][1]:
                intervals[i] = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
                del intervals[i + 1]
            else:
                i += 1

        return intervals


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_b(self):
        self.assertEqual([[1, 5]], Solution().merge([[1, 4], [4, 5]]))

    def test_c(self):
        self.assertEqual([[0, 4]], Solution().merge([[1, 4], [0, 4]]))


if __name__ == "__main__":
    unittest.main()
