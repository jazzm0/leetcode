import unittest
from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        max_profit = 0
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(7, solution.maxProfit([7, 1, 5, 3, 6, 4]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(3, solution.maxProfit([1, 4, 2]))


if __name__ == "__main__":
    unittest.main()
