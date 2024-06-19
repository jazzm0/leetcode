import heapq
import unittest
from typing import List


# https://leetcode.com/problems/maximum-subsequence-score

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combination = sorted([x for x in zip(nums2, nums1)], reverse=True)

        heap, s, answer = [], 0, 0

        for num2, num1 in combination:
            heapq.heappush(heap, num1)
            s += num1
            if len(heap) > k:
                s -= heapq.heappop(heap)
            if len(heap) == k:
                answer = max(answer, s * num2)

        return answer


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(12, Solution().maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))

    def test_b(self):
        self.assertEqual(30, Solution().maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))

    def test_c(self):
        self.assertEqual(168, Solution().maxScore([2, 1, 14, 12], [11, 7, 13, 6], 3))
