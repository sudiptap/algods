"""
3797. Count Routes to Climb a Rectangular Grid
https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Layer-by-layer DP with movement constraints
- Grid of '.' (available) and '#' (blocked).
- Start from any cell in bottom row, end at any cell in top row.
- Move constraints: Euclidean distance <= d, move to same row or one row up,
  cannot stay on same row for two consecutive turns.
- DP: dp[row][col][last_was_horizontal] = number of routes reaching (row,col)
  with last_was_horizontal indicating if we moved horizontally last turn.
- Process from bottom row (n-1) upward to row 0.

Time: O(n * m^2 * d)  Space: O(m)
---
"""

from typing import List
import math


class Solution:
    def countRoutes(self, grid: List[str], d: int) -> int:
        MOD = 10**9 + 7
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0

        if n == 0 or m == 0:
            return 0

        # State: dp[col][last_horizontal]
        # last_horizontal: 0 = last move was vertical (or start), 1 = horizontal
        # Process from bottom (row n-1) to top (row 0).

        # Initialize: start at any available cell in bottom row
        # "Start" means no previous move, so last_horizontal = 0
        dp = [[0] * 2 for _ in range(m)]
        for c in range(m):
            if grid[n - 1][c] == '.':
                dp[c][0] = 1  # starting positions, last move = "vertical" (came from outside)

        if n == 1:
            # Already at top row, but can do one horizontal move
            # dp[c][0] = 1 for each available cell (start)
            # Can move horizontally once from any start
            new_dp = [[0] * 2 for _ in range(m)]
            for c in range(m):
                new_dp[c][0] = dp[c][0]
                new_dp[c][1] = dp[c][1]
            for c1 in range(m):
                if grid[0][c1] != '.' or dp[c1][0] == 0:
                    continue
                for c2 in range(m):
                    if c1 == c2 or grid[0][c2] != '.':
                        continue
                    if abs(c1 - c2) <= d:
                        new_dp[c2][1] = (new_dp[c2][1] + dp[c1][0]) % MOD
            return sum(new_dp[c][0] + new_dp[c][1] for c in range(m)) % MOD

        # For each row from n-1 up to 0:
        # From current position, can move horizontally (same row) or vertically (up one row).
        # Constraint: can't do horizontal twice in a row.

        for row in range(n - 1, -1, -1):
            # First, handle horizontal moves within this row
            # Can make horizontal moves if last move was vertical (last_horizontal=0)
            # After horizontal move, last_horizontal becomes 1.
            # Multiple horizontal moves in sequence are NOT allowed (can't stay on same row
            # for two consecutive turns). So at most one horizontal move before going up.

            # Collect horizontal moves: from (row, c1) to (row, c2) with dist <= d
            # Only if last move was vertical (last_horizontal=0)
            new_dp_horiz = [[0] * 2 for _ in range(m)]
            for c in range(m):
                if grid[row][c] != '.':
                    continue
                # Copy non-horizontal paths through
                new_dp_horiz[c][0] = dp[c][0]
                new_dp_horiz[c][1] = dp[c][1]

            for c1 in range(m):
                if grid[row][c1] != '.' or dp[c1][0] == 0:
                    continue
                for c2 in range(m):
                    if c1 == c2 or grid[row][c2] != '.':
                        continue
                    dist = abs(c1 - c2)
                    if dist <= d:
                        new_dp_horiz[c2][1] = (new_dp_horiz[c2][1] + dp[c1][0]) % MOD

            dp = new_dp_horiz

            # Then handle vertical moves to row-1
            if row > 0:
                new_dp = [[0] * 2 for _ in range(m)]
                for c1 in range(m):
                    if grid[row][c1] != '.':
                        continue
                    total = (dp[c1][0] + dp[c1][1]) % MOD
                    if total == 0:
                        continue
                    for c2 in range(m):
                        if grid[row - 1][c2] != '.':
                            continue
                        dist_sq = 1 + (c1 - c2) ** 2
                        if dist_sq <= d * d:
                            new_dp[c2][0] = (new_dp[c2][0] + total) % MOD
                dp = new_dp

        # Sum all paths that reached top row (row 0)
        ans = 0
        for c in range(m):
            ans = (ans + dp[c][0] + dp[c][1]) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countRoutes(["..", "#."], 1) == 2
    assert sol.countRoutes(["..", "#."], 2) == 4
    assert sol.countRoutes(["#"], 750) == 0
    assert sol.countRoutes([".."], 1) == 4

    print("all tests passed")
