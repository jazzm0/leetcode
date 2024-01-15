# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import unittest
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                operand_one = stack.pop()
                operand_two = stack.pop()
                result = None
                if tokens[i] == "+":
                    result = operand_two + operand_one
                elif tokens[i] == "-":
                    result = operand_two - operand_one
                elif tokens[i] == "*":
                    result = operand_two * operand_one
                elif tokens[i] == "/":
                    if operand_one < 0 and operand_two < 0:
                        result = -operand_two // -operand_one
                    elif operand_one < 0:
                        result = -(operand_two // -operand_one)
                    elif operand_two < 0:
                        result = -(-operand_two // operand_one)
                    else:
                        result = operand_two // operand_one
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(9, Solution().evalRPN(["2", "1", "+", "3", "*"]))

    def test_b(self):
        self.assertEqual(6, Solution().evalRPN(["4", "13", "5", "/", "+"]))

    def test_c(self):
        self.assertEqual(22, Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
