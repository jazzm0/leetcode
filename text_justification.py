import unittest
from typing import List


# https://leetcode.com/problems/text-justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start = 0
        while start < len(words):
            end, current_length, character_count = start + 1, len(words[start]), len(words[start])
            while current_length < maxWidth:
                if end < len(words) and current_length + len(words[end]) < maxWidth:
                    character_count += len(words[end])
                    current_length += 1 + len(words[end])
                    end += 1
                else:
                    break
            result.append(self.assemlbe_line(start, end, character_count, maxWidth, words))
            start = end
        return result

    def assemlbe_line(self, start: int, end: int, character_count: int, maxWidth: int, words: List[str]) -> str:
        if end - start == 1:
            return words[start] + (maxWidth - len(words[start])) * " "

        if end == len(words):
            line = " ".join(words[start:end])
            return line + (maxWidth - len(line)) * " "
        else:
            space_count = maxWidth - character_count
            places_needed = end - start - 1
            slice_size = space_count // places_needed

            if space_count == slice_size * places_needed:
                return (" " * slice_size).join(words[start:end])
            else:
                big_slice_count = space_count % places_needed
                multiplier = slice_size + 1
                line = ""
                for i in range(start, end):
                    line += words[i]
                    line += multiplier * " "
                    big_slice_count -= 1
                    if big_slice_count == 0:
                        multiplier -= 1
                    if i == end - 2:
                        multiplier = 0
        return line


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([
            "This    is    an",
            "example  of text",
            "justification.  "
        ], Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

    def test_b(self):
        self.assertEqual([
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ], Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))

    def test_c(self):
        self.assertEqual([
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ], Solution().fullJustify(
            ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"], 20))

    def test_d(self):
        self.assertEqual(
            ["ask   not   what",
             "your country can",
             "do  for  you ask",
             "what  you can do",
             "for your country"],
            Solution().fullJustify(
                ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do",
                 "for", "your", "country"], 16))


if __name__ == "__main__":
    unittest.main()
