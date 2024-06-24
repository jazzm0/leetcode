# https://leetcode.com/problems/daily-temperatures

import unittest
from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = [(temperatures[x], x) for x in range(len(temperatures))]
        s = [temperatures[0]]
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            next = temperatures[i]

            if len(s) != 0:

                element = s.pop()
                while element[0] < next[0]:
                    result[element[1]] = next[1] - element[1]
                    if len(s) == 0:
                        break
                    element = s.pop()

                if element[0] >= next[0]:
                    s.append(element)

            s.append(next)

        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

    def test_b(self):
        self.assertEqual([1, 1, 1, 0], Solution().dailyTemperatures([30, 40, 50, 60]))

    def test_c(self):
        self.assertEqual([1, 1, 0], Solution().dailyTemperatures([30, 60, 90]))

    def test_d(self):
        self.assertEqual([8, 1, 5, 4, 3, 2, 1, 1, 0, 0],
                         Solution().dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
