"""
115. Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Pattern: 04 - Longest Common Subsequence (two-sequence counting)

---
APPROACH: 1D DP (space-optimized)
- dp[j] = number of ways to form t[:j] from s[:i] (as we scan s)
- If s[i-1] == t[j-1]: dp[j] = dp[j] + dp[j-1]
    → dp[j] (skip s[i-1]) + dp[j-1] (use s[i-1] to match t[j-1])
- If s[i-1] != t[j-1]: dp[j] = dp[j]
    → can only skip s[i-1]
- Scan j RIGHT TO LEFT to avoid overwriting dp[j-1] before using it
  (same trick as 0/1 knapsack)

Base: dp[0] = 1 (empty t is a subsequence of anything)

Time: O(m*n)  Space: O(n)
---
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # empty t matches any prefix of s

        for i in range(1, m + 1):
            # scan right to left so dp[j-1] is still from previous i
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                # else: dp[j] stays the same (skip s[i-1])

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numDistinct("rabbbit", "rabbit") == 3
    assert sol.numDistinct("babgbag", "bag") == 5
    assert sol.numDistinct("a", "a") == 1
    assert sol.numDistinct("a", "b") == 0
    assert sol.numDistinct("aaa", "a") == 3
    assert sol.numDistinct("", "a") == 0
    assert sol.numDistinct("abc", "") == 1

    print("all tests passed")
