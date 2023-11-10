import unittest


# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isPalindrome(121))

    def test_b(self):
        self.assertEqual(False, Solution().isPalindrome(1211))


if __name__ == "__main__":
    unittest.main()
