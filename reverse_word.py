import unittest


# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip().split(" ")
        result = ""
        for i in range(len(s) - 1, -1, -1):
            if len(s[i]) > 0:
                result += s[i] + " "
        return result[0: len(result) - 1]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual("blue is sky the", solution.reverseWords("the sky is blue"))

    def test_b(self):
        solution = Solution()

        self.assertEqual("world hello", solution.reverseWords("  hello world  "))

    def test_c(self):
        solution = Solution()

        self.assertEqual("example good a", solution.reverseWords("a good   example"))


if __name__ == "__main__":
    unittest.main()
