"""
1143. Longest Common Subsequence (Medium)
https://leetcode.com/problems/longest-common-subsequence/

Pattern: 04 - Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest
common subsequence. If there is no common subsequence, return 0.

Approach:
    Classic 2D DP.  dp[i][j] = LCS length of text1[:i] and text2[:j].
    If chars match, dp[i][j] = dp[i-1][j-1] + 1.
    Otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]).

Time:  O(m * n)
Space: O(m * n)  —  can be optimized to O(min(m, n)) with 1D array.
"""

from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest common subsequence."""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3

def test_example2():
    assert Solution().longestCommonSubsequence("abc", "abc") == 3

def test_example3():
    assert Solution().longestCommonSubsequence("abc", "def") == 0

def test_single_char_match():
    assert Solution().longestCommonSubsequence("a", "a") == 1

def test_single_char_no_match():
    assert Solution().longestCommonSubsequence("a", "b") == 0

def test_empty_like():
    assert Solution().longestCommonSubsequence("a", "ab") == 1

def test_longer():
    assert Solution().longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
