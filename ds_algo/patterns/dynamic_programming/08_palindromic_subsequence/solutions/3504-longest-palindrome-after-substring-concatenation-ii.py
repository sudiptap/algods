"""
3504. Longest Palindrome After Substring Concatenation II
https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Optimized palindrome check using DP.
- Precompute palindrome extension for matching prefixes of s with reversed suffixes of t.
- For each suffix s[i..] and prefix t[..j], find max matching length.
- Then extend with longest palindromic substring in the remaining middle.
- Use LPS-style matching between s and reverse(t).

Time: O(n*m + n^2 + m^2)  Space: O(n*m)
---
"""


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        t_rev = t[::-1]

        # Precompute: for each (i, j), max length L such that s[i:i+L] == t_rev[j:j+L]
        # i.e., s[i..i+L-1] matches reverse of t ending at some position
        # match[i][j] = length of common prefix of s[i:] and t_rev[j:]
        match = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t_rev[j]:
                    match[i][j] = match[i + 1][j + 1] + 1

        # Precompute longest palindromic substring starting at each position in s
        # and ending at each position in t_rev (or equivalently, in s remaining / t remaining)

        # For a palindrome formed by s[i..i+L-1] + middle_palindrome + t_rev[j..j+L-1]:
        # Actually the concatenation is s[i..x] + t[y..z] and the result is palindrome.
        # s[i..x] + t[y..z] being palindrome means:
        #   s[i..i+L-1] matches reverse(t[z-L+1..z]) and the middle is a palindrome.

        # Better approach: for each matching length L between s[i:i+L] and t_rev[j:j+L]:
        #   The palindrome is s[i..i+L-1] + (palindrome extension in s or t) + reverse of s[i..i+L-1]
        #   But reverse of s[i..i+L-1] = t[m-1-j..m-1-j+L-1] since s[i..i+L-1] = t_rev[j..j+L-1].

        # Precompute: longest palindrome starting at position p in s (i.e., s[p..q] is palindrome)
        # and longest palindrome ending at position p in t_rev.

        # pal_s[i] = length of longest palindromic substring starting at index i in s
        pal_s = [1] * n
        # pal_t[j] = length of longest palindromic substring starting at index j in t_rev
        pal_t = [1] * m

        # Compute using expand-around-center
        def longest_pal_starting(string):
            sz = len(string)
            res = [1] * sz
            for center in range(sz):
                # Odd length
                lo, hi = center, center
                while lo >= 0 and hi < sz and string[lo] == string[hi]:
                    if lo == center or True:  # update starting positions
                        res[lo] = max(res[lo], hi - lo + 1)
                    lo -= 1
                    hi += 1
                # Even length
                lo, hi = center, center + 1
                while lo >= 0 and hi < sz and string[lo] == string[hi]:
                    res[lo] = max(res[lo], hi - lo + 1)
                    lo -= 1
                    hi += 1
            return res

        pal_s = longest_pal_starting(s)
        pal_t = longest_pal_starting(t_rev)

        ans = max(max(pal_s), max(pal_t))

        # For each pair (i in s, j in t_rev) with match[i][j] = L > 0:
        # We can form: s[i..i+L-1] + palindrome_middle + t_rev[j+L-1..j] (reversed back = t piece)
        # Total length = 2*L + palindrome_middle_length
        # The middle must come from s[i+L..] or t_rev[..j-1], specifically:
        #   If we take more from s: palindromic substring starting at s[i+L], length = pal_s[i+L]
        #   If we take more from t_rev: palindromic substring starting at t_rev[j+L], length = pal_t[j+L]
        # But actually we concatenate s_substring + t_substring, so the "middle" is either:
        #   More of s after the matching part, or more of t_rev after the matching part.

        for i in range(n):
            for j in range(m):
                L = match[i][j]
                if L > 0:
                    # Use exactly L characters from each side
                    for use_L in range(1, L + 1):
                        extra = 0
                        if i + use_L < n:
                            extra = max(extra, pal_s[i + use_L])
                        if j + use_L < m:
                            extra = max(extra, pal_t[j + use_L])
                        ans = max(ans, 2 * use_L + extra)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestPalindrome("a", "a") == 2
    assert sol.longestPalindrome("abc", "def") == 1
    assert sol.longestPalindrome("b", "aaaa") == 4
    assert sol.longestPalindrome("abcde", "ecdba") == 5

    print("Solution: all tests passed")
