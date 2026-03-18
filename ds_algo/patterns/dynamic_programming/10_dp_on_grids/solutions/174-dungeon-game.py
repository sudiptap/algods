"""
174. Dungeon Game
https://leetcode.com/problems/dungeon-game/

Pattern: 10 - DP on Grids (reverse traversal)

A knight starts at top-left of an m x n grid and must reach bottom-right.
Each cell contains an integer (positive = health gain, negative = damage).
The knight dies if health drops to 0 or below at any point.
Return the minimum initial health needed to reach the bottom-right alive.

---
APPROACH: Backward DP from bottom-right
- Forward DP fails because the optimal path depends on FUTURE cells.
- Work backwards: dp[i][j] = minimum health needed when entering cell (i,j)
  to eventually reach the princess alive.
- Base: dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
- Transition: dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
  We pick the better next cell (min health needed), then subtract current
  cell's effect. Health must be at least 1.
- Answer: dp[0][0]

Time: O(m * n)  Space: O(n) with rolling array, O(m * n) with full grid
---
"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # dp[i][j] = min health needed at (i, j) to reach (m-1, n-1) alive
        dp = [[0] * n for _ in range(m)]

        # Fill bottom-right corner
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        # Last row: can only go right
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])

        # Last column: can only go down
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        # Fill rest bottom-up, right-to-left
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_next = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_next - dungeon[i][j])

        return dp[0][0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [[-2,-3,3],[-5,-10,1],[10,30,-5]] -> 7
    # Path: right->right->down->down needs 7 initial health
    assert sol.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]) == 7

    # Single cell positive: need 1
    assert sol.calculateMinimumHP([[0]]) == 1
    assert sol.calculateMinimumHP([[100]]) == 1

    # Single cell negative: need |val| + 1
    assert sol.calculateMinimumHP([[-5]]) == 6

    # Single row
    assert sol.calculateMinimumHP([[-3, 5]]) == 4

    # Single column
    assert sol.calculateMinimumHP([[-3], [5]]) == 4

    # All positive: always need 1
    assert sol.calculateMinimumHP([[1, 2], [3, 4]]) == 1

    # Larger grid
    assert sol.calculateMinimumHP([
        [1, -3, 3],
        [0, -2, 0],
        [-3, -3, -3]
    ]) == 3

    print("Solution: all tests passed")
