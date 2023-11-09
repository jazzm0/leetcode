import unittest
from typing import List


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        positions = {}
        for i in range(len(numbers)):
            needed = target - numbers[i]

            if needed in positions:
                return [positions[needed], i + 1]

            positions[numbers[i]] = i + 1


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([1, 2], Solution().twoSum([2, 7, 11, 15], 9))

    def test_b(self):
        self.assertEqual([1, 3], Solution().twoSum([2, 3, 4], 6))

    def test_c(self):
        self.assertEqual([1, 2], Solution().twoSum([0, 0, 3, 4], 0))


if __name__ == "__main__":
    unittest.main()
