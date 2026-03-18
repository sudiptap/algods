# Fibonacci Pattern

## Core Idea
Current state depends on a fixed number of previous states (usually 1-2).

## Template
```python
def solve(n):
    if n <= 1:
        return base_case
    prev2, prev1 = base0, base1
    for i in range(2, n + 1):
        curr = f(prev1, prev2)
        prev2, prev1 = prev1, curr
    return prev1
```

## Complexity
- Time: O(n)
- Space: O(1) with state compression, O(n) with full table

## Classic Problems
- 70. Climbing Stairs
- 198. House Robber
- 91. Decode Ways
- 509. Fibonacci Number
- 1137. N-th Tribonacci Number
