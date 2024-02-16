# https://leetcode.com/problems/increasing-triplet-subsequence

import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def find_next_higher_position(self, values_index: int, min_index: int, values: List[int], positions: dict) -> (
    int, int):
        for i in range(values_index + 1, len(values)):
            next_index = bisect_left(positions[values[i]], min_index)
            if next_index < len(positions[values[i]]) and positions[values[i]][next_index] > min_index:
                return i, positions[values[i]][next_index]
        return None, -1

    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        positions = {}
        values = []
        for i in range(n):
            if nums[i] not in positions:
                position = positions.get(nums[i], list())
                position.append(i)
                positions[nums[i]] = position
                values.append(nums[i])
            else:
                positions[nums[i]].append(i)
        values = sorted(values)
        for i in range(len(values)):
            next_next, next_index = self.find_next_higher_position(i, positions[values[i]][0], values, positions)
            if next_index >= 0:
                if self.find_next_higher_position(next_next, next_index, values, positions)[1] > 0:
                    return True
        return False


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().increasingTriplet([1, 2, 3, 4, 5]))

    def test_b(self):
        self.assertEqual(True, Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))

    def test_c(self):
        self.assertEqual(True, Solution().increasingTriplet([1, 5, 0, 4, 1, 3]))

    def test_d(self):
        self.assertEqual(False, Solution().increasingTriplet([2, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1]))
