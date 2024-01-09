import unittest
from bisect import bisect_left
from typing import List


# https://leetcode.com/problems/insert-interval
class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)
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
        self.assertEqual([[1, 5], [6, 9]], Solution().insert([[1, 3], [6, 9]], [2, 5]))

    def test_b(self):
        self.assertEqual([[1, 2], [3, 10], [12, 16]],
                         Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


if __name__ == "__main__":
    unittest.main()
