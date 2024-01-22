# https://leetcode.com/problems/copy-list-with-random-pointer
import unittest
from typing import Optional, List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def build_list(self, nums: List[tuple]) -> Optional[Node]:
        node_addresses, head, ptr = [], None, None
        for i in range(0, len(nums)):
            node = Node(nums[i][0], None)
            node_addresses.append(node)
            if head is None:
                ptr = head = node
            else:
                ptr.next = node
            ptr = node
        index = 0
        ptr = head
        while ptr is not None:
            if nums[index][1] is not None:
                ptr.random = node_addresses[nums[index][1]]
            ptr = ptr.next
            index += 1

        return head

    def copyRandomList(self, head: 'Optional[Node]') -> Optional[Node]:
        ptr = head
        nums = []
        addresses = {}
        index = 0
        while ptr is not None:
            addresses[id(ptr)] = index
            ptr = ptr.next
            index += 1

        ptr = head
        while ptr is not None:
            if id(ptr.random) in addresses:
                nums.append((ptr.val, addresses[id(ptr.random)]))
            else:
                nums.append((ptr.val, None))
            ptr = ptr.next

        return self.build_list(nums)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        l1 = solution.build_list([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
        self.assertEquals(7, Solution().copyRandomList(l1).val)

    def test_b(self):
        solution = Solution()
        l1 = solution.build_list([(-1, None)])
        self.assertEquals(-1, Solution().copyRandomList(l1).val)
