# https://leetcode.com/problems/greatest-common-divisor-of-strings

import unittest


class Solution:
    
    def is_divisor(self, s: str, d: str) -> bool:
        if len(d) > 0 and len(s) % len(d) != 0:
            return False
        count = len(s) // len(d)
        if d * count == s:
            return True
        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        length = min(len(str1), len(str2))
        for i in range(1, length + 1):
            if self.is_divisor(str1, str1[:i]) and self.is_divisor(str2, str1[:i]):
                gcd = str1[:i]
        return gcd


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("ABC", Solution().gcdOfStrings("ABCABC", "ABC"))

    def test_b(self):
        self.assertEqual("AB", Solution().gcdOfStrings("ABABAB", "ABAB"))

    def test_c(self):
        self.assertEqual("", Solution().gcdOfStrings("LEET", "CODE"))

    def test_d(self):
        self.assertEqual(True, Solution().is_divisor("ABAB", "AB"))

    def test_e(self):
        self.assertEqual(False, Solution().is_divisor("ABAB", "A"))
