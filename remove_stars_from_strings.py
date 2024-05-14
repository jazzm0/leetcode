# https://leetcode.com/problems/removing-stars-from-a-string
import unittest


class Solution:
    # def removeStars(self, s: str) -> str:
    #     chars = list(s)
    #     i = 0
    #     while chars:
    #         if chars[i] == "*":
    #             del chars[i - 1]
    #             del chars[i - 1]
    #             i -= 1
    #         else:
    #             i += 1
    #         if i == len(chars):
    #             break
    #     return ''.join(chars)
    class Solution:
        def removeStars(self, s: str) -> str:
            i = 0
            while s:
                if i < len(s) - 1:
                    if s[i + 1] == "*":
                        s = s[0:i] + s[i + 2:]
                        i -= 1
                    else:
                        i += 1
                else:
                    break
            return s


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("lecoe", Solution().removeStars("leet**cod*e"))

    def test_b(self):
        self.assertEqual("", Solution().removeStars("erase*****"))
