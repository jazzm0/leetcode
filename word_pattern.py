import unittest


# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        word_map = {}
        is_mapped = set()
        for i in range(len(pattern)):
            if pattern[i] not in word_map:
                if words[i] in is_mapped:
                    return False
                word_map[pattern[i]] = words[i]
                is_mapped.add(words[i])
            elif words[i] != word_map[pattern[i]]:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().wordPattern("abba", "dog cat cat dog"))

    def test_b(self):
        self.assertEqual(False, Solution().wordPattern("abba", "dog cat cat fish"))

    def test_c(self):
        self.assertEqual(False, Solution().wordPattern("aaaa", "dog cat cat dog"))


if __name__ == "__main__":
    unittest.main()
