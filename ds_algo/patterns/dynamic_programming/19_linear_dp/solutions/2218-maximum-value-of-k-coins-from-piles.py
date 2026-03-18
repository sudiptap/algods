"""
2218. Maximum Value of K Coins From Piles (Hard)
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

Pattern: Linear DP (Knapsack-style)

There are n piles of coins. You can take coins only from the top of each pile.
Given an integer k, return the maximum total value of coins you can collect by
taking exactly k coins in total.

Approach:
    Treat this as a bounded knapsack. Maintain dp[j] = max value using exactly
    j coins from the piles processed so far. For each pile, compute prefix
    sums, then for each capacity j (from k down), try taking 1..min(len(pile), j)
    coins from the current pile's top.

Time:  O(n * k * max_pile_size)  -- but sum of all pile sizes <= 2000
Space: O(k)
"""

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """Return the maximum value collecting exactly k coins from the tops of piles."""
        dp = [0] * (k + 1)

        for pile in piles:
            # Prefix sums for the current pile
            prefix = [0]
            for coin in pile:
                prefix.append(prefix[-1] + coin)

            # Update dp in reverse to avoid using same pile twice
            for j in range(k, 0, -1):
                for take in range(1, min(len(pile), j) + 1):
                    dp[j] = max(dp[j], dp[j - take] + prefix[take])

        return dp[k]


# ---------- Tests ----------
import unittest


class TestMaxValueOfCoins(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        piles = [[1, 100, 3], [7, 8, 9]]
        self.assertEqual(self.sol.maxValueOfCoins(piles, 2), 101)

    def test_example2(self):
        piles = [[100], [100], [100], [100], [100], [100],
                 [1, 1, 1, 1, 1, 1, 700]]
        self.assertEqual(self.sol.maxValueOfCoins(piles, 7), 706)

    def test_single_pile(self):
        piles = [[5, 3, 1]]
        self.assertEqual(self.sol.maxValueOfCoins(piles, 2), 8)

    def test_k_equals_one(self):
        piles = [[1, 2], [3, 4]]
        self.assertEqual(self.sol.maxValueOfCoins(piles, 1), 3)

    def test_take_all(self):
        piles = [[1, 2], [3]]
        self.assertEqual(self.sol.maxValueOfCoins(piles, 3), 6)


if __name__ == "__main__":
    unittest.main()
