"""
2370. Longest Ideal Subsequence
https://leetcode.com/problems/longest-ideal-subsequence/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH:
dp[c] = length of the longest ideal subsequence ending with character c
        (where c is 0..25 for 'a'..'z').
For each character in the string, look at all characters within distance k
and take the max dp value, then add 1.

Time: O(n * k)  Space: O(26) = O(1)
---
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """Return the length of the longest ideal subsequence with gap <= k."""
        dp = [0] * 26

        for ch in s:
            c = ord(ch) - ord("a")
            lo = max(0, c - k)
            hi = min(25, c + k)
            best = 0
            for j in range(lo, hi + 1):
                if dp[j] > best:
                    best = dp[j]
            dp[c] = best + 1

        return max(dp)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: "acfgbd", k=2 -> 4 ("acbd")
    assert sol.longestIdealString("acfgbd", 2) == 4
    # Example 2: "abcd", k=3 -> 4 (whole string)
    assert sol.longestIdealString("abcd", 3) == 4
    # Single char
    assert sol.longestIdealString("a", 0) == 1
    # All same chars
    assert sol.longestIdealString("aaaa", 0) == 4
    # k=0 means only same chars allowed
    assert sol.longestIdealString("abab", 0) == 2
    # k=25 means any chars allowed (longest subsequence = whole string)
    assert sol.longestIdealString("azby", 25) == 4

    print("all tests passed")
