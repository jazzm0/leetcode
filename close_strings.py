# https://leetcode.com/problems/determine-if-two-strings-are-close
import unittest
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        chars_word1 = Counter(word1)
        chars_word2 = Counter(word2)
        if (len(chars_word1) != len(chars_word2) or chars_word2.keys() != chars_word1.keys() or
                sorted(list(chars_word1.values())) != sorted(list(chars_word2.values()))):
            return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().closeStrings("abc", "bca"))

    def test_b(self):
        self.assertEqual(True, Solution().closeStrings("cababa", "abbccc"))

    def test_c(self):
        self.assertEqual(False, Solution().closeStrings("abbzzca", "babzzcz"))
