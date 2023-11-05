import unittest
from typing import List

from sortedcontainers import SortedSet


# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remainder = [0] * n
        peaks = SortedSet()
        s = 0
        for i in range(n):
            remainder[i] = gas[i] - cost[i]
            peaks.add((remainder[i], i))
            s += remainder[i]

        if s < 0:
            return -1

        while len(peaks) > 0:
            best = peaks.pop()
            i, tank = best[1], 0
            if remainder[i] < 0:
                continue
            for j in range(n):
                tank += remainder[(i + j) % n]
                if tank < 0:
                    break

            if j == n - 1:
                return i
        return -1


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(3, solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(0, solution.canCompleteCircuit([2], [2]))


if __name__ == "__main__":
    unittest.main()
