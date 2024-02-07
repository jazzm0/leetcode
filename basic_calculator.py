# https://leetcode.com/problems/basic-calculator

import unittest


class Solution:
    def scan_number(self, s: str, start: int) -> (int, int):
        number = ""
        i = start
        while i < len(s):
            if s[i].isdigit():
                number += s[i]
                i += 1
            else:
                break
        if len(number) > 0:
            return int(number), i
        raise Exception

    def calculate_simple(self, s: str) -> int:
        result = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "+":
                stack.append("+")
                i += 1
            elif s[i] == "-":
                string_number, i = self.scan_number(s, i + 1)
                if len(stack) > 0:
                    stack.append("+")
                stack.append(-string_number)
            elif s[i].isdigit():
                string_number, i = self.scan_number(s, i)
                stack.append(string_number)

        while len(stack) != 1:
            operand_one = stack.pop()
            operator = stack.pop()
            operand_two = stack.pop()
            if operator == "+":
                result += operand_one + operand_two
            elif operator == "-":
                result += operand_two - operand_one
            stack.append(result)
            result = 0

        return stack.pop()

    def calculate(self, s: str) -> int:
        s = s.strip().replace(" ", "")

        return 0


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(2, Solution().calculate_simple("1+1"))

    def test_b(self):
        self.assertEqual(3, Solution().calculate_simple("2-1+2"))

    def test_c(self):
        self.assertEqual(23, Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

    def test_d(self):
        self.assertEqual(11, Solution().calculate_simple("10+1"))

    def test_e(self):
        self.assertEqual(0, Solution().calculate_simple("1+2+3+4+5-55+6+7+8+9+10"))

    def test_f(self):
        self.assertEqual(1, Solution().calculate_simple("2-1+2-1-1"))

    def test_g(self):
        self.assertEqual(-8, Solution().calculate_simple("-1-1-1-5"))
