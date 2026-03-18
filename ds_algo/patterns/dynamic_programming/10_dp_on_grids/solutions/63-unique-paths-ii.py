"""
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

Pattern: 10 - DP on Grids (extension of #62 with obstacles)

---
APPROACH: 1D DP
- Same as #62 but if cell is obstacle, dp[j] = 0
- dp[j] += dp[j-1] only if no obstacle

Time: O(m*n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert sol.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert sol.uniquePathsWithObstacles([[1]]) == 0
    assert sol.uniquePathsWithObstacles([[0]]) == 1
    assert sol.uniquePathsWithObstacles([[0, 0], [1, 0]]) == 1

    print("all tests passed")
