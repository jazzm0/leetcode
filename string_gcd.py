# https://leetcode.com/problems/greatest-common-divisor-of-strings

import unittest


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_str(str1: str, str2: str) -> str:
    gcd_length = gcd(len(str1), len(str2))
    candidate = str1[:gcd_length]
    if str1[:gcd_length] * (len(str2) // gcd_length) == str2 and str1[:gcd_length] * (len(str1) // gcd_length) == str1:
        return candidate
    return ""


class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            return gcd_str(str1, str2)
        elif len(str1) > len(str2):
            return gcd_str(str2, str1)
        else:
            if str1 != str2:
                return ""
            return str1


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("ABC", Solution().gcdOfStrings("ABCABC", "ABC"))

    def test_b(self):
        self.assertEqual("AB", Solution().gcdOfStrings("ABABAB", "ABAB"))

    def test_c(self):
        self.assertEqual("", Solution().gcdOfStrings("LEET", "CODE"))

    def test_d(self):
        self.assertEqual(21, gcd(252, 105))