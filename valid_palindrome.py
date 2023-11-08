import unittest


# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""
        for i in range(len(s)):
            if s[i].isalnum():
                converted += s[i].lower()
        for i in range(len(converted) // 2):
            if converted[i] != converted[-(i + 1)]:
                return False
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    unittest.main()
