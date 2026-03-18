"""
576. Out of Boundary Paths
https://leetcode.com/problems/out-of-boundary-paths/

Pattern: 17 - Probability DP

---
APPROACH: 3D DP (moves × grid)
- dp[moves][i][j] = number of paths to reach cell (i, j) using exactly `moves` moves
- For each cell, try all 4 directions. If the next position is out of bounds,
  add dp[moves][i][j] to the answer (the ball has exited). Otherwise propagate
  to dp[moves+1][ni][nj].
- Base: dp[0][startRow][startColumn] = 1
- Optimise space by keeping only current and next move layers.

Time: O(maxMove * m * n)   Space: O(m * n)
---
"""

MOD = 10**9 + 7


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """Return the number of paths the ball can exit the grid within maxMove moves."""
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0

        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            new_dp[ni][nj] = (new_dp[ni][nj] + dp[i][j]) % MOD
                        else:
                            result = (result + dp[i][j]) % MOD
            dp = new_dp

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.findPaths(2, 2, 2, 0, 0) == 6
    assert sol.findPaths(1, 3, 3, 0, 1) == 12
    assert sol.findPaths(1, 1, 1, 0, 0) == 4
    assert sol.findPaths(1, 1, 0, 0, 0) == 0
    assert sol.findPaths(2, 3, 1, 0, 0) == 2
    assert sol.findPaths(8, 50, 23, 5, 26) == 914783380

    print("all tests passed")
