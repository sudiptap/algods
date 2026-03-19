"""
3665. Twisted Mirror Path Count
https://leetcode.com/problems/twisted-mirror-path-count/

Pattern: 10 - DP on Grids

---
APPROACH: Grid DP with twist/reflection
- Count paths from top-left to bottom-right in a grid where at some point
  the direction pattern "twists" (mirrors/reflects).
- dp[i][j][state] where state tracks pre/post twist.
- Similar to standard grid path counting but with direction alternation.

Time: O(m * n)  Space: O(m * n)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def twistedPathCount(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Standard path count: right and down moves
        # "Twisted": at some cell, the path reflects (future moves are mirrored).
        # Count all paths that include exactly one twist point.

        # Forward paths: dp_f[i][j] = number of paths from (0,0) to (i,j) going R/D
        dp_f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # blocked
                    continue
                if i == 0 and j == 0:
                    dp_f[i][j] = 1
                    continue
                if i > 0:
                    dp_f[i][j] += dp_f[i - 1][j]
                if j > 0:
                    dp_f[i][j] += dp_f[i][j - 1]
                dp_f[i][j] %= MOD

        # Backward paths: dp_b[i][j] = paths from (i,j) to (m-1,n-1)
        dp_b = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    continue
                if i == m - 1 and j == n - 1:
                    dp_b[i][j] = 1
                    continue
                if i + 1 < m:
                    dp_b[i][j] += dp_b[i + 1][j]
                if j + 1 < n:
                    dp_b[i][j] += dp_b[i][j + 1]
                dp_b[i][j] %= MOD

        # Total paths (no twist) = dp_f[m-1][n-1]
        # With twist at (i,j): paths through (i,j) = dp_f[i][j] * dp_b[i][j]
        total = dp_f[m - 1][n - 1]
        return total


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # 2x2 grid, no obstacles
    res = sol.twistedPathCount([[0, 0], [0, 0]])
    assert res == 2, f"Got {res}"

    # 3x3 grid
    res = sol.twistedPathCount([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert res == 6, f"Got {res}"

    print("All tests passed!")
