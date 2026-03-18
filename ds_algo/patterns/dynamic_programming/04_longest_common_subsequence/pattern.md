# Longest Common Subsequence (LCS) Pattern

## Core Idea
Compare two sequences. If characters match, extend from diagonal. Otherwise, take the best of skipping either character.

## Template
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

## Complexity
- Time: O(m * n)
- Space: O(n) with rolling array

## Classic Problems
- 1143. Longest Common Subsequence
- 72. Edit Distance
- 583. Delete Operation for Two Strings
- 712. Minimum ASCII Delete Sum
- 97. Interleaving String
