# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums: List[int]) -> Optional[ListNode]:
    head = ListNode(nums[0], None)
    ptr = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i], None)
        ptr.next = node
        ptr = node
    return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        seen = set()
        while h is not None:
            if h.next is not None and h.val == h.next.val:
                seen.add(h.val)
                h.next = h.next.next
            else:
                h = h.next
        h = head
        previous = None
        while h is not None:
            if h.val in seen:
                if previous is None:
                    head = h.next
                else:
                    if h.next is not None:
                        previous.next = h.next
                    else:
                        previous.next = None
            else:
                previous = h
            h = h.next

        return head


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        linked = build_list([1, 1, 1, 2, 3])
        self.assertEqual(2, Solution().deleteDuplicates(linked).val)
