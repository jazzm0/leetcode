import heapq
import unittest
from typing import List, Tuple


# https://leetcode.com/problems/total-cost-to-hire-k-workers


class Solution:

    def get_next(self, costs: List[Tuple[int, int]], next_candidates: List[Tuple[int, int]], candidates: int,
                 end: bool = False):
        if len(costs) == 0 or len(next_candidates) == candidates:
            return
        position = 0 if not end else -1
        candidate = costs[position]
        del costs[position]
        heapq.heappush(next_candidates, candidate)

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costs = [(costs[i], i) for i in range(len(costs))]
        left_candidates, right_candidates = [], []

        for i in range(candidates):
            self.get_next(costs, left_candidates, candidates)
            self.get_next(costs, right_candidates, candidates, True)

        total_costs, left, right = 0, None, None
        for _ in range(k):
            if not left and len(left_candidates) > 0:
                left = heapq.heappop(left_candidates)

            if not right and len(right_candidates) > 0:
                right = heapq.heappop(right_candidates)

            if not right or (left and left[0] <= right[0]):
                total_costs += left[0]

                if right and left[1] == right[1]:
                    right = None

                self.get_next(costs, left_candidates, candidates)
                left = None
            else:
                total_costs += right[0]

                if not left or left[1] == right[1]:
                    left = None

                self.get_next(costs, right_candidates, candidates, True)
                right = None
        return total_costs


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(11, Solution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))

    def test_b(self):
        self.assertEqual(4, Solution().totalCost([1, 2, 4, 1], 3, 3))

    def test_c(self):
        self.assertEqual(526, Solution().totalCost([57, 33, 26, 76, 14, 67, 24, 90, 72, 37, 30], 11, 2))

    def test_d(self):
        self.assertEqual(7, Solution().totalCost([2, 2, 1, 1, 1], 5, 3))
