# Dynamic Programming (DP)

## When to Use
- **Optimal substructure**: optimal solution is built from optimal sub-solutions
- **Overlapping subproblems**: same subproblems solved repeatedly
- Counting ways, min/max optimization, yes/no feasibility
- Keywords: "minimum cost", "maximum profit", "number of ways", "can you reach"

## Core Idea
Break the problem into subproblems. Store results to avoid recomputation. Two approaches: top-down (memoization) or bottom-up (tabulation).

## Framework: FAST Method
1. **F**ind the recursive solution
2. **A**nalyze for overlapping subproblems
3. **S**ave results (memoize or tabulate)
4. **T**urn around (convert to bottom-up if needed)

## Templates

### Top-Down (Memoization)
```python
from functools import lru_cache

def solve(nums):
    @lru_cache(maxsize=None)
    def dp(i):
        if i == 0:
            return base_case
        return recurrence(dp(i - 1), ...)
    return dp(len(nums) - 1)
```

### Bottom-Up (Tabulation)
```python
def solve(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = base_case
    for i in range(1, n + 1):
        dp[i] = recurrence(dp[i - 1], ...)
    return dp[n]
```

### Common Sub-Patterns

**0/1 Knapsack**
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # skip item
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]
```

**Longest Common Subsequence**
```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

## Complexity
- Varies per problem. Generally O(n * state_space)
- Space can often be optimized from 2D to 1D

## Classic Problems
| # | Problem | Difficulty | Sub-pattern | Status |
|---|---------|-----------|-------------|--------|
| 53 | Maximum Subarray | Medium | Kadane's | |
| 62 | Unique Paths | Medium | Grid DP | |
| 70 | Climbing Stairs | Easy | Fibonacci | |
| 198 | House Robber | Medium | Linear DP | |
| 300 | Longest Increasing Subsequence | Medium | LIS | |
| 322 | Coin Change | Medium | Unbounded Knapsack | |
| 416 | Partition Equal Subset Sum | Medium | 0/1 Knapsack | |
| 494 | Target Sum | Medium | 0/1 Knapsack | |
| 518 | Coin Change II | Medium | Unbounded Knapsack | |
| 1143 | Longest Common Subsequence | Medium | LCS | |
| 72 | Edit Distance | Medium | String DP | |
| 139 | Word Break | Medium | Linear DP | |
| 152 | Maximum Product Subarray | Medium | Kadane's variant | |

## Tips
- Start with brute-force recursion, then add memoization
- Draw the state transition diagram
- Ask: "What's the **last** decision I make?" — that often defines the recurrence
- Space optimization: if `dp[i]` only depends on `dp[i-1]`, use two variables instead of an array
