"""
1312. Minimum Insertion Steps to Make a String Palindrome (Hard)
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: n - LPS (Longest Palindromic Subsequence)
- The minimum insertions to make s a palindrome equals
  len(s) - LPS(s).
- LPS is computed via standard DP on s and reverse(s) (LCS variant).
- Alternatively, interval DP: dp[i][j] = min insertions for s[i..j].
  dp[i][j] = 0 if i >= j
  dp[i][j] = dp[i+1][j-1] if s[i] == s[j]
  dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1 otherwise

Here we use the LPS approach for clarity.

Time:  O(n^2)
Space: O(n^2), reducible to O(n)
---
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        """Return the minimum number of insertions to make s a palindrome."""
        n = len(s)
        t = s[::-1]

        # Compute LCS(s, reverse(s)) = LPS(s) using O(n) space
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        lps = prev[n]
        return n - lps


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minInsertions("zzazz") == 0

    # Example 2
    assert sol.minInsertions("mbadm") == 2

    # Example 3
    assert sol.minInsertions("leetcode") == 5

    # Single char
    assert sol.minInsertions("a") == 0

    # Two same chars
    assert sol.minInsertions("aa") == 0

    # Two different chars
    assert sol.minInsertions("ab") == 1

    # Already palindrome
    assert sol.minInsertions("racecar") == 0

    print("all tests passed")
