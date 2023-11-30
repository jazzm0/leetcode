import unittest


# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = set()
        seen.add(n)
        while True:
            digits = str(n)
            sum = 0
            for d in digits:
                sum += int(d) ** 2
            n = sum
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isHappy(19))


if __name__ == "__main__":
    unittest.main()
