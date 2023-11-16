import unittest
from typing import List


# https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:

    def is_permutation(self, s: str, start: int, step: int, number_of_words: int, words_counts: {}) -> bool:
        for i in range(number_of_words):
            sub_string = s[start + i * step: start + (i + 1) * step]
            if sub_string not in words_counts or words_counts[sub_string] == 0:
                return False
            else:
                words_counts[sub_string] -= 1
        return True

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result, words_counts = [], {}
        for i in range(len(words)):
            words_counts[words[i]] = words_counts.get(words[i], 0) + 1

        step = len(words[0])
        number_of_words = len(words)
        for start in range(len(s) - step * (number_of_words - 1)):
            if self.is_permutation(s, start, step, number_of_words, words_counts.copy()):
                result.append(start)

        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([0, 9], Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))

    def test_b(self):
        self.assertEqual([], Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))

    def test_c(self):
        self.assertEqual([13], Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                                                        ["fooo", "barr", "wing", "ding", "wing"]))


if __name__ == "__main__":
    unittest.main()
