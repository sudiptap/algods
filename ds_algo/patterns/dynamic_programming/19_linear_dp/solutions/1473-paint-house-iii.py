"""
1473. Paint House III (Hard)

Pattern: Linear DP (19)
Approach:
    dp[i][j][k] = minimum cost to paint the first i houses such that there
    are exactly j neighborhoods and house i is painted color k.

    Transitions:
        - If house i is already painted (houses[i] != 0), skip to that color.
        - Otherwise, try every color c in [1..n]:
            * If c == prev_color (color of house i-1), neighborhoods stay the same.
            * If c != prev_color, neighborhoods increase by 1.
    Base case: dp[0][neighborhoods_from_house0][color_of_house0] = cost[0][color-1].
    Answer: min(dp[m-1][target][c]) over all colors c.

Complexity:
    Time:  O(m * target * n * n) where m = houses, n = colors
    Space: O(m * target * n)
"""

from typing import List
import math


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """Return minimum cost to paint all houses forming exactly target neighborhoods."""
        INF = float('inf')
        # dp[j][k] = min cost with j neighborhoods, last house colored k (1-indexed)
        # Initialize with infinity
        dp = [[INF] * (n + 1) for _ in range(target + 1)]

        # Base case: house 0
        if houses[0] != 0:
            dp[1][houses[0]] = 0
        else:
            for c in range(1, n + 1):
                dp[1][c] = cost[0][c - 1]

        for i in range(1, m):
            new_dp = [[INF] * (n + 1) for _ in range(target + 1)]
            if houses[i] != 0:
                c = houses[i]
                for j in range(1, target + 1):
                    # Same color as previous house -> same neighborhood count
                    val = dp[j][c]
                    # Different color -> neighborhood count was j-1
                    if j >= 2:
                        for prev_c in range(1, n + 1):
                            if prev_c != c:
                                val = min(val, dp[j - 1][prev_c])
                    new_dp[j][c] = min(new_dp[j][c], val)
            else:
                for c in range(1, n + 1):
                    c_cost = cost[i][c - 1]
                    for j in range(1, target + 1):
                        val = dp[j][c]  # same color as prev
                        if j >= 2:
                            for prev_c in range(1, n + 1):
                                if prev_c != c:
                                    val = min(val, dp[j - 1][prev_c])
                        if val < INF:
                            new_dp[j][c] = min(new_dp[j][c], val + c_cost)
            dp = new_dp

        ans = min(dp[target][c] for c in range(1, n + 1))
        return ans if ans < INF else -1


# ---------- Tests ----------
import unittest


class TestPaintHouseIII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        houses = [0, 0, 0, 0, 0]
        cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
        self.assertEqual(self.sol.minCost(houses, cost, 5, 2, 3), 9)

    def test_example2(self):
        houses = [0, 2, 1, 2, 0]
        cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
        self.assertEqual(self.sol.minCost(houses, cost, 5, 2, 3), 11)

    def test_example3(self):
        houses = [3, 1, 2, 3]
        cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.sol.minCost(houses, cost, 4, 3, 3), -1)

    def test_single_house(self):
        houses = [0]
        cost = [[5, 3, 8]]
        self.assertEqual(self.sol.minCost(houses, cost, 1, 3, 1), 3)

    def test_all_painted(self):
        houses = [1, 1, 1]
        cost = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(self.sol.minCost(houses, cost, 3, 2, 1), 0)

    def test_impossible(self):
        houses = [1, 2, 1, 2]
        cost = [[1, 2], [1, 2], [1, 2], [1, 2]]
        # neighborhoods = 4, target = 1 -> impossible
        self.assertEqual(self.sol.minCost(houses, cost, 4, 2, 1), -1)


if __name__ == "__main__":
    unittest.main()
