"""
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/

Pattern: 04 - Longest Common Subsequence (two-sequence matching)

Compare with #10 (Regex Matching):
- #10: '*' means zero or more of the PRECEDING element (tied to prev char)
- #44: '*' matches any sequence independently (much simpler wildcard)

---
APPROACH 1: 2D DP
- dp[i][j] = does s[:i] match p[:j]?
- Base: dp[0][0] = True, dp[0][j] = True only if p[:j] is all '*'
- Transitions:
    p[j-1] == '*':  dp[i][j] = dp[i-1][j]   (star eats one char from s)
                              OR dp[i][j-1]   (star matches empty)
    p[j-1] == '?' or p[j-1] == s[i-1]:
                     dp[i][j] = dp[i-1][j-1]  (consume both)

Time: O(m*n)  Space: O(m*n), optimizable to O(n)

APPROACH 2: 1D DP (space-optimized)
- Only need previous row → single array with careful update order

Time: O(m*n)  Space: O(n)
---
"""


# ---------- Approach 1: 2D DP ----------
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # first row: s is empty, only leading '*' can match
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # star matches empty (dp[i][j-1]) OR eats one char (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


# ---------- Approach 2: 1D DP ----------
class SolutionOptimized:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True

        # base row: empty s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]

        for i in range(1, m + 1):
            new_dp = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    new_dp[j] = new_dp[j - 1] or dp[j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    new_dp[j] = dp[j - 1]
            dp = new_dp

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionOptimized]:
        sol = Sol()

        assert sol.isMatch("aa", "a") == False
        assert sol.isMatch("aa", "*") == True
        assert sol.isMatch("cb", "?a") == False
        assert sol.isMatch("adceb", "*a*b") == True
        assert sol.isMatch("acdcb", "a*c?b") == False
        assert sol.isMatch("", "") == True
        assert sol.isMatch("", "*") == True
        assert sol.isMatch("", "***") == True
        assert sol.isMatch("abc", "a*c") == True
        assert sol.isMatch("abc", "a**c") == True  # consecutive stars

        print(f"{Sol.__name__}: all tests passed")
