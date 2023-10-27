import unittest
from typing import List, Dict


# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def mul(self, counts: Dict[int, int], n: int) -> int:
        result = 1
        for k, v in counts.items():
            if k == n:
                v -= 1
            result *= k ** v
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        counts = {}
        for i in range(n):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        for i in range(n):
            answer[i] = self.mul(counts, nums[i])
        return answer


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        solution = Solution()

        self.assertEqual([24, 12, 8, 6], solution.productExceptSelf([1, 2, 3, 4]))

    def test_b(self):
        solution = Solution()

        self.assertEqual([24, 0, 0, 0, 0], solution.productExceptSelf([0, 1, 2, 3, 4]))

    def test_c(self):
        solution = Solution()

        self.assertEqual(
            [-51438240, -28576800, -128595600, 28576800, 28576800, 36741600, 32148900, -36741600, 28576800, -25719120],
            solution.productExceptSelf([5, 9, 2, -9, -9, -7, -8, 7, -9, 10]))


if __name__ == "__main__":
    unittest.main()
