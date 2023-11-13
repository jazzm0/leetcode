import unittest


# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, start, end = 0, 0, 0
        contained_chars = set()
        while end < len(s):
            if s[end] not in contained_chars:
                contained_chars.add(s[end])
                end += 1
            else:
                contained_chars.remove(s[start])
                start += 1
            max_len = max(max_len, len(contained_chars))
        return max_len


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcabcbb"))

    def test_b(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("bbbbbbbbb"))

    def test_c(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("pwwkew"))

    def test_d(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("dvdf"))


if __name__ == "__main__":
    unittest.main()
