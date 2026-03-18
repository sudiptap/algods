# Palindromic Subsequence Pattern

## Core Idea
LCS of a string with its reverse gives the longest palindromic subsequence. Or use interval DP on [i, j].

## Template
```python
def longest_palindromic_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
```

## Complexity
- Time: O(n^2)
- Space: O(n^2), reducible to O(n)

## Classic Problems
- 516. Longest Palindromic Subsequence
- 1312. Minimum Insertion Steps to Make a String Palindrome
- 5. Longest Palindromic Substring
- 647. Palindromic Substrings
