import unittest


# https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_counts, magazine_counts = {}, {}
        for i in range(len(ransomNote)):
            ransom_note_counts[ransomNote[i]] = ransom_note_counts.get(ransomNote[i], 0) + 1

        for i in range(len(magazine)):
            magazine_counts[magazine[i]] = magazine_counts.get(magazine[i], 0) + 1

        for k, v in ransom_note_counts.items():
            if k not in magazine_counts or magazine_counts[k] < v:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(False, Solution().canConstruct("a", "b"))

    def test_b(self):
        self.assertEqual(False, Solution().canConstruct("aa", "ab"))

    def test_c(self):
        self.assertEqual(True, Solution().canConstruct("aa", "aab"))


if __name__ == "__main__":
    unittest.main()
