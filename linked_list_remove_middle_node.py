# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

import unittest
from typing import Optional

from linked_list_utils import build_list, verify_list, ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_count = 0
        ptr = head
        while ptr is not None:
            node_count += 1
            ptr = ptr.next

        if node_count == 1:
            return None

        target, count = node_count // 2, 0
        ptr = head
        while ptr is not None:
            if count == target - 1:
                ptr.next = ptr.next.next
                break
            count += 1
            ptr = ptr.next
        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        l1 = build_list([1, 3, 4, 7, 1, 2, 6])
        self.assertTrue(verify_list([1, 3, 4, 1, 2, 6], Solution().deleteMiddle(l1)))

    def test_b(self):
        l1 = build_list([1])
        self.assertTrue(verify_list([], Solution().deleteMiddle(l1)))
