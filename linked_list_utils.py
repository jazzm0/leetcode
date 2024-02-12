from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def verify_list(nums: List[int], head: Optional[ListNode]) -> bool:
    i = 0
    while head is not None:
        if head.val != nums[i]:
            return False
        i += 1
        head = head.next
    if i < len(nums):
        return False
    return True


def build_list_with_cycle(nums: List[int], pos: int) -> Optional[ListNode]:
    head, ptr = None, None
    cycle = None
    for i in range(0, len(nums)):
        node = ListNode(nums[i], None)
        if i == pos:
            cycle = node

        if head is None:
            head = node
        else:
            ptr.next = node
        ptr = node
    ptr.next = cycle
    return head


def build_list(nums: List[int]) -> Optional[ListNode]:
    head, ptr = None, None
    for i in range(0, len(nums)):
        node = ListNode(nums[i], None)

        if head is None:
            head = node
        else:
            ptr.next = node
        ptr = node
    return head
