import unittest
from bisect import bisect_left


# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        return len(self.requests) - bisect_left(self.requests, t - 3000)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        recentcounter = RecentCounter()
        self.assertEqual(1, recentcounter.ping(1))
        self.assertEqual(2, recentcounter.ping(100))
        self.assertEqual(3, recentcounter.ping(3001))
        self.assertEqual(3, recentcounter.ping(3002))
