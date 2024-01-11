import unittest


# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 == 1:
            return False
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack) == 0 or c != brackets[stack.pop()]:
                    return False
        if len(stack) != 0:
            return False
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isValid("()"))

    def test_b(self):
        self.assertEqual(True, Solution().isValid("()[]{}"))

    def test_c(self):
        self.assertEqual(False, Solution().isValid("(]"))


if __name__ == "__main__":
    unittest.main()
