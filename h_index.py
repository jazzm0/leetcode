import unittest
from typing import List


# https://leetcode.com/problems/h-index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations = sorted(citations, reverse=True)

        if n > 0 and citations[0] == 0:
            return 0

        for i in range(n - 1, -1, -1):
            if citations[i] >= i + 1:
                return i + 1
        return 1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        solution = Solution()

        self.assertEqual(3, solution.hIndex([3, 0, 6, 1, 5]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(1, solution.hIndex([3, 1, 1]))

    def test_c(self):
        solution = Solution()

        self.assertEqual(1, solution.hIndex([100]))

    def test_d(self):
        solution = Solution()

        self.assertEqual(2, solution.hIndex([15, 11]))

    def test_e(self):
        solution = Solution()

        self.assertEqual(0, solution.hIndex([0]))

    def test_f(self):
        solution = Solution()

        self.assertEqual(1, solution.hIndex([0, 1]))


if __name__ == "__main__":
    unittest.main()
