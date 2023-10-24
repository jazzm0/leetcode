import unittest
from typing import List


# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0

        for k in range(n):
            nums1.pop()

        while i < m + n:
            if (i < len(nums1) and j < n and nums1[i] >= nums2[j]) or i > m + j - 1:
                nums1.insert(i, nums2[j])
                j += 1
            else:
                i += 1


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        a = [1, 4, 4, 5, 0, 0, 0, 0]
        b = [1, 2, 5, 6]
        solution.merge(a, 4, b, 4)
        self.assertEqual(a, [1, 1, 2, 4, 4, 5, 5, 6])

    def test_b(self):
        solution = Solution()
        a = [1, 2, 3, 0, 0, 0]
        b = [2, 5, 6]
        solution.merge(a, 3, b, 3)
        self.assertEqual(a, [1, 2, 2, 3, 5, 6])

    def test_c(self):
        solution = Solution()
        a = [0]
        b = [1]
        solution.merge(a, 0, b, 1)
        self.assertEqual(a, [1])

    def test_d(self):
        solution = Solution()
        a = []
        b = [1]
        solution.merge(a, 0, b, 1)
        self.assertEqual(a, [1])

    def test_e(self):
        solution = Solution()
        a = [4, 0, 0, 0, 0, 0]
        b = [1, 2, 3, 5, 6]
        solution.merge(a, 1, b, 5)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
