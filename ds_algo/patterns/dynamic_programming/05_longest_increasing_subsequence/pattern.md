# Longest Increasing Subsequence (LIS) Pattern

## Core Idea
Find the longest subsequence where elements are in increasing order.

## Template (O(n log n) with patience sorting)
```python
import bisect

def lis(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

## Template (O(n^2) basic DP)
```python
def lis(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

## Complexity
- O(n log n) with binary search
- O(n^2) with basic DP

## Classic Problems
- 300. Longest Increasing Subsequence
- 354. Russian Doll Envelopes
- 673. Number of Longest Increasing Subsequence
- 1048. Longest String Chain
