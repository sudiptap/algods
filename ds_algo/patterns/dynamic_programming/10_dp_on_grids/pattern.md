# DP on Grids

## Core Idea
Traverse a 2D grid, building answers from previously visited cells (usually top/left).

## Template
```python
def grid_dp(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    # fill first row and column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    # fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]
```

## Complexity
- Time: O(m * n)
- Space: O(n) with rolling array

## Classic Problems
- 62. Unique Paths
- 64. Minimum Path Sum
- 174. Dungeon Game
- 221. Maximal Square
- 85. Maximal Rectangle
