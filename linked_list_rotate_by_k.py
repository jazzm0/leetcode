# https://leetcode.com/problems/rotate-list/

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        nodes = []
        ptr = head
        while ptr is not None:
            nodes.append(ptr)
            ptr = ptr.next
        if len(nodes) <= 1:
            return head
        k %= len(nodes)
        ptr = head
        head = nodes[-k]
        nodes[-1].next = ptr
        nodes[-(k + 1)].next = None
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([4, 5, 1, 2, 3], Solution().rotateRight(l1, 2)))

    def test_b(self):
        l1 = build_list([0, 1, 2])
        self.assertTrue(verify_list([2, 0, 1], Solution().rotateRight(l1, 4)))

    def test_c(self):
        l1 = build_list([1])
        self.assertTrue(verify_list([1], Solution().rotateRight(l1, 1)))
