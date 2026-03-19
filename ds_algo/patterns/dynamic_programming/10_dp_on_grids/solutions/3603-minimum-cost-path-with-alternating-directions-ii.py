"""
3603. Minimum Cost Path with Alternating Directions II
https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

Pattern: 10 - DP on Grids

---
APPROACH: Grid DP with alternating direction constraint
- Move from (0,0) to (m-1,n-1) on a grid.
- Must alternate between right (R) and down (D) moves.
- Two starting options: start with R or start with D.
- dp[i][j][last_move] = min cost to reach (i,j) with last move being R or D.
- Transition: if last was R, next must be D; if last was D, next must be R.

Time: O(m * n)  Space: O(m * n)
---
"""

from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # dp[i][j][0] = min cost reaching (i,j) with last move = Right
        # dp[i][j][1] = min cost reaching (i,j) with last move = Down
        dp = [[[INF, INF] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = grid[0][0]  # pretend last move was R (next must be D)
        dp[0][0][1] = grid[0][0]  # pretend last move was D (next must be R)

        for i in range(m):
            for j in range(n):
                # From (i,j) with last=R (0), next must be D: go to (i+1,j)
                if dp[i][j][0] < INF and i + 1 < m:
                    val = dp[i][j][0] + grid[i + 1][j]
                    dp[i + 1][j][1] = min(dp[i + 1][j][1], val)

                # From (i,j) with last=D (1), next must be R: go to (i,j+1)
                if dp[i][j][1] < INF and j + 1 < n:
                    val = dp[i][j][1] + grid[i][j + 1]
                    dp[i][j + 1][0] = min(dp[i][j + 1][0], val)

        return min(dp[m - 1][n - 1][0], dp[m - 1][n - 1][1])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # 2x2 grid: must go R then D or D then R
    res = sol.minCost([[1, 2], [3, 4]])
    # R then D: 1->2->4 = 7. D then R: 1->3->4 = 8. Min = 7.
    assert res == 7, f"Got {res}"

    # 1x1 grid
    res = sol.minCost([[5]])
    assert res == 5, f"Got {res}"

    print("All tests passed!")
