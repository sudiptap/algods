"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Pattern: 08 - Palindromic Subsequence (Interval DP on substrings)

---
APPROACH 1: DP (Interval DP)
- dp[i][j] = True if s[i..j] is a palindrome
- Base: single chars are palindromes, two equal adjacent chars are palindromes
- Transition: s[i..j] is palindrome if s[i] == s[j] AND s[i+1..j-1] is palindrome
- Track the longest one found

Time: O(n^2)  Space: O(n^2)

APPROACH 2: Expand Around Center (optimal for interviews)
- Every palindrome has a center: single char (odd length) or between two chars (even length)
- For each center, expand outward while chars match
- 2n-1 possible centers, each expansion is O(n) worst case

Time: O(n^2)  Space: O(1)
---
"""


# ---------- Approach 1: DP ----------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # every single char is a palindrome
        for i in range(n):
            dp[i][i] = True

        # check substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    # length 2: just need matching chars
                    # length > 2: inner substring must also be palindrome
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_len:
                            start, max_len = i, length

        return s[start : start + max_len]


# ---------- Approach 2: Expand Around Center ----------
class SolutionExpand:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        start, max_len = 0, 1

        def expand(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # after loop: s[left+1..right-1] is the palindrome
            length = right - left - 1
            if length > max_len:
                start, max_len = left + 1, length

        for i in range(n):
            expand(i, i)      # odd-length palindromes
            expand(i, i + 1)  # even-length palindromes

        return s[start : start + max_len]


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionExpand]:
        sol = Sol()
        # Example 1
        result = sol.longestPalindrome("babad")
        assert result in ("bab", "aba"), f"Got {result}"

        # Example 2
        assert sol.longestPalindrome("cbbd") == "bb"

        # Edge cases
        assert sol.longestPalindrome("a") == "a"
        assert sol.longestPalindrome("ac") in ("a", "c")
        assert sol.longestPalindrome("racecar") == "racecar"

        print(f"{Sol.__name__}: all tests passed")
