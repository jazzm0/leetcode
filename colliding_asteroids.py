import unittest
from typing import List


# https://leetcode.com/problems/asteroid-collision

class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:  # a < 0
                # Destroy the previous positive one(s).
                while stack and 0 < stack[-1] < -a:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == -a:
                    stack.pop()  # Both asteroids explode.
                else:  # stack[-1] > the current asteroid.
                    pass  # Destroy the current asteroid, so do nothing.

        return stack


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([5, 10], Solution().asteroidCollision([5, 10, -5]))

    def test_b(self):
        self.assertEqual([], Solution().asteroidCollision([8, -8]))

    def test_c(self):
        self.assertEqual([10], Solution().asteroidCollision([10, 2, -5]))

    def test_d(self):
        self.assertEqual([-2, -1, 1, 2], Solution().asteroidCollision([-2, -1, 1, 2]))
