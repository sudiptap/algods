"""
2184. Number of Ways to Build Sturdy Brick Wall (Medium)
https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

Build a wall of height x width using bricks of given widths. No two
adjacent rows can have aligned vertical edges (except at the boundaries).
Return number of ways mod 10^9+7.

Pattern: Counting / Combinatorial
Approach:
- Generate all valid row patterns (ways to fill a row of given width
  using available brick widths).
- Represent each row pattern by its set of internal vertical edge positions.
- Two rows are compatible if their edge sets don't share any position.
- dp[row][pattern] = number of ways to fill rows 1..row ending with pattern.
- Multiply through the transition matrix for height rows.

Time:  O(height * P^2) where P = number of valid row patterns
Space: O(P)
"""

from typing import List
from collections import defaultdict


class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        """Return number of ways to build a sturdy brick wall.

        Args:
            height: Number of rows.
            width: Width of the wall.
            bricks: Available brick widths.

        Returns:
            Count of valid walls mod 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Generate all valid row patterns
        # A pattern is represented by a frozenset of internal edge positions
        patterns = []

        def gen_row(pos, edges):
            if pos == width:
                patterns.append(frozenset(edges))
                return
            for b in bricks:
                if pos + b <= width:
                    new_edges = edges[:]
                    if pos + b < width:
                        new_edges.append(pos + b)
                    gen_row(pos + b, new_edges)

        gen_row(0, [])

        n = len(patterns)
        if n == 0:
            return 0

        # Precompute compatibility
        compat = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if not patterns[i] & patterns[j]:  # no shared edges
                    compat[i].append(j)

        # DP
        dp = [1] * n  # first row: any pattern

        for _ in range(height - 1):
            new_dp = [0] * n
            for j in range(n):
                for i in compat[j]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD


# ---------- tests ----------
def test_build_wall():
    sol = Solution()

    # Example 1: height=2, width=3, bricks=[1,2]
    assert sol.buildWall(2, 3, [1, 2]) == 2

    # Example 2: height=1, width=1, bricks=[5] -> 0 (can't fill)
    assert sol.buildWall(1, 1, [5]) == 0

    # Single brick fills exactly
    assert sol.buildWall(1, 3, [3]) == 1

    # height=1, any pattern works
    assert sol.buildWall(1, 2, [1, 2]) == 2

    print("All tests passed for 2184. Number of Ways to Build Sturdy Brick Wall")


if __name__ == "__main__":
    test_build_wall()
