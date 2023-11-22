import unittest
from typing import List


# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            row = [0] * n
            for j in range(n):
                row[n - j - 1] = matrix[j][i]
            matrix.append(row)

        for i in range(n):
            del matrix[0]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        Solution().rotate(m)
        self.assertEqual(m, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])


if __name__ == "__main__":
    unittest.main()
