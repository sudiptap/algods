"""
2267. Check if There Is a Valid Parentheses String Path
https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

Pattern: 10 - DP on Grids

---
APPROACH: dp[i][j][balance] - DFS/DP through grid tracking parenthesis balance
- At each cell (i,j), '(' adds +1 to balance, ')' adds -1.
- If balance < 0 at any point, invalid. At (m-1,n-1), balance must be 0.
- Use set of reachable balances at each cell.
- dp[i][j] = set of valid balances reachable at cell (i,j).

Time: O(m * n * (m+n))  Space: O(m * n * (m+n))
---
"""

from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        # Total path length is m+n-1, must be even for valid parens
        if (m + n - 1) % 2 == 1:
            return False

        # dp[i][j] = set of valid balances at (i,j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                delta = 1 if grid[i][j] == '(' else -1
                if i == 0 and j == 0:
                    if delta >= 0:
                        dp[0][0].add(delta)
                    continue

                sources = set()
                if i > 0:
                    sources |= dp[i - 1][j]
                if j > 0:
                    sources |= dp[i][j - 1]

                max_balance = (m - 1 - i) + (n - 1 - j)  # max possible closing parens remaining
                for b in sources:
                    nb = b + delta
                    if 0 <= nb <= max_balance:
                        dp[i][j].add(nb)

        return 0 in dp[m - 1][n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]] ) == True
    assert sol.hasValidPath([[")",")"],["(","("]]) == False
    assert sol.hasValidPath([["(",")"]] ) == True
    assert sol.hasValidPath([["("]]) == False

    print("all tests passed")
