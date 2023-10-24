import unittest
from collections import Counter
from typing import List


# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        counts = Counter(nums)
        for k, v in counts.items():
            if v > majority_count:
                return k


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        a = [3, 2, 2, 3]

        self.assertEqual(3, solution.majorityElement([3, 2, 3]))


if __name__ == "__main__":
    unittest.main()
