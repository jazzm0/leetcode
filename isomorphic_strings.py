import unittest


# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        mapped_chars = {}
        is_mapped = set()
        for i in range(n):
            if s[i] not in mapped_chars:
                if t[i] in is_mapped:
                    return False
                mapped_chars[s[i]] = t[i]
                is_mapped.add(t[i])
            elif mapped_chars[s[i]] != t[i]:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isIsomorphic("a", "b"))

    def test_b(self):
        self.assertEqual(False, Solution().isIsomorphic("aa", "ab"))

    def test_c(self):
        self.assertEqual(False, Solution().isIsomorphic("aa", "aab"))

    def test_d(self):
        self.assertEqual(True, Solution().isIsomorphic("paper", "title"))

    def test_e(self):
        self.assertEqual(False, Solution().isIsomorphic("bbbaaaba", "aaabbbba"))

    def test_f(self):
        self.assertEqual(False, Solution().isIsomorphic("badc", "baba"))


if __name__ == "__main__":
    unittest.main()
