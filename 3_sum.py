import unittest
from typing import List


# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_results = set()
        nums = sorted(nums)
        positions = {}
        for i in range(len(nums)):
            indexes = positions.get(nums[i], list())
            if len(indexes) < 2:
                indexes.append(i)
                positions[nums[i]] = indexes

        if len(positions) == 1 and 0 in positions:
            return [[0, 0, 0]]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in positions:
                    indexes = positions[-(nums[i] + nums[j])]
                    for target in indexes:
                        if target != i and target != j:
                            s = sorted([nums[i], nums[j], nums[target]])
                            unique_results.add((s[0], s[1], s[2]))
        results = []
        for r in unique_results:
            results.insert(0, [r[0], r[1], r[2]])
        return results


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    unittest.main()
