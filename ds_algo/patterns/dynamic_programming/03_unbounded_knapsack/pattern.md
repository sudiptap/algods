# Unbounded Knapsack Pattern

## Core Idea
Items can be reused unlimited times. Iterate capacity **forwards**.

## Template
```python
def unbounded_knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # forward allows reuse
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
```

## Key Insight
Forward iteration on capacity allows the same item to contribute multiple times.

## Complexity
- Time: O(n * capacity)
- Space: O(capacity)

## Classic Problems
- 322. Coin Change
- 518. Coin Change II
- 139. Word Break
- Rod Cutting
