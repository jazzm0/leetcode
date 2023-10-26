import unittest
from typing import List


# https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(5, solution.candy([1, 0, 2]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(4, solution.candy([1, 2, 2]))

    def test_c(self):
        solution = Solution()

        self.assertEqual(7, solution.candy([1, 3, 2, 2, 1]))

    def test_d(self):
        solution = Solution()

        self.assertEqual(13, solution.candy([1, 2, 87, 87, 87, 2, 1]))

    # 1, 2, 3, 2, 2, 2, 1


if __name__ == "__main__":
    unittest.main()
