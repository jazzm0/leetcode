import unittest


# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        d, inc, key = {}, 1, 1

        for i in range(len(s)):
            row = d.get(key, list())
            row.append(s[i])
            d[key] = row
            key += inc
            if key == numRows or key == 1:
                inc *= -1

        result = ""
        for i in range(1, numRows + 1):
            if i in d:
                row = d[i]
                for j in range(len(row)):
                    result += row[j]
        return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        self.assertEqual("PAHNAPLSIIGYIR", solution.convert("PAYPALISHIRING", 3))

    def test_b(self):
        solution = Solution()

        self.assertEqual("PINALSIGYAHRPI", solution.convert("PAYPALISHIRING", 4))

    def test_c(self):
        solution = Solution()

        self.assertEqual("ACEBD", solution.convert("ABCDE", 2))


if __name__ == "__main__":
    unittest.main()
