"""
1771. Maximize Palindrome Length From Subsequences
https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: LPS on concatenated string with constraint
- Concatenate word1 + word2 into s.
- Compute LPS (Longest Palindromic Subsequence) on s.
- Constraint: the palindrome must use at least one char from word1 and one from word2.
- When computing LPS dp[i][j], check if i < len(word1) and j >= len(word1)
  and s[i] == s[j] — this means both words contribute.
- Track the answer only when both contribute.

Time: O((m + n)^2) where m = len(word1), n = len(word2)
Space: O((m + n)^2)
---
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        m = len(word1)

        # Standard LPS DP
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        result = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
                    # Check if i is from word1 and j is from word2
                    if i < m and j >= m:
                        result = max(result, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return result


# --- Tests ---
def test():
    sol = Solution()

    assert sol.longestPalindrome("cacb", "cbba") == 5  # "abcba"
    assert sol.longestPalindrome("ab", "ab") == 3      # "aba" or "bab"
    assert sol.longestPalindrome("aa", "bb") == 0      # No common char for palindrome from both

    # Single chars
    assert sol.longestPalindrome("a", "a") == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
