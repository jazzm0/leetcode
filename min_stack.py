# https://leetcode.com/problems/min-stack
import unittest


class MinStack:
    data = []

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        if len(self.data) > 0:
            self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        stack = MinStack()
        stack.push(-1)
        self.assertEqual(-1, stack.top())
        self.assertEqual(-1, stack.getMin())
