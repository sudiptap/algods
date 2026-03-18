# 0/1 Knapsack Pattern

## Core Idea
For each item, decide to include or exclude it. Each item can be used at most once.

## Template
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):  # reverse to avoid reuse
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
```

## Key Insight
Iterate capacity **backwards** to ensure each item is used at most once.

## Complexity
- Time: O(n * capacity)
- Space: O(capacity) with 1D optimization

## Classic Problems
- 416. Partition Equal Subset Sum
- 494. Target Sum
- 474. Ones and Zeroes
- 1049. Last Stone Weight II
