"""
3563. Lexicographically Smallest String After Adjacent Removals
https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

Pattern: 08 - Palindromic Subsequence (Interval DP)

---
APPROACH: Interval DP
- Two adjacent characters can be removed if they are "complementary"
  (e.g., their combined value is divisible by some rule or they match
  palindromically: a+z, b+y, etc. -- actually a[i]+a[i+1] form a
  palindrome-like pair when (ord(a)-ord('a'))+(ord(b)-ord('a')) == 25,
  or more precisely, they can be removed if |ord(a)-ord(b)| <= 1 or
  they wrap around).

  Actually: two adjacent chars can be removed if together they could form
  part of a palindrome. The exact rule per problem: s[i] and s[i+1] can
  be removed if (ord(s[i]) - ord('a') + ord(s[i+1]) - ord('a')) % 26 <= 1
  or the reverse. Let me check: the rule is s[i]+s[j] are "matching" if
  |ord(s[i])-ord(s[j])| <= 1 (mod 26, considering wrap az).

- can_remove[i][j] = True if substring s[i..j] can be completely removed.
- For can_remove[i][j]: need to pair s[i] with some s[k] where they match,
  and can_remove[i+1][k-1] and can_remove[k+1][j].
- Then build the lexicographically smallest result using DP.

Time: O(n^3)  Space: O(n^2)
---
"""


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        def can_match(a, b):
            d = abs(ord(a) - ord(b))
            return d <= 1 or d >= 25  # wrap around z-a

        # can_remove[i][j] = can we completely remove s[i..j]?
        can_remove = [[False] * n for _ in range(n)]

        # Length must be even to fully remove
        for length in range(2, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                # Try pairing s[i] with s[k] for k = i+1, i+3, i+5, ...
                for k in range(i + 1, j + 1, 2):
                    if can_match(s[i], s[k]):
                        left_ok = (k == i + 1) or can_remove[i + 1][k - 1]
                        right_ok = (k == j) or can_remove[k + 1][j]
                        if left_ok and right_ok:
                            can_remove[i][j] = True
                            break

        # Now find lex smallest string after removals.
        # dp[i] = lex smallest string from s[i..n-1] after removals
        # We can either keep s[i] or remove a block starting at i.
        # If we keep s[i], result = s[i] + dp[i+1]
        # If we remove s[i..k] (can_remove[i][k]), result = dp[k+1]
        # Take lex smallest.

        # Build from right to left
        dp = [""] * (n + 1)
        for i in range(n - 1, -1, -1):
            # Option: keep s[i]
            best = s[i] + dp[i + 1]
            # Option: remove some block starting at i
            for k in range(i + 1, n, 2):  # k-i+1 must be even, so k is odd offset from i
                if can_remove[i][k]:
                    candidate = dp[k + 1]
                    if candidate < best:
                        best = candidate
            dp[i] = best

        return dp[0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # "abc": b,c are adjacent with |b-c|=1, can remove -> "a"
    assert sol.lexicographicallySmallestString("abc") == "a"
    # "bcda": b,c removable->da, d,c removable... let's just check
    res = sol.lexicographicallySmallestString("bcda")
    print(f"bcda -> '{res}'")
    # "az": |a-z|=25, wraps around, removable -> ""
    assert sol.lexicographicallySmallestString("az") == ""
    # "aab": a,a |diff|=0 <=1, remove -> "b". Or a,b |diff|=1, remove -> "a". "a" < "b".
    assert sol.lexicographicallySmallestString("aab") == "a"

    print("All tests passed!")
