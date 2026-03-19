"""
3844. Longest Almost-Palindromic Substring
https://leetcode.com/problems/longest-almost-palindromic-substring/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Expand around center with 1 mismatch allowance
- Almost-palindromic: becomes palindrome after removing exactly 1 character.
- For each center (odd and even), expand while characters match.
- When mismatch occurs, try skipping left or right char, continue expanding.
- Track maximum total length found.

Time: O(n^2)  Space: O(1)
---
"""


class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)

        def expand(l, r):
            """Expand around [l,r] as palindrome center, then allow 1 mismatch."""
            # First expand as far as possible with exact palindrome
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # Now s[l] != s[r] (or out of bounds)
            # The palindrome is s[l+1..r-1]. To make "almost palindromic",
            # we remove one character from the boundary.
            # Try removing s[l] (skip left) or s[r] (skip right) and continue.
            # Option 1: skip left side, continue from (l-1, r)
            l1, r1 = l - 1, r
            while l1 >= 0 and r1 < n and s[l1] == s[r1]:
                l1 -= 1
                r1 += 1
            # Option 2: skip right side, continue from (l, r+1)
            l2, r2 = l, r + 1
            while l2 >= 0 and r2 < n and s[l2] == s[r2]:
                l2 -= 1
                r2 += 1
            return min(n, max(r1 - l1 - 1, r2 - l2 - 1))

        ans = 0
        for i in range(n):
            ans = max(ans, expand(i, i))      # odd-length palindrome center
            ans = max(ans, expand(i, i + 1))   # even-length palindrome center
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.almostPalindromic("abca") == 4
    assert sol.almostPalindromic("abba") == 4
    assert sol.almostPalindromic("zzabba") == 5
    assert sol.almostPalindromic("ab") == 2  # remove either char -> palindrome

    print("all tests passed")
