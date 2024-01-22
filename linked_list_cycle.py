# https://leetcode.com/problems/linked-list-cycle

import unittest
from typing import Optional

from linked_list_sum import ListNode
from linked_list_utils import build_list_with_cycle


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        addresses = set()
        while head is not None:
            if id(head) in addresses:
                return True
            addresses.add(id(head))
            head = head.next
        return False


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        linked = build_list_with_cycle([3, 2, 0, -4], 1)
        self.assertEqual(True, Solution().hasCycle(linked))

    def test_b(self):
        linked = build_list_with_cycle([3, 2, 0, -4], -1)
        self.assertEqual(False, Solution().hasCycle(linked))
