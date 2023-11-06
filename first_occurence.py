import unittest


# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(0, solution.strStr("sadbutsad", "sad"))

    def test_b(self):
        solution = Solution()

        self.assertEqual(-1, solution.strStr("leetcode", "leeto"))


if __name__ == "__main__":
    unittest.main()
