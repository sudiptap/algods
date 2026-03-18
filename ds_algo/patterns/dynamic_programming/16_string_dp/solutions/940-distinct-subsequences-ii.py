"""
940. Distinct Subsequences II
https://leetcode.com/problems/distinct-subsequences-ii/

Pattern: 16 - String DP

---
APPROACH: DP tracking last occurrence of each character
- dp[i] = number of distinct non-empty subsequences considering s[0..i-1]
- When we add character s[i], every existing subsequence can be extended by s[i],
  plus s[i] alone. So dp[i] = 2 * dp[i-1] + 1.
- But if s[i] appeared before at index j, the subsequences counted at dp[j-1]
  (plus 1 for s[j] alone) were already extended by the same character, creating
  duplicates. Subtract dp[j-1] + 1 to remove them.
- Track last occurrence of each character to know what to subtract.

Time: O(n)  Space: O(n) — can be optimized to O(1) with rolling variable
---
"""

MOD = 10**9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """Return the number of distinct non-empty subsequences of s, mod 10^9+7."""
        n = len(s)
        dp = [0] * (n + 1)
        # dp[i] = number of distinct non-empty subsequences using s[0..i-1]
        last = {}  # char -> last index (1-indexed) where it appeared

        for i in range(1, n + 1):
            c = s[i - 1]
            dp[i] = (2 * dp[i - 1] + 1) % MOD

            if c in last:
                j = last[c]
                dp[i] = (dp[i] - dp[j - 1] - 1) % MOD

            last[c] = i

        return dp[n] % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.distinctSubseqII("abc") == 7         # a,b,c,ab,ac,bc,abc
    assert sol.distinctSubseqII("aba") == 6          # a,b,ab,ba,aa,aba
    assert sol.distinctSubseqII("aaa") == 3          # a, aa, aaa
    assert sol.distinctSubseqII("a") == 1
    assert sol.distinctSubseqII("ab") == 3           # a, b, ab
    assert sol.distinctSubseqII("lee") == 5          # l,e,le,ee,lee
    assert sol.distinctSubseqII("aab") == 5          # a,aa,b,ab,aab

    print("all tests passed")
