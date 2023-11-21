import unittest
from typing import List, Set


# https://leetcode.com/problems/valid-sudoku

class Solution:

    def check_row(self, numbers: List[str], valid_numbers: Set[int]) -> bool:
        sawn = set()
        for i in range(len(numbers)):
            if numbers[i] == '.':
                continue
            number = int(numbers[i])
            if number not in valid_numbers or number in sawn:
                return False
            sawn.add(number)
        return True

    def check_column(self, board: List[List[str]], column: int, valid_numbers: Set[int]) -> bool:
        sawn = set()
        for i in range(len(board[column])):
            if board[i][column] == '.':
                continue
            number = int(board[i][column])
            if number not in valid_numbers or number in sawn:
                return False
            sawn.add(number)
        return True

    def check_square(self, board: List[List[str]], row: int, column: int, valid_numbers: Set[int]) -> bool:
        sawn = set()
        for i in range(3):
            for j in range(3):
                if board[row + i][column + j] == '.':
                    continue
                number = int(board[row + i][column + j])
                if number not in valid_numbers or number in sawn:
                    return False
                sawn.add(number)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != len(board[0]) != 9:
            return False

        valid_numbers = set([x for x in range(1, 10)])
        for i in range(len(board)):
            if not self.check_row(board[i], valid_numbers) or not self.check_column(board, i, valid_numbers):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not self.check_square(board, i, j, valid_numbers):
                    return False
        return True


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(True, Solution().isValidSudoku([
            ["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


if __name__ == "__main__":
    unittest.main()
