"""
2222. Number of Ways to Select Buildings (Medium)
https://leetcode.com/problems/number-of-ways-to-select-buildings/

Pattern: State Machine DP

Given a binary string s representing a row of buildings ('0' = office, '1' =
restaurant), select 3 buildings such that no two adjacent selected buildings
are of the same type. Return the number of valid selections.

The only valid 3-length alternating subsequences are "010" and "101".

Approach:
    Scan left to right, maintaining counts of valid subsequences of each
    length ending with 0 or 1:
      - end0, end1       : count of length-1 subsequences ending in 0 / 1
      - end01, end10     : count of length-2 subsequences ending in 01 / 10
      - end010, end101   : count of length-3 subsequences (the answer)

    When we see '0': end010 += end01, end10 += end1, end0 += 1
    When we see '1': end101 += end10, end01 += end0, end1 += 1

Time:  O(n)
Space: O(1)
"""


class Solution:
    def numberOfWays(self, s: str) -> int:
        """Return the number of ways to select 3 alternating buildings."""
        end0 = end1 = 0
        end01 = end10 = 0
        end010 = end101 = 0

        for ch in s:
            if ch == '0':
                end010 += end01
                end10 += end1
                end0 += 1
            else:
                end101 += end10
                end01 += end0
                end1 += 1

        return end010 + end101


# ---------- Tests ----------
import unittest


class TestNumberOfWays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.numberOfWays("001101"), 6)

    def test_example2(self):
        self.assertEqual(self.sol.numberOfWays("11100"), 0)

    def test_minimum_valid(self):
        self.assertEqual(self.sol.numberOfWays("010"), 1)
        self.assertEqual(self.sol.numberOfWays("101"), 1)

    def test_all_same(self):
        self.assertEqual(self.sol.numberOfWays("000"), 0)
        self.assertEqual(self.sol.numberOfWays("111"), 0)

    def test_alternating(self):
        # "0101" -> subsequences: "010"(positions 0,1,2), "010"(0,1,3-nope: 0,1 are 01 then 0 at 3? s="0101")
        # "010" at (0,1,2), "101" at (1,2,3), "010" at (0,1,2) and (0,3 nope)
        # Let me just count: end sequences for "0101":
        # After '0': end0=1
        # After '1': end1=1, end01=1
        # After '0': end0=2, end10=1, end010=1
        # After '1': end1=2, end01=2, end101=1
        # total = 1 + 1 = 2
        self.assertEqual(self.sol.numberOfWays("0101"), 2)

    def test_longer(self):
        self.assertEqual(self.sol.numberOfWays("10101"), 5)


if __name__ == "__main__":
    unittest.main()
