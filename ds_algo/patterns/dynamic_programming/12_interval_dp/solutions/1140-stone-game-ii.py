"""
1140. Stone Game II (Medium)
https://leetcode.com/problems/stone-game-ii/

Pattern: 12 - Interval DP (Game Theory)

Alice and Bob take turns (Alice first). On each turn the current player
takes stones from the first X remaining piles where 1 <= X <= 2*M, then
M = max(M, X). Return the maximum stones Alice can get.

Approach:
    Suffix sums + memoized DFS.
    dfs(i, M) = max stones the current player can collect from piles[i:]
                with the given M value.
    Current player tries X = 1..2*M, taking suffix[i] - suffix[i+X] stones,
    and the opponent then gets dfs(i+X, max(M, X)).
    Current player's total = suffix[i] - dfs(i+X, max(M, X)).

Time:  O(n^3)  —  n states for i, n for M, loop up to 2M
Space: O(n^2)
"""

from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """Return the maximum number of stones Alice can get."""
        n = len(piles)

        # Suffix sums: suffix[i] = sum(piles[i:])
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dfs(i: int, M: int) -> int:
            """Max stones the current player can collect from piles[i:]."""
            if i >= n:
                return 0
            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0
            for X in range(1, 2 * M + 1):
                # Current player takes piles[i..i+X-1], getting suffix[i]-suffix[i+X]
                # Opponent then gets dfs(i+X, max(M, X))
                opponent = dfs(i + X, max(M, X))
                best = max(best, suffix[i] - opponent)

            return best

        return dfs(0, 1)


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10

def test_example2():
    assert Solution().stoneGameII([1, 2, 3, 4, 5, 100]) == 104

def test_single_pile():
    assert Solution().stoneGameII([5]) == 5

def test_two_piles():
    assert Solution().stoneGameII([1, 2]) == 3

def test_equal_piles():
    assert Solution().stoneGameII([3, 3, 3, 3]) == 6


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
