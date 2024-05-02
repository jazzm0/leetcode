# https://leetcode.com/problems/merge-strings-alternately

import unittest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        result = []
        min_len = min(m, n)
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        result = ''.join(result)
        if n > m:
            return result + word2[m:]
        elif n < m:
            return result + word1[n:]
        else:
            return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("apbqcr", Solution().mergeAlternately("abc", "pqr"))

    def test_b(self):
        self.assertEqual("apbqrs", Solution().mergeAlternately("ab", "pqrs"))

    def test_c(self):
        self.assertEqual("apbqcd", Solution().mergeAlternately("abcd", "pq"))
