"""
516. Longest Palindromic Subsequence (Medium)
https://leetcode.com/problems/longest-palindromic-subsequence/

Pattern: Palindromic Subsequence

Given a string s, find the length of its longest palindromic subsequence.

Approach:
    dp[i][j] = length of LPS in s[i..j].
    If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
    Else:            dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    Base case: dp[i][i] = 1 (single char is a palindrome).
    Fill diagonally (increasing gap length).

Time:  O(n^2)
Space: O(n^2)
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Return the length of the longest palindromic subsequence in s."""
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().longestPalindromeSubseq("bbbab") == 4

def test_example2():
    assert Solution().longestPalindromeSubseq("cbbd") == 2

def test_single_char():
    assert Solution().longestPalindromeSubseq("a") == 1

def test_palindrome():
    assert Solution().longestPalindromeSubseq("racecar") == 7

def test_all_same():
    assert Solution().longestPalindromeSubseq("aaaa") == 4

def test_no_repeat():
    assert Solution().longestPalindromeSubseq("abcde") == 1

def test_two_chars_same():
    assert Solution().longestPalindromeSubseq("aa") == 2

def test_two_chars_diff():
    assert Solution().longestPalindromeSubseq("ab") == 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
