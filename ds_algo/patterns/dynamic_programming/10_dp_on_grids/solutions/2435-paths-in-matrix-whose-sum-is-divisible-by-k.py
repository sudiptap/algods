"""
2435. Paths in Matrix Whose Sum Is Divisible by K
https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

Pattern: 10 - DP on Grids

---
APPROACH: dp[i][j][r] = number of paths reaching (i,j) with sum % k == r
- Only move right or down.
- Transition: dp[i][j][(r + grid[i][j]) % k] += dp[i-1][j][r] + dp[i][j-1][r]
- Answer: dp[m-1][n-1][0]

Time: O(m * n * k)  Space: O(m * n * k), can optimize to O(n * k)
---
"""

from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for r in range(k):
                    nr = (r + grid[i][j]) % k
                    if i > 0:
                        dp[i][j][nr] = (dp[i][j][nr] + dp[i - 1][j][r]) % MOD
                    if j > 0:
                        dp[i][j][nr] = (dp[i][j][nr] + dp[i][j - 1][r]) % MOD

        return dp[m - 1][n - 1][0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3) == 2
    assert sol.numberOfPaths([[0,0]], 5) == 1
    assert sol.numberOfPaths([[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1) == 10

    print("all tests passed")
