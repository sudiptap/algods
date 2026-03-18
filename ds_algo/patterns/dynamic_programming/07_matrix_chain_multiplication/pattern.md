# Matrix Chain Multiplication (MCM) / Interval Merge Pattern

## Core Idea
Try every possible split point in a range [i, j] and pick the optimal one.

## Template
```python
def mcm(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):          # subproblem size
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):   # split point
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]
```

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## Classic Problems
- 312. Burst Balloons
- 1039. Minimum Score Triangulation of Polygon
- 1000. Minimum Cost to Merge Stones
- 241. Different Ways to Add Parentheses
