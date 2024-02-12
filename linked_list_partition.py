# https://leetcode.com/problems/rotate-list/

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ptr, n_head, n_ptr, last = head, None, None, head
        while ptr is not None:
            last = ptr
            tmp = None
            if ptr.next is not None:
                tmp = ptr.next.next
            if head.val >= x:
                tmp = head.next
                if n_head is None:
                    n_head = n_ptr = head
                    n_head.next = None
                else:
                    n_ptr.next = head
                    n_ptr = n_ptr.next
                    n_ptr.next = None
                head = ptr = tmp
            elif ptr.next is not None and ptr.next.val >= x:

                if n_head is None:
                    n_head = n_ptr = ptr.next
                    n_head.next = None
                else:
                    n_ptr.next = ptr.next
                    n_ptr = n_ptr.next
                    n_ptr.next = None
                ptr.next = tmp
            else:
                ptr = ptr.next
        if head is None:
            return n_head
        last.next = n_head
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 4, 3, 2, 5, 2])
        self.assertTrue(verify_list([1, 2, 2, 4, 3, 5], Solution().partition(l1, 3)))

    def test_b(self):
        l1 = build_list([2, 1])
        self.assertTrue(verify_list([1, 2], Solution().partition(l1, 2)))

    def test_c(self):
        l1 = build_list([1, 2])
        self.assertTrue(verify_list([1, 2], Solution().partition(l1, 0)))

    def test_d(self):
        l1 = build_list([1, 4, 3, 2, 5, 2])
        self.assertTrue(verify_list([1, 2, 2, 4, 3, 5], Solution().partition(l1, 3)))
