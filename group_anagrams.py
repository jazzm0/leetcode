import unittest
from typing import List


# https://leetcode.com/problems/group-anagrams

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            group = groups.get(key, list())
            group.append(s)
            groups[key] = group
        result = []
        for g in groups.values():
            result.append(g)
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"], ["matter", "rematt", "tamter"]],
                         Solution().groupAnagrams(
                             ["eat", "matter", "tea", "tan", "rematt", "ate", "nat", "bat", "tamter"]))


if __name__ == "__main__":
    unittest.main()
