import unittest
from typing import List


# https://leetcode.com/problems/game-of-life

class Solution:

    def getLiveNeighbours(self, board: List[List[int]], i: int, j: int) -> int:
        neighbours = 0
        m, n = len(board), len(board[0])

        if i > 0 and j > 0 and board[i - 1][j - 1] == 1:
            neighbours += 1
        if i > 0 and board[i - 1][j] == 1:
            neighbours += 1
        if i > 0 and j < n - 1 and board[i - 1][j + 1] == 1:
            neighbours += 1
        if j > 0 and board[i][j - 1] == 1:
            neighbours += 1
        if j < n - 1 and board[i][j + 1] == 1:
            neighbours += 1
        if i < m - 1 and j > 0 and board[i + 1][j - 1] == 1:
            neighbours += 1
        if i < m - 1 and board[i + 1][j] == 1:
            neighbours += 1
        if i < m - 1 and j < n - 1 and board[i + 1][j + 1] == 1:
            neighbours += 1
        return neighbours

    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        next_state = [[0] * n for _ in range(m)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                neighbours = self.getLiveNeighbours(board, r, c)
                if neighbours < 2 or neighbours > 3:
                    next_state[r][c] = 0
                elif neighbours == 2:
                    next_state[r][c] = board[r][c]
                elif neighbours == 3:
                    if board[r][c] == 0:
                        next_state[r][c] = 1
                    else:
                        next_state[r][c] = board[r][c]

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = next_state[r][c]


class TestStringMethods(unittest.TestCase):
    def test_neighbours(self):
        m = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

        self.assertEqual(1, Solution().getLiveNeighbours(m, 0, 0))
        self.assertEqual(2, Solution().getLiveNeighbours(m, 0, 2))
        self.assertEqual(5, Solution().getLiveNeighbours(m, 1, 1))
        self.assertEqual(3, Solution().getLiveNeighbours(m, 2, 1))

    def test_a(self):
        m = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        Solution().gameOfLife(m)
        self.assertEqual([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]], m)

    def test_b(self):
        m = [[1, 1], [1, 0]]
        Solution().gameOfLife(m)
        self.assertEqual([[1, 1], [1, 1]], m)


if __name__ == "__main__":
    unittest.main()
