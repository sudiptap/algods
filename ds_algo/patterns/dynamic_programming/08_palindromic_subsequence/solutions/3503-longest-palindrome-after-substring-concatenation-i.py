"""
3503. Longest Palindrome After Substring Concatenation I
https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Check all pairs of substrings.
- Try all substrings of s (s[i..j]) and all substrings of t (t[k..l]).
- Concatenate them and check if the result is a palindrome.
- Track maximum length.
- Also consider using only s or only t.

Time: O(n^2 * m^2 * (n+m))  Space: O(n+m)
---
"""


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(x):
            return x == x[::-1]

        n, m = len(s), len(t)
        ans = 0

        # Try all substrings of s concatenated with all substrings of t
        for i in range(n):
            for j in range(i, n):
                # s[i..j] alone
                sub_s = s[i:j + 1]
                if is_palindrome(sub_s):
                    ans = max(ans, len(sub_s))
                # s[i..j] + t[k..l]
                for k in range(m):
                    for l in range(k, m):
                        concat = sub_s + t[k:l + 1]
                        if is_palindrome(concat):
                            ans = max(ans, len(concat))

        # Also substrings of t alone
        for k in range(m):
            for l in range(k, m):
                sub_t = t[k:l + 1]
                if is_palindrome(sub_t):
                    ans = max(ans, len(sub_t))

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestPalindrome("a", "a") == 2
    assert sol.longestPalindrome("abc", "def") == 1
    assert sol.longestPalindrome("b", "aaaa") == 4
    assert sol.longestPalindrome("abcde", "ecdba") == 5

    print("Solution: all tests passed")
