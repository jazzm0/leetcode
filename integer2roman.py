import unittest


# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        specials = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        result = ""
        if num > 999:
            result = self.simplify(result, num, 1000, numerals, specials)
        if num > 99:
            result = self.simplify(result, num, 100, numerals, specials)

        result = self.simplify(result, num, 10, numerals, specials)

        return result

    def simplify(self, s: str, number: int, modulo: int, numerals: {}, specials: {}) -> str:
        mod = number % modulo
        if mod in specials:
            return s + specials[mod]
        if mod in numerals:
            return s + numerals[mod]
        if modulo == 1000:
            r = 
        if mod < 5:
            s += numerals[1] * mod
        elif mod > 5 and modulo == 10:
            s += numerals[5]
            s += numerals[1] * (mod - 5)
        return s


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual("IV", solution.intToRoman(4))

    def test_a1(self):
        solution = Solution()

        self.assertEqual("III", solution.intToRoman(3))

    def test_a2(self):
        solution = Solution()

        self.assertEqual("VII", solution.intToRoman(7))

    def test_b(self):
        solution = Solution()

        self.assertEqual("CD", solution.intToRoman(400))


if __name__ == "__main__":
    unittest.main()
