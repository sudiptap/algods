"""
1547. Minimum Cost to Cut a Stick (Hard)

Pattern: Matrix Chain Multiplication (07)
Approach:
    Sort the cuts array and add endpoints 0 and n.
    dp[i][j] = minimum cost to make all cuts between cuts[i] and cuts[j].

    For each interval [i, j], try every possible cut point mid in (i+1..j-1):
        dp[i][j] = min(dp[i][mid] + dp[mid][j]) + (cuts[j] - cuts[i])

    The cost of a cut is the length of the current stick segment (cuts[j] - cuts[i]).
    Base case: dp[i][i+1] = 0 (no cuts to make in adjacent positions).

Complexity:
    Time:  O(c^3) where c = len(cuts)
    Space: O(c^2)
"""

from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """Return the minimum total cost of making all the cuts."""
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        m = len(cuts)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if j - i <= 1:
                return 0
            return (cuts[j] - cuts[i]) + min(
                dp(i, mid) + dp(mid, j) for mid in range(i + 1, j)
            )

        return dp(0, m - 1)


# ---------- Tests ----------
import unittest


class TestMinCostCutStick(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.minCost(7, [1, 3, 4, 5]), 16)

    def test_example2(self):
        self.assertEqual(self.sol.minCost(9, [5, 6, 1, 4, 2]), 22)

    def test_single_cut(self):
        self.assertEqual(self.sol.minCost(10, [5]), 10)

    def test_two_cuts(self):
        # stick of length 4, cuts at 1, 3
        # cut at 1 first: cost 4, then cut at 3: cost 3 -> total 7
        # cut at 3 first: cost 4, then cut at 1: cost 3 -> total 7
        self.assertEqual(self.sol.minCost(4, [1, 3]), 7)

    def test_adjacent_cuts(self):
        self.assertEqual(self.sol.minCost(5, [1, 2, 3, 4]), 12)

    def test_single_position(self):
        self.assertEqual(self.sol.minCost(2, [1]), 2)


if __name__ == "__main__":
    unittest.main()
