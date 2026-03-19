"""
3472. Longest Palindromic Subsequence After at Most K Operations
https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: LPS DP with budget for character changes.
- dp[i][j][k] = longest palindromic subsequence of s[i..j] using at most k operations.
- An operation changes a character to an adjacent one (cost 1 per step).
- To match s[i] and s[j], cost = min circular distance between s[i] and s[j] in alphabet.
  Actually, distance = min(|s[i]-s[j]|, 26 - |s[i]-s[j]|) since we can go either way.
- If cost <= remaining budget k, we can include both: dp[i+1][j-1] + 2 with k - cost.

Time: O(n^2 * k)  Space: O(n^2 * k)
---
"""


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i][j][b] = LPS length of s[i..j] with budget b
        # Too much memory if k is large. Let's limit.
        # k can be up to 200 based on constraints.

        # Use memoization
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j, b):
            if i > j:
                return 0
            if i == j:
                return 1
            res = max(dp(i + 1, j, b), dp(i, j - 1, b))
            diff = abs(ord(s[i]) - ord(s[j]))
            cost = min(diff, 26 - diff)
            if cost <= b:
                res = max(res, 2 + dp(i + 1, j - 1, b - cost))
            return res

        return dp(0, n - 1, k)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestPalindromicSubsequence("abced", 2) == 3
    assert sol.longestPalindromicSubsequence("aaazzz", 4) == 6  # cost 3*1 = need budget... actually cost per pair = min(25, 1)=1? no, a-z = 25, min(25,1)=1. All 3 pairs cost 1 each, total 3 <= 4.
    assert sol.longestPalindromicSubsequence("a", 0) == 1

    print("Solution: all tests passed")
