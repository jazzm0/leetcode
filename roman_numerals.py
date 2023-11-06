import unittest
from collections import Counter


# https://leetcode.com/problems/roman-to-integer

class Solution:

    def simplify(self, s: str, pattern: str, value: int, new_value: int) -> (str, int):
        if s.find(pattern) >= 0:
            return s.replace(pattern, ""), value + new_value
        return s, value

    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        specials = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        result = 0
        for k, v in specials.items():
            s, result = self.simplify(s, k, result, v)

        counts = Counter(s)
        for k, v in counts.items():
            result += numerals[k] * v
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual(3, solution.romanToInt("III"))

    def test_b(self):
        solution = Solution()

        self.assertEqual(58, solution.romanToInt("LVIII"))

    def test_c(self):
        solution = Solution()

        self.assertEqual(1994, solution.romanToInt("MCMXCIV"))

    def test_d(self):
        solution = Solution()

        self.assertEqual(4, solution.romanToInt("IV"))


if __name__ == "__main__":
    unittest.main()
