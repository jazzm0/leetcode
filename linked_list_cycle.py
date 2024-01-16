# https://leetcode.com/problems/linked-list-cycle

import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums: List[int], pos: int) -> Optional[ListNode]:
    head, ptr = None, None
    cycle = None
    for i in range(0, len(nums)):
        node = ListNode(nums[i], None)
        if i == pos:
            cycle = node

        if head is None:
            ptr = head = node

        ptr.next = node
        ptr = node
    ptr.next = cycle
    return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        addresses = set()
        while head is not None:
            if id(head) in addresses:
                return True
            addresses.add(id(head))
            head = head.next
        return False


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        linked = build_list([3, 2, 0, -4], 1)
        self.assertEqual(True, Solution().hasCycle(linked))

    def test_b(self):
        linked = build_list([3, 2, 0, -4], -1)
        self.assertEqual(False, Solution().hasCycle(linked))
