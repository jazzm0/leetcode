import unittest


# https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                part = []
                while stack and stack[-1] != "[":
                    part.insert(0, stack.pop())
                stack.pop()
                times = []
                while stack and stack[-1].isdigit():
                    times.insert(0, stack.pop())
                times = int(''.join(times))
                part = ''.join(part) * times
                if stack:
                    if stack[-1] != "[":
                        stack.append(stack.pop() + part)
                    else:
                        stack.append(part)
                else:
                    result.append(part)
        return ''.join(result) + ''.join(stack)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("aaabcbc", Solution().decodeString("3[a]2[bc]"))

    def test_b(self):
        self.assertEqual("accaccacc", Solution().decodeString("3[a2[c]]"))

    def test_c(self):
        self.assertEqual("abcabccdcdcdef", Solution().decodeString("2[abc]3[cd]ef"))

    def test_d(self):
        self.assertEqual("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",
                         Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
