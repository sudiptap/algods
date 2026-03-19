"""
2328. Number of Increasing Paths in a Grid
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

Pattern: 10 - DP on Grids

---
APPROACH: DFS + memoization
- For each cell, count strictly increasing paths starting from it.
- memo[i][j] = number of increasing paths starting at (i,j).
- dfs(i,j) = 1 + sum(dfs(ni,nj)) for neighbors (ni,nj) where grid[ni][nj] > grid[i][j].
- Answer = sum of memo[i][j] for all cells.

Time: O(m * n)  Space: O(m * n)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dfs(i, j):
            res = 1  # path of just this cell
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    res = (res + dfs(ni, nj)) % MOD
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countPaths([[1, 1], [3, 4]]) == 8
    assert sol.countPaths([[1], [2]]) == 3
    assert sol.countPaths([[1]]) == 1

    print("all tests passed")
