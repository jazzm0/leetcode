import unittest
from typing import Dict, Set


# https://leetcode.com/problems/minimum-window-substring

class Solution:

    def reduce(self, s: str, start: int, end: int, surplus: Dict, keys: Set) -> int:
        while start < end:
            if s[start] in surplus:
                surplus[s[start]] -= 1
                if surplus[s[start]] == 0:
                    del surplus[s[start]]
            elif s[start] in keys:
                break
            start += 1
        return start

    def minWindow(self, s: str, t: str) -> str:
        min_substring = ""
        needed = {}
        len_s, len_t = len(s), len(t)

        if len_t > len_s:
            return min_substring

        for i in range(len(t)):
            needed[t[i]] = needed.get(t[i], 0) + 1

        start, end = 0, 0
        surplus, keys = {}, set(needed.keys())

        while end < len_s:
            if len(needed) > 0:
                if s[end] in needed:
                    needed[s[end]] -= 1
                    if needed[s[end]] == 0:
                        del needed[s[end]]
                elif s[end] in keys:
                    surplus[s[end]] = surplus.get(s[end], 0) + 1
            end += 1
            if len(needed) == 0:
                break

        if len(needed) == 0:
            while start < len_s:

                start = self.reduce(s, start, end, surplus, keys)

                if len(s[start:end]) < len(min_substring) or len(min_substring) == 0:
                    min_substring = s[start:end]
                    if len_t == len(min_substring):
                        return min_substring

                found = False
                while end < len_s and not found:
                    if s[end] in keys:
                        if s[start] == s[end]:
                            found = True
                            start += 1
                        else:
                            surplus[s[end]] = surplus.get(s[end], 0) + 1
                    end += 1

                if not found and len(min_substring) <= len(s[start:end]):
                    return min_substring
            else:
                return min_substring

        return min_substring


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("BANC", Solution().minWindow("ADOBECODEBANC", "ABC"))

    def test_b(self):
        self.assertEqual("a", Solution().minWindow("a", "a"))

    def test_c(self):
        self.assertEqual("ba", Solution().minWindow("bba", "ab"))

    def test_d(self):
        self.assertEqual("", Solution().minWindow("a", "b"))

    def test_e(self):
        self.assertEqual("a", Solution().minWindow("ab", "a"))

    def test_f(self):
        self.assertEqual("baa", Solution().minWindow("bbaac", "aba"))

    def test_g(self):
        self.assertEqual("cwae", Solution().minWindow("cabwefgewcwaefgcf", "cae"))

    def test_h(self):
        self.assertEqual("cabd", Solution().minWindow("abcabdebac", "cda"))


if __name__ == "__main__":
    unittest.main()
