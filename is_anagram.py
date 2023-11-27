import unittest


# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s, char_count_t = {}, {}
        for i in range(len(s)):
            char_count_s[s[i]] = char_count_s.get(s[i], 0) + 1
            char_count_t[t[i]] = char_count_t.get(t[i], 0) + 1

        for k, v in char_count_s.items():
            if k not in char_count_t or char_count_t[k] != v:
                return False
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isAnagram("anagram", "nagaram"))

    def test_b(self):
        self.assertEqual(False, Solution().isAnagram("rat", "car"))


if __name__ == "__main__":
    unittest.main()
