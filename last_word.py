import unittest


# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")
        return len(s[len(s) - 1])


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        solution = Solution()

        self.assertEqual(4, solution.lengthOfLastWord("   fly me   to   the moon  "))
        self.assertEqual(5, solution.lengthOfLastWord("Hello World"))


if __name__ == "__main__":
    unittest.main()
