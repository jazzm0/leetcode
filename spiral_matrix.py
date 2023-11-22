import unittest
from typing import List


# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while len(matrix) > 0 and len(matrix[0]) > 0:

            for i in range(len(matrix[0])):
                result.append(matrix[0][0])
                del matrix[0][0]
            del matrix[0]
            for i in range(0, len(matrix)):
                result.append(matrix[i][len(matrix[i]) - 1])
                del matrix[i][len(matrix[i]) - 1]

            if len(matrix) > 0:
                for i in range(len(matrix[0]) - 1, -1, -1):
                    result.append(matrix[len(matrix) - 1][i])
                    del matrix[len(matrix) - 1][i]

                del matrix[len(matrix) - 1]

            if len(matrix) > 0 and len(matrix[0]) > 0:
                for i in range(len(matrix) - 1, -1, -1):
                    result.append(matrix[i][0])
                    del matrix[i][0]

        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_b(self):
        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
                         Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

    def test_c(self):
        self.assertEqual([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
                         Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

    def test_d(self):
        self.assertEqual([7, 9, 6],
                         Solution().spiralOrder([[7], [9], [6]]))


if __name__ == "__main__":
    unittest.main()
