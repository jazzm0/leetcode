import unittest
from typing import List


# https://leetcode.com/problems/group-anagrams

class Solution:

    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts_s, char_counts_t = {}, {}

        for i in range(len(s)):
            char_counts_s[s[i]] = char_counts_s.get(s[i], 0) + 1
            char_counts_t[t[i]] = char_counts_t.get(t[i], 0) + 1

        for k, v in char_counts_s.items():
            if k not in char_counts_t or char_counts_t[k] != v:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_of_same_length = {}
        for s in strs:
            groups = groups_of_same_length.get(len(s), {})
            found_group = False
            for k, v in groups.items():
                if self.is_anagram(s, k):
                    v.append(s)
                    found_group = True
            if not found_group:
                groups[s] = [s]
            groups_of_same_length[len(s)] = groups
        result = []
        for group in groups_of_same_length.values():
            for g in group.values():
                result.append(g)
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"], ["matter", "rematt", "tamter"]],
                         Solution().groupAnagrams(
                             ["eat", "matter", "tea", "tan", "rematt", "ate", "nat", "bat", "tamter"]))


if __name__ == "__main__":
    unittest.main()
