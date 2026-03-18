"""
132. Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Expand Around Center + DP for min cuts
- dp[i] = minimum number of cuts needed for s[:i] (first i characters)
- Base: dp[0] = -1 (empty string needs -1 cuts so that a single palindrome = 0 cuts)
- For each center, expand outward. When s[l..r] is a palindrome,
  dp[r+1] = min(dp[r+1], dp[l] + 1)
- This avoids building a full O(n^2) palindrome table.

Why expand around center?
- Each palindrome substring s[l..r] means we can take s[:l] (needing dp[l] cuts)
  and append s[l..r] as one more piece, so dp[r+1] = dp[l] + 1.
- Expanding from every center covers all palindromic substrings.

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # dp[i] = min cuts for s[:i]
        # Initialize dp[i] = i - 1 (worst case: every char is its own partition)
        dp = list(range(-1, n))  # dp[0]=-1, dp[1]=0, dp[2]=1, ...

        for center in range(n):
            # Odd-length palindromes: expand around single center
            l, r = center, center
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

            # Even-length palindromes: expand around center pair
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: "aab" -> "aa" | "b" -> 1 cut
    assert sol.minCut("aab") == 1, f"Got {sol.minCut('aab')}"

    # Example 2: "a" -> already palindrome -> 0 cuts
    assert sol.minCut("a") == 0

    # Example 3: "ab" -> "a" | "b" -> 1 cut
    assert sol.minCut("ab") == 1

    # Already a palindrome
    assert sol.minCut("racecar") == 0

    # Worst case: all different chars
    assert sol.minCut("abcd") == 3

    # Repeated chars
    assert sol.minCut("aaaa") == 0

    # Mixed palindromes
    assert sol.minCut("abba") == 0  # entire string is palindrome

    # Longer example
    assert sol.minCut("ababbbabbababa") == 3

    print("Solution: all tests passed")
