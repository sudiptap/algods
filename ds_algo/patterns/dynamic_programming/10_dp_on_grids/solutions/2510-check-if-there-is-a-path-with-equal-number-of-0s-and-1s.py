"""
2510. Check if There is a Path With Equal Number of 0s And 1s
https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

Pattern: 10 - DP on Grids

---
APPROACH: dp[i][j][diff] tracking difference of 1s and 0s
- Path length = m + n - 1. Need equal 0s and 1s, so m+n-1 must be even.
- Treat 0 as -1 and 1 as +1. Need diff == 0 at end.
- dp[i][j] = set of reachable differences at cell (i,j).
- Transition: from (i-1,j) or (i,j-1), add grid[i][j] contribution.

Time: O(m * n * (m+n))  Space: O(m * n * (m+n))
---
"""

from typing import List


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_len = m + n - 1
        if path_len % 2 == 1:
            return False

        # dp[i][j] = set of reachable diffs (count_1 - count_0)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        val = 1 if grid[0][0] == 1 else -1
        dp[0][0].add(val)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = 1 if grid[i][j] == 1 else -1
                sources = set()
                if i > 0:
                    sources |= dp[i - 1][j]
                if j > 0:
                    sources |= dp[i][j - 1]
                dp[i][j] = {d + val for d in sources}

        return 0 in dp[m - 1][n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.isThereAPath([[0, 1, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0]]) == True
    assert sol.isThereAPath([[1, 1, 1], [0, 0, 0]]) == True  # path (1,1,0,0) has 2 of each
    assert sol.isThereAPath([[0, 1], [1, 0]]) == False  # path_len=3 is odd

    print("all tests passed")
