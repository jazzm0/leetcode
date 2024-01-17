# https://leetcode.com/problems/add-two-numbers

import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums: List[int]) -> Optional[ListNode]:
    head, ptr = None, None
    for i in range(0, len(nums)):
        node = ListNode(nums[i], None)
        if head is None:
            ptr = head = node
        ptr.next = node
        ptr = node
    return head


def verify_list(nums: List[int], head: Optional[ListNode]) -> bool:
    i = 0
    while head is not None:
        if head.val != nums[i]:
            return False
        i += 1
        head = head.next
    return True


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
