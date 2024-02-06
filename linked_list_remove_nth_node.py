# https://leetcode.com/problems/remove-nth-node-from-end-of-list

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        ptr = head
        while ptr is not None:
            nodes.append(ptr)
            ptr = ptr.next
        target = nodes[-n]
        ptr = head
        while ptr is not None:
            if target == head:
                head = head.next
                break
            if ptr.next == target:
                ptr.next = target.next
                break
            ptr = ptr.next
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([1, 2, 3, 5], Solution().removeNthFromEnd(l1, 2)))

    def test_b(self):
        l1 = build_list([1, 2])
        self.assertTrue(verify_list([1], Solution().removeNthFromEnd(l1, 1)))

    def test_c(self):
        l1 = build_list([1])
        self.assertTrue(verify_list([], Solution().removeNthFromEnd(l1, 1)))
