# https://leetcode.com/problems/reverse-vowels-of-a-string

import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowels_s = []
        positions = set()
        result = ""
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vowels_s.append(s[i])
                positions.add(i)
        for i in range(len(s)):
            if i in positions:
                result += vowels_s.pop()
            else:
                result += s[i]
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("holle", Solution().reverseVowels("hello"))

    def test_b(self):
        self.assertEqual("leotcede", Solution().reverseVowels("leetcode"))
