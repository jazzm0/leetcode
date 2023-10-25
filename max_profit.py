import unittest
from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        max_diff = prices[1] - prices[0]
        min_element = prices[0]

        for i in range(1, n):
            if prices[i] - min_element > max_diff:
                max_diff = prices[i] - min_element

            if prices[i] < min_element:
                min_element = prices[i]
        return max_diff


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(7, solution.maxProfit([7, 1, 5, 3, 6, 4, 8]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(3, solution.maxProfit([1, 4, 2]))


if __name__ == "__main__":
    unittest.main()
