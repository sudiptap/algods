"""
3742. Maximum Path Score in a Grid
https://leetcode.com/problems/maximum-path-score-in-a-grid/

Pattern: 10 - DP on Grids

---
APPROACH: 3D DP tracking position and cost used
- dp[i][j][c] = max score at (i,j) having used cost c.
- Cell value 0: score +0, cost +0. Value 1: score +1, cost +1.
  Value 2: score +2, cost +1.
- grid[0][0] == 0 always.
- Transitions: from (i-1,j) or (i,j-1).
- Return max dp[m-1][n-1][c] for c in [0,k], or -1.

Time: O(m * n * k)  Space: O(n * k) with rolling array
---
"""

from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('-inf')

        # dp[j][c] = max score at column j with cost c
        dp = [[INF] * (k + 1) for _ in range(n)]
        dp[0][0] = 0  # start at (0,0) with cost 0, score 0

        # Fill first row
        for j in range(1, n):
            v = grid[0][j]
            s_add = v
            c_add = 0 if v == 0 else 1
            for c in range(k + 1):
                if dp[j - 1][c] == INF:
                    continue
                nc = c + c_add
                if nc <= k:
                    dp[j][nc] = max(dp[j][nc], dp[j - 1][c] + s_add)

        for i in range(1, m):
            new_dp = [[INF] * (k + 1) for _ in range(n)]
            for j in range(n):
                v = grid[i][j]
                s_add = v
                c_add = 0 if v == 0 else 1

                # From above (dp[j])
                for c in range(k + 1):
                    if dp[j][c] == INF:
                        continue
                    nc = c + c_add
                    if nc <= k:
                        new_dp[j][nc] = max(new_dp[j][nc], dp[j][c] + s_add)

                # From left (new_dp[j-1])
                if j > 0:
                    for c in range(k + 1):
                        if new_dp[j - 1][c] == INF:
                            continue
                        nc = c + c_add
                        if nc <= k:
                            new_dp[j][nc] = max(new_dp[j][nc], new_dp[j - 1][c] + s_add)

            dp = new_dp

        result = max(dp[n - 1])
        return result if result != INF else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxPathScore([[0, 1], [2, 0]], k=1) == 2
    assert sol.maxPathScore([[0, 1], [1, 2]], k=1) == -1
    assert sol.maxPathScore([[0]], k=0) == 0
    assert sol.maxPathScore([[0, 0], [0, 0]], k=0) == 0
    assert sol.maxPathScore([[0, 2], [0, 0]], k=1) == 2

    print("all tests passed")
