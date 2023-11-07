import unittest
from typing import List


# https://leetcode.com/problems/text-justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        while i < len(words):
            j, current_length, character_count = i + 1, len(words[i]), len(words[i])
            while current_length < maxWidth:
                if j < len(words) and current_length + len(words[j]) < maxWidth:
                    character_count += len(words[j])
                    current_length += 1 + len(words[j])
                    j += 1
                else:
                    break
            result.append(self.assemlbe_line(i, j, character_count, maxWidth, words))
            i = j
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

            size = space_count // places_needed

            if space_count == size * places_needed:
                return (" " * size).join(words[start:end])
            else:
                left, last = size + 1, size
                line = ""
                for i in range(start, end):
                    line += words[i]
                    if i < end - 2 and len(line) + left + len(words[i + 1]) + last + len(words[i + 2]) <= maxWidth:
                        line += left * " "
                    elif i == end - 2:
                        line += last * " "
                    places_needed -= 1

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
