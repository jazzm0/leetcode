# https://leetcode.com/problems/add-two-numbers

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, ptr = None, None
        addition = 0

        while l1 is not None or l2 is not None:

            if l1 is not None and l2 is not None:
                addition = l1.val + l2.val + addition
            elif l1 is not None:
                addition = l1.val + addition
            elif l2 is not None:
                addition = l2.val + addition

            if addition >= 10:
                node = ListNode(addition - 10, None)
                addition = 1
            else:
                node = ListNode(addition, None)
                addition = 0
            if result is None:
                ptr = result = node
            else:
                ptr.next = node
                ptr = node

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if addition == 1:
            node = ListNode(addition, None)
            ptr.next = node

        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])
        self.assertTrue(verify_list([7, 0, 8], Solution().addTwoNumbers(l1, l2)))

    def test_b(self):
        l1 = build_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_list([9, 9, 9, 9])
        self.assertTrue(verify_list([8, 9, 9, 9, 0, 0, 0, 1], Solution().addTwoNumbers(l1, l2)))
