"""
3441. Minimum Cost Good Caption
https://leetcode.com/problems/minimum-cost-good-caption/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: DP on grouping into blocks of >= 3 consecutive same characters.
- A "good caption" has every character in a run of >= 3 identical chars.
- We can increment/decrement characters (cost 1 per step).
- dp[i] = min cost to make s[0..i-1] good.
- For each position i, try blocks of length L = 3, 4, 5 ending at i.
  (Longer blocks can be decomposed into 3/4/5 without increasing cost.)
- For each block, find char with min total distance, then lex smallest among ties.

Time: O(26 * n)  Space: O(n)
---
"""


class Solution:
    def minimumCost(self, s: str) -> str:
        n = len(s)
        if n < 3:
            return ""

        INF = float('inf')
        # dp[i] = (min_cost, string) for s[0..i-1]
        dp = [(INF, "")] * (n + 1)
        dp[0] = (0, "")

        for i in range(3, n + 1):
            for L in range(3, min(6, i + 1)):
                j = i - L
                if dp[j][0] == INF and j > 0:
                    continue
                chars = [ord(s[t]) - ord('a') for t in range(j, i)]

                # Find min cost char and lex smallest among ties
                best_cost = INF
                for c in range(26):
                    cost = sum(abs(ch - c) for ch in chars)
                    if cost < best_cost:
                        best_cost = cost

                total = dp[j][0] + best_cost
                if total > dp[i][0]:
                    continue

                for c in range(26):
                    cost = sum(abs(ch - c) for ch in chars)
                    if cost == best_cost:
                        candidate = dp[j][1] + chr(c + ord('a')) * L
                        if total < dp[i][0] or candidate < dp[i][1]:
                            dp[i] = (total, candidate)
                        break

        return dp[n][1] if dp[n][0] < INF else ""


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumCost("cdcd") == "cccc"
    assert sol.minimumCost("ab") == ""
    assert sol.minimumCost("aaa") == "aaa"
    assert sol.minimumCost("abcabc") == "bbbbbb"

    print("Solution: all tests passed")
