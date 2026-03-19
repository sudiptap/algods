"""
1216. Valid Palindrome III (Hard)

Pattern: 08_palindromic_subsequence
- Check if string can become a palindrome by removing at most k characters.

Approach:
- dp[i][j] = minimum removals to make s[i..j] a palindrome.
- Base: dp[i][i] = 0, dp[i][i-1] = 0 (empty).
- Transition:
  - If s[i] == s[j]: dp[i][j] = dp[i+1][j-1]
  - Else: dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
- Answer: dp[0][n-1] <= k.
- Equivalently, min removals = n - LPS(s) where LPS = longest palindromic subsequence.

Complexity:
- Time:  O(n^2)
- Space: O(n^2), can be optimized to O(n)
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        if n <= 1:
            return True

        # dp[i][j] = min removals to make s[i..j] palindrome
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1] <= k


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: "abcdeca", k=2 -> remove 'b' and 'e' -> "acdca" palindrome
    assert sol.isValidPalindrome("abcdeca", 2) is True

    # Example 2: "abbababa", k=1
    assert sol.isValidPalindrome("abbababa", 1) is True

    # Already palindrome
    assert sol.isValidPalindrome("aba", 0) is True

    # Not possible
    assert sol.isValidPalindrome("abcde", 1) is False

    # Single char
    assert sol.isValidPalindrome("a", 0) is True

    # k large enough
    assert sol.isValidPalindrome("abcdef", 5) is True

    print("All tests passed!")


if __name__ == "__main__":
    test()
