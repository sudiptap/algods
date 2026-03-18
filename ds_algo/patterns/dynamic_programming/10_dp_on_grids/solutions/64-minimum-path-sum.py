"""
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Pattern: 10 - DP on Grids

---
APPROACH: 1D DP
- dp[j] = min cost to reach column j in current row
- dp[j] = grid[i][j] + min(dp[j], dp[j-1])  (from above or left)
- First row: only from left. First col: only from above.

Time: O(m*n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert sol.minPathSum([[1]]) == 1

    print("all tests passed")
