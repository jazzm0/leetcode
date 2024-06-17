import unittest
from typing import Tuple


# https://leetcode.com/problems/dota2-senate

class Solution:
    def all_same(self, senate: str) -> str:
        result = all(c == senate[0] for c in senate)
        if result:
            if senate[0] == "R":
                return "Radiant"
            else:
                return "Dire"

    def delete_next(self, senate: str, party: str, start: int) -> Tuple[bool, str]:
        if len(senate) == 1:
            return False, senate
        for i in range(start, len(senate)):
            if senate[i] == party:
                return False, senate[:i] + senate[i + 1:]
        for i in range(0, start):
            if senate[i] == party:
                return True, senate[:i] + senate[i + 1:]

    def predictPartyVictory(self, senate: str) -> str:
        i = 0
        while True:
            all_same = self.all_same(senate)
            if all_same:
                return all_same
            if senate[i] == "R":
                deleted_previous, senate = self.delete_next(senate, "D", i)
            elif senate[i] == "D":
                deleted_previous, senate = self.delete_next(senate, "R", i)
            if not deleted_previous:
                i += 1
            if i >= len(senate):
                i = 0


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("Radiant", Solution().predictPartyVictory("RD"))

    def test_b(self):
        self.assertEqual("Dire", Solution().predictPartyVictory("RDD"))

    def test_c(self):
        self.assertEqual("Dire", Solution().predictPartyVictory("DDRRR"))

    def test_d(self):
        self.assertEqual("Radiant", Solution().predictPartyVictory("DDRRRR"))

    def test_e(self):
        self.assertEqual("Radiant", Solution().predictPartyVictory("DDDRRRRR"))
