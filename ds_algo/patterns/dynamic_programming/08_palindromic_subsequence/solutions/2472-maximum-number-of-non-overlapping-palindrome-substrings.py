"""
2472. Maximum Number of Non-overlapping Palindrome Substrings
https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Precompute palindromes, greedy/DP
- dp[i] = max non-overlapping palindromic substrings in s[:i] each of length >= k.
- Precompute is_pal[i][j] = whether s[i..j] is a palindrome using expand-from-center
  or DP.
- dp[i] = max(dp[i-1], dp[j] + 1) for all j where s[j..i-1] is a palindrome and
  i-j >= k.
- Optimization: only need to check length k and k+1 (if a longer palindrome exists,
  it contains a shorter one of length k or k+1 centered similarly).

Time: O(n * k)  Space: O(n)
---
"""


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # dp[i] = max palindromes in s[:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            # Check palindromes ending at i-1 of length k and k+1
            for length in [k, k + 1]:
                j = i - length
                if j >= 0 and is_palindrome(j, i - 1):
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxPalindromes("abaccdbbd", 3) == 2
    assert sol.maxPalindromes("adbcda", 2) == 0
    assert sol.maxPalindromes("aa", 1) == 2
    assert sol.maxPalindromes("abab", 2) == 1

    print("all tests passed")
