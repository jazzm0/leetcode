import unittest
from typing import List


# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        lcp = ""
        for i in range(len(first)):
            for j in range(1, len(strs)):
                second = strs[j]
                if len(second) <= i or second[i] != first[i]:
                    return lcp
            lcp += first[i]
        return lcp


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual("fl", solution.longestCommonPrefix(["flower", "flow", "flight"]))

    def test_c(self):
        solution = Solution()

        self.assertEqual("a", solution.longestCommonPrefix(["ab", "a"]))


if __name__ == "__main__":
    unittest.main()
