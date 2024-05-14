# https://leetcode.com/problems/equal-row-and-column-pairs
import unittest
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, counts, rows = len(grid), 0, {}

        for i in range(n):
            rows[repr(grid[i])] = rows.get(repr(grid[i]), 0) + 1

        for i in range(n):
            column = []
            for j in range(n):
                column.append(grid[j][i])

            if repr(column) in rows:
                counts += rows[repr(column)]
        return counts


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(1, Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
