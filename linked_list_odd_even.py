# https://leetcode.com/problems/odd-even-linked-list/

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        ptr = last_odd = head
        even_ptr = last_even = even_head = head.next
        while ptr is not None:
            if ptr.next and ptr.next.next:
                last_odd = ptr.next = ptr.next.next
            ptr = ptr.next
            if even_ptr:
                if even_ptr.next and even_ptr.next.next:
                    last_even = even_ptr.next = even_ptr.next.next
                even_ptr = even_ptr.next

        last_odd.next = even_head
        if last_even:
            last_even.next = None
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([1, 3, 5, 2, 4], Solution().oddEvenList(l1)))

    def test_b(self):
        l1 = build_list([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(verify_list([1, 3, 5, 7, 2, 4, 6, 8], Solution().oddEvenList(l1)))

    def test_c(self):
        l1 = build_list([1])
        self.assertTrue(verify_list([1], Solution().oddEvenList(l1)))
