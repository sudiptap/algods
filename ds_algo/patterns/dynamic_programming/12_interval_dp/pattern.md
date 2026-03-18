# Interval DP

## Core Idea
Solve for small intervals first, build up to larger ones. dp[i][j] = answer for subarray [i..j].

## Template
```python
def interval_dp(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    # base case: single elements
    for i in range(n):
        dp[i][i] = base(arr[i])
    # expand interval length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + merge_cost(i, j))
    return dp[0][n-1]
```

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## Classic Problems
- 546. Remove Boxes
- 877. Stone Game
- 664. Strange Printer
- 1547. Minimum Cost to Cut a Stick
