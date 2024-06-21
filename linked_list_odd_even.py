# https://leetcode.com/problems/odd-even-linked-list/

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        ptr = head
        even_ptr = even_head = head.next
        while ptr.next and even_ptr.next:
            ptr.next = even_ptr.next
            if even_ptr.next.next:
                even_ptr.next = even_ptr.next.next
                even_ptr = even_ptr.next
            else:
                even_ptr.next = None
            ptr = ptr.next

        ptr.next = even_head
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
