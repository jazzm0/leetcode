# https://leetcode.com/problems/reverse-linked-list

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        ptr = head
        while ptr is not None:
            nodes.append(ptr)
            ptr = ptr.next
        if len(nodes) <= 1:
            return head

        ptr = head = nodes[-1]
        del nodes[-1]
        while len(nodes) != 0:
            ptr.next = nodes[-1]
            del nodes[-1]
            ptr = ptr.next

        ptr.next = None
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 3, 4, 7, 1, 2, 6])
        self.assertTrue(verify_list([6, 2, 1, 7, 4, 3, 1], Solution().reverseList(l1)))
