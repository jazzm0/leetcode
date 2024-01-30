# https://leetcode.com/problems/reverse-nodes-in-k-group

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        group = []
        first, end, ptr = head, None, head
        index = 0
        while ptr is not None or len(group) == k:
            if index % k == 0 and index != 0:
                ptr = first
                while len(group) != 0:
                    if first == head:
                        ptr = head = group.pop()
                        continue
                    ptr.next = group.pop()
                    ptr = ptr.next
                first = ptr
                ptr.next = end
                index = 0
            else:
                group.append(ptr)
                index += 1
            end = ptr = ptr.next
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([2, 1, 4, 3, 5], Solution().reverseKGroup(l1, 2)))

    def test_b(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([3, 2, 1, 4, 5], Solution().reverseKGroup(l1, 3)))

    def test_c(self):
        l1 = build_list([1, 2, 3, 4, 5])
        self.assertTrue(verify_list([1, 2, 3, 4, 5], Solution().reverseKGroup(l1, 1)))

    def test_d(self):
        l1 = build_list([1, 2])
        self.assertTrue(verify_list([2, 1], Solution().reverseKGroup(l1, 2)))
