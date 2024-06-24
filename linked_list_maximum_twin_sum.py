# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

import unittest
from typing import Optional

from linked_list_utils import build_list, ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values, ptr, max_sum = [], head, 0
        while ptr:
            values.append(ptr.val)
            ptr = ptr.next

        for i in range(len(values) // 2):
            max_sum = max(max_sum, values[i] + values[-(i + 1)])
        return max_sum


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([5, 4, 2, 1])
        self.assertTrue(6, Solution().pairSum(l1))

    def test_b(self):
        l1 = build_list([4, 2, 2, 3])
        self.assertTrue(7, Solution().pairSum(l1))

    def test_c(self):
        l1 = build_list([1, 100000])
        self.assertTrue(100001, Solution().pairSum(l1))
