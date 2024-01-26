# https://leetcode.com/problems/merge-two-sorted-lists

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        actual, head, ptr = None, None, None
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val > l2.val:
                    ptr = l2
                    l2 = l2.next
                else:
                    ptr = l1
                    l1 = l1.next
            elif l1 is not None:
                ptr = l1
                l1 = l1.next
            elif l2 is not None:
                ptr = l2
                l2 = l2.next
            if head is None:
                head = actual = ptr
            else:
                actual.next = ptr
                actual = actual.next
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 2, 4])
        l2 = build_list([1, 3, 4])
        self.assertTrue(verify_list([1, 1, 2, 3, 4, 4], Solution().mergeTwoLists(l1, l2)))
