"""
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Pattern: 04 - Longest Common Subsequence (two-sequence alignment/matching)

---
APPROACH: 2D DP on (i, j) = can s[i:] be matched by p[j:]

Key insight: When we see 'x*' in the pattern, we have two choices:
  1. Skip it (match zero occurrences)  → dp[i][j] = dp[i][j+2]
  2. Use it (if current char matches)   → dp[i][j] = dp[i+1][j]
     (stay at j to allow more matches of the same char)

For '.' or exact char match without '*':
  dp[i][j] = dp[i+1][j+1]  (consume one char from both)

dp[i][j] = True means s[i:] matches p[j:]

Base case: dp[m][n] = True (both exhausted)

Time: O(m * n)  Space: O(m * n)
---
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = does s[i:] match p[j:]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True  # both strings exhausted

        # fill bottom-up: i from m down to 0, j from n-1 down to 0
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                # does s[i] match p[j]?
                first_match = i < m and p[j] in (s[i], '.')

                if j + 1 < n and p[j + 1] == '*':
                    # option 1: skip 'x*' entirely (zero occurrences)
                    # option 2: use 'x*' if first char matches (one+ occurrences)
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # no star: must match current char and advance both
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


# ---------- Approach 2: Top-down with memoization ----------
class SolutionMemo:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache
        m, n = len(s), len(p)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            # base: pattern exhausted
            if j == n:
                return i == m

            first_match = i < m and p[j] in (s[i], '.')

            if j + 1 < n and p[j + 1] == '*':
                # skip 'x*' OR consume one char and stay
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionMemo]:
        sol = Sol()

        # Example 1
        assert sol.isMatch("aa", "a") == False

        # Example 2
        assert sol.isMatch("aa", "a*") == True

        # Example 3
        assert sol.isMatch("ab", ".*") == True

        # Additional cases
        assert sol.isMatch("aab", "c*a*b") == True       # c* = empty, a* = aa
        assert sol.isMatch("mississippi", "mis*is*p*.") == False
        assert sol.isMatch("", "a*b*c*") == True          # all stars can be zero
        assert sol.isMatch("a", "ab*") == True             # b* = empty
        assert sol.isMatch("aaa", "a*a") == True           # a* = aa, then a

        print(f"{Sol.__name__}: all tests passed")
