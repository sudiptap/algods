"""
730. Count Different Palindromic Subsequences (Hard)

Given a string s, return the number of different non-empty palindromic
subsequences in s. The answer may be very large, return it modulo 10^9 + 7.

Pattern: Palindromic Subsequence DP
- dp[i][j] = number of distinct palindromic subsequences in s[i..j].
- When s[i] != s[j]: dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
  (inclusion-exclusion to avoid double counting the overlap).
- When s[i] == s[j]: find the innermost occurrences of s[i] within (i, j).
  - No duplicate of s[i] inside: dp[i][j] = dp[i+1][j-1] * 2 + 2
    (wrap every inner palindrome + add "aa" and "a")
  - Exactly one duplicate inside: dp[i][j] = dp[i+1][j-1] * 2 + 1
    ("a" already counted inside)
  - Two or more duplicates: dp[i][j] = dp[i+1][j-1] * 2 - dp[lo+1][hi-1]
    (subtract palindromes between the inner duplicate pair, already counted)

Time:  O(n^2)
Space: O(n^2)
"""

MOD = 10**9 + 7


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """Return count of distinct non-empty palindromic subsequences mod 10^9+7."""
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] != s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else:
                    # Find innermost matching characters
                    lo, hi = i + 1, j - 1
                    while lo <= hi and s[lo] != s[i]:
                        lo += 1
                    while hi >= lo and s[hi] != s[i]:
                        hi -= 1

                    if lo > hi:
                        # No duplicate of s[i] inside (i, j)
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif lo == hi:
                        # Exactly one duplicate of s[i] inside
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        # Two or more duplicates inside
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[lo + 1][hi - 1]

                dp[i][j] = dp[i][j] % MOD

        return dp[0][n - 1] % MOD


# ----------------- Tests -----------------
def run_tests():
    sol = Solution()

    # Example 1: "bccb" -> "b", "c", "bb", "cc", "bcb", "bccb"
    assert sol.countPalindromicSubsequences("bccb") == 6, "Test 1 failed"

    # Example 2
    assert sol.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361, "Test 2 failed"

    # Single character
    assert sol.countPalindromicSubsequences("a") == 1, "Test 3 failed"

    # Two same characters: "a", "aa"
    assert sol.countPalindromicSubsequences("aa") == 2, "Test 4 failed"

    # Two different characters: "a", "b"
    assert sol.countPalindromicSubsequences("ab") == 2, "Test 5 failed"

    # "aab" -> "a", "b", "aa", "aab" has palindromic subseq: a, b, aa = 3
    assert sol.countPalindromicSubsequences("aab") == 3, "Test 6 failed"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
