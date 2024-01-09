import sys
import unittest
from math import log

sys.set_int_max_str_digits(500000)


# https://leetcode.com/problems/factorial-trailing-zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        factorial = 1
        for i in range(n, 1, -1):
            factorial *= i
        factorial = str(factorial)
        count = 0
        for j in range(len(factorial)):
            if factorial[-(j + 1)] == "0":
                count += 1
            else:
                break
        return count

    def trailingZeroes2(self, n: int) -> int:
        if n < 5:
            return 0
        k = int(log(n, 5))
        count = 0
        for i in range(1, k + 1):
            count += n // (5 ** i)
        return count


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(0, Solution().trailingZeroes(3))

    def test_b(self):
        self.assertEqual(1, Solution().trailingZeroes(5))

    def test_c(self):
        self.assertEqual(9, Solution().trailingZeroes(43))

    def test_d(self):
        for i in range(5, 200):
            self.assertEqual(Solution().trailingZeroes(i), Solution().trailingZeroes2(i))


if __name__ == "__main__":
    unittest.main()
