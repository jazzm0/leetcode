# https://leetcode.com/problems/reverse-linked-list-ii/

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left < 1:
            return head
        index = 1
        nodes = []
        start, end = None, None
        ptr = head
        while ptr is not None:
            if left <= index <= right:
                nodes.append(ptr)
            if index == left - 1:
                start = ptr
            elif index == right + 1:
                end = ptr
            ptr = ptr.next
            index += 1
        if start is not None:
            ptr = start
        else:
            head = ptr = nodes.pop()
        while len(nodes) != 0:
            ptr.next = nodes.pop()
            ptr = ptr.next
        ptr.next = end
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([1, 4, 3, 2, 5], Solution().reverseBetween(l1, 2, 4)))

    def test_b(self):
        l1 = build_list([5])
        self.assertTrue(verify_list([5], Solution().reverseBetween(l1, 1, 1)))

    def test_c(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([4, 3, 2, 1, 5], Solution().reverseBetween(l1, 1, 4)))

    def test_d(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([1, 5, 4, 3, 2], Solution().reverseBetween(l1, 2, 5)))

    def test_e(self):
        l1 = build_list([3, 5])
        self.assertTrue(verify_list([5, 3], Solution().reverseBetween(l1, 1, 2)))
