"""
1682. Longest Palindromic Subsequence II
https://leetcode.com/problems/longest-palindromic-subsequence-ii/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: LPS with constraint that no two adjacent chars are same
- dp[i][j][last] = length of longest palindromic subsequence in s[i..j]
  where the last character added to the palindrome's outer layer is 'last'.
- When s[i] == s[j] and s[i] != last, extend: dp[i][j][last] = max dp[i+1][j-1][s[i]] + 2
- Otherwise try skipping i or j.
- Use character index (0-25) for 'last', 26 = no last character yet.

Time: O(n^2 * 26)
Space: O(n^2 * 26)
---
"""

from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(i, j, last):
            if i >= j:
                return 0
            if s[i] == s[j] and s[i] != last:
                return dp(i + 1, j - 1, s[i]) + 2
            return max(dp(i + 1, j, last), dp(i, j - 1, last))

        return dp(0, n - 1, '#')


# --- Tests ---
def test():
    sol = Solution()

    assert sol.longestPalindromeSubseq("bbabab") == 4  # "bab" or "bab" -> "abba" = 4
    assert sol.longestPalindromeSubseq("dcbccacdb") == 4
    assert sol.longestPalindromeSubseq("a") == 0  # Single char, need pairs
    assert sol.longestPalindromeSubseq("aa") == 2
    assert sol.longestPalindromeSubseq("aaa") == 2  # Can only use "aa" since no adjacent same

    print("All tests passed!")


if __name__ == "__main__":
    test()
