# https://leetcode.com/problems/find-the-highest-altitude

import unittest
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude, largest_altitude = 0, 0
        for i in range(len(gain)):
            current_altitude += gain[i]
            largest_altitude = max(largest_altitude, current_altitude)
        return largest_altitude


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(1, Solution().largestAltitude([-5, 1, 5, 0, -7]))

    def test_b(self):
        self.assertEqual(0, Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
