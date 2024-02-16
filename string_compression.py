# https://leetcode.com/problems/string-compression

import unittest
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            actual = chars[i]
            count = 0
            while i < len(chars) and actual == chars[i]:
                del chars[i]
                count += 1
            if count == 1:
                chars.insert(i, actual)
            else:
                chars.insert(i, actual)
                count = str(count)
                for j in range(len(count)):
                    chars.insert(i + 1, count[j])
                    i += 1
            i += 1
        return len(''.join(chars))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(6, Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))

    def test_b(self):
        self.assertEqual(4, Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
