import unittest
from typing import List


# https://leetcode.com/problems/trapping-rain-water

class Solution:

    def sum_trap(self, height: List[int], start: int, end: int) -> int:
        if end - start < 2:
            return 0
        s = 0
        h = min(height[start], height[end])
        for i in range(start + 1, end):
            s += h - height[i]
        return s

    def find_next_right(self, start: int, height: List[int]) -> int:
        max_height, max_height_index, reference_height = 0, -1, height[start]
        for i in range(start, len(height)):
            if height[i] > reference_height:
                return i
            if height[i] > max_height and i != start:
                max_height_index = i
                max_height = height[i]
        return max_height_index

    def get_local_min_count(self, height: List[int]) -> bool:
        down_slope, climb_slope = False, False
        for i in range(len(height) - 2):
            if height[i] > height[i + 1]:
                down_slope = True
            if height[i + 1] < height[i + 2]:
                climb_slope = True
        return down_slope and climb_slope

    def find_boundaries(self, height: List[int]) -> List[tuple[int, int]]:
        result = []
        i = 0
        while i < len(height):
            if height[i] == 0:
                i += 1
                continue
            next_index = self.find_next_right(i, height)
            if next_index > 0:
                result.append((i, next_index))
                i = next_index
            else:
                break
        return result

    def trap(self, height: List[int]) -> int:
        trapped = 0
        if not self.get_local_min_count(height):
            return 0

        boundaries = self.find_boundaries(height)
        for b in boundaries:
            trapped += self.sum_trap(height, b[0], b[1])
        return trapped


class TestStringMethods(unittest.TestCase):

    def test_a1(self):
        solution = Solution()

        self.assertEqual(1, solution.sum_trap([4, 2, 3], 0, 2))

    def test_a2(self):
        solution = Solution()

        self.assertEqual(0, solution.sum_trap([4, 2, 3], 0, 1))

    def test_a3(self):
        solution = Solution()

        self.assertEqual(3, solution.find_next_right(1, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(7, solution.find_next_right(3, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(8, solution.find_next_right(7, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(10, solution.find_next_right(8, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_a(self):
        solution = Solution()

        self.assertEqual(6, solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_b(self):
        solution = Solution()

        self.assertEqual(1, solution.trap([4, 2, 3]))

    def test_c(self):
        solution = Solution()

        self.assertEqual(1, solution.trap([4, 9, 4, 5, 3, 2]))

    def test_d(self):
        solution = Solution()

        self.assertEqual(9, solution.trap([4, 2, 0, 3, 2, 5]))

    def test_e(self):
        solution = Solution()

        self.assertEqual(1, solution.trap([5, 4, 1, 2]))

    def test_f(self):
        solution = Solution()

        self.assertEqual(23, solution.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))

    def test_g(self):
        solution = Solution()

        self.assertEqual(0, solution.trap([1] * 20000))


if __name__ == "__main__":
    unittest.main()
