"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

Pattern: 10 - DP on Grids (THE intro problem for this pattern)

---
APPROACH 1: 2D DP
- dp[i][j] = number of ways to reach (i, j)
- dp[i][j] = dp[i-1][j] + dp[i][j-1]  (from above + from left)
- Base: first row and first column are all 1 (only one way to reach them)

Time: O(m*n)  Space: O(m*n)

APPROACH 2: 1D DP (space-optimized)
- Only need previous row → single array, update left to right
- dp[j] += dp[j-1]  (dp[j] already has "from above", dp[j-1] has "from left")

Time: O(m*n)  Space: O(n)

APPROACH 3: Math (combinatorics)
- Total moves = (m-1) downs + (n-1) rights = (m+n-2) moves
- Choose which (m-1) of them are downs: C(m+n-2, m-1)

Time: O(min(m,n))  Space: O(1)
---
"""

from math import comb


# ---------- Approach 1: 2D DP ----------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


# ---------- Approach 2: 1D DP ----------
class SolutionOptimized:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]


# ---------- Approach 3: Math ----------
class SolutionMath:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionOptimized, SolutionMath]:
        sol = Sol()

        assert sol.uniquePaths(3, 7) == 28
        assert sol.uniquePaths(3, 2) == 3
        assert sol.uniquePaths(1, 1) == 1
        assert sol.uniquePaths(1, 5) == 1
        assert sol.uniquePaths(7, 3) == 28  # symmetric
        assert sol.uniquePaths(10, 10) == 48620

        print(f"{Sol.__name__}: all tests passed")
