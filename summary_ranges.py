import unittest
from typing import List


# https://leetcode.com/problems/summary-ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return [str(nums[0])]

        longest, start, result = 1, 0, []
        while start < n:
            j = start
            while j < n - 1:
                if nums[j + 1] - nums[j] != 1:
                    break
                j += 1
            if start != j:
                result.append(f'{str(nums[start])}->{str(nums[j])}')
            else:
                result.append(f'{str(nums[start])}')
            start = j + 1

        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(["0->2", "4->5", "7"], Solution().summaryRanges([0, 1, 2, 4, 5, 7]))

    def test_b(self):
        self.assertEqual(["0", "2->4", "6", "8->9"], Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))


if __name__ == "__main__":
    unittest.main()
