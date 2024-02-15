# https://leetcode.com/problems/can-place-flowers/

import unittest
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False

        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if ((i == 0 and flowerbed[i + 1] == 0) or
                        (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0) or
                        (len(flowerbed) - 1 > i > 0 == flowerbed[i + 1] and flowerbed[i - 1] == 0)):
                    flowerbed[i] = 1
                    count += 1
        return count >= n


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))

    def test_b(self):
        self.assertEqual(False, Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_c(self):
        self.assertEqual(False, Solution().canPlaceFlowers([1, 0], 1))
