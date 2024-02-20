# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

import unittest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        if count == k:
            return count
        actual = count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                actual -= 1
            if s[i] in vowels:
                actual += 1
            count = max(count, actual)
            if count == k:
                return count
        return count


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(3, Solution().maxVowels("abciiidef", 3))

    def test_b(self):
        self.assertEqual(2, Solution().maxVowels("aeiou", 2))

    def test_c(self):
        self.assertEqual(2, Solution().maxVowels("leetcode", 3))
