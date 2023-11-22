import unittest
from typing import List, Tuple


# https://leetcode.com/problems/set-matrix-zeroes

class Solution:

    def fillZeroes(self, matrix: List[List[int]], coordinate: Tuple[int]) -> None:
        for i in range(0, len(matrix)):
            matrix[i][coordinate[1]] = 0
        for i in range(0, len(matrix[0])):
            matrix[coordinate[0]][i] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes_in_row = zeroes.get(i, list())
                    zeroes_in_row.append(j)
                    zeroes[i] = zeroes_in_row
        for k, v in zeroes.items():
            for j in v:
                self.fillZeroes(matrix, (k, j))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        Solution().setZeroes(m)
        self.assertEqual([[1, 0, 1], [0, 0, 0], [1, 0, 1]], m)

    def test_b(self):
        m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        Solution().setZeroes(m)
        self.assertEqual([[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], m)


if __name__ == "__main__":
    unittest.main()
