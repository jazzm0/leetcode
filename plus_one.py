import unittest
from typing import List


# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = True
        while i >= 0:
            if (digits[i] == 9 and carry) or digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i - 1] += 1
                carry = False
            else:
                if carry:
                    digits[i] += 1
                break
            i -= 1
        return digits


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([1, 2, 4], Solution().plusOne([1, 2, 3]))

    def test_b(self):
        self.assertEqual([1, 0, 0, 0], Solution().plusOne([9, 9, 9]))

    def test_c(self):
        self.assertEqual([9, 0, 0], Solution().plusOne([8, 9, 9]))


if __name__ == "__main__":
    unittest.main()
