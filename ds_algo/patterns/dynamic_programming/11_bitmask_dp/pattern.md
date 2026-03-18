# Bitmask DP

## Core Idea
Use a bitmask to represent which elements have been used/visited. State = (bitmask, current_position).

## Template
```python
def bitmask_dp(n, dist):
    # TSP example: dp[mask][i] = min cost to visit cities in mask, ending at i
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at city 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    full_mask = (1 << n) - 1
    return min(dp[full_mask][i] + dist[i][0] for i in range(n))
```

## Complexity
- Time: O(2^n * n^2)
- Space: O(2^n * n)
- Practical limit: n <= 20

## Classic Problems
- Travelling Salesman Problem
- 698. Partition to K Equal Sum Subsets
- 943. Find the Shortest Superstring
- 1125. Smallest Sufficient Team
