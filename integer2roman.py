import unittest


# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        specials = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

        thousands = (num // 1000)
        result = thousands * numerals[1000]
        num -= thousands * 1000

        hundreds = num // 100
        whole_hundreds = hundreds * 100
        result = self.count(hundreds, whole_hundreds, 500, 100, result, numerals, specials)
        num -= whole_hundreds

        tens = num // 10
        whole_tens = tens * 10
        result = self.count(tens, whole_tens, 50, 10, result, numerals, specials)
        num -= whole_tens

        result = self.count(num, num, 5, 1, result, numerals, specials)

        return result

    def count(self, count: int, whole: int, high_key: int, low_key: int, result: str, numerals: {},
              specials: {}) -> str:
        if whole in specials:
            result += specials[whole]
        elif count >= 5:
            result += numerals[high_key] + (count - 5) * numerals[low_key]
        else:
            result += count * numerals[low_key]
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual("MMM", solution.intToRoman(3000))

    def test_b(self):
        solution = Solution()

        self.assertEqual("MMMCM", solution.intToRoman(3900))

    def test_c(self):
        solution = Solution()

        self.assertEqual("MMMDCC", solution.intToRoman(3700))

    def test_d(self):
        solution = Solution()

        self.assertEqual("MMMCCC", solution.intToRoman(3300))

    def test_e(self):
        solution = Solution()

        self.assertEqual("MMMCCCLXX", solution.intToRoman(3370))

    def test_f(self):
        solution = Solution()

        self.assertEqual("IX", solution.intToRoman(9))


if __name__ == "__main__":
    unittest.main()
