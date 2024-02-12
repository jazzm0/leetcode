# https://leetcode.com/problems/merge-strings-alternately

import unittest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1, len_w2 = len(word1), len(word2)
        total_length = max(len_w1, len_w2)
        result = ""
        for i in range(total_length):
            if i < len_w1:
                result += word1[i]
            if i < len_w2:
                result += word2[i]
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("apbqcr", Solution().mergeAlternately("abc", "pqr"))
