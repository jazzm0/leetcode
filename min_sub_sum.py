import unittest
from typing import List


# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        actual_sum, start, end, min_len = 0, 0, 0, len(nums)

        while actual_sum < target and end < len(nums):
            actual_sum += nums[end]
            end += 1

        if actual_sum < target:
            return 0

        while end < len(nums) or actual_sum > target:
            while start < end:
                min_len = min(min_len, end - start)
                if min_len == 1:
                    return 1

                if actual_sum - nums[start] >= target:
                    actual_sum -= nums[start]
                    start += 1
                elif end < len(nums):
                    actual_sum += nums[end]
                    end += 1
                else:
                    return min_len

        return min_len


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(2, Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

    def test_b(self):
        self.assertEqual(1, Solution().minSubArrayLen(4, [1, 4, 4]))

    def test_c(self):
        self.assertEqual(0, Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))

    def test_d(self):
        self.assertEqual(3, Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))


if __name__ == "__main__":
    unittest.main()
