"""
2318. Number of Distinct Roll Sequences
https://leetcode.com/problems/number-of-distinct-roll-sequences/

Pattern: 14 - State Machine DP

---
APPROACH: dp[i][last][second_last] with constraints
- Cannot roll same number twice in a row.
- Cannot roll same number within distance 2 (last and second_last must differ from current).
- GCD(current, last) must be 1.
- dp[i][a][b] = number of sequences of length i ending in (..., b, a).
- Transition: dp[i+1][c][a] += dp[i][a][b] if c != a, c != b, gcd(c, a) == 1.

Time: O(n * 6^3)  Space: O(6^2) with space optimization
---
"""

from math import gcd


class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 6

        # dp[last][second_last] = count
        # Use 0 as sentinel for "no second_last" (first position)
        dp = [[0] * 7 for _ in range(7)]

        # Initialize length 2
        for a in range(1, 7):
            for b in range(1, 7):
                if a != b and gcd(a, b) == 1:
                    dp[a][b] = 1

        for length in range(3, n + 1):
            new_dp = [[0] * 7 for _ in range(7)]
            for a in range(1, 7):  # current last
                for b in range(1, 7):  # current second_last
                    if a == b or gcd(a, b) != 1:
                        continue
                    # a is the new roll, b was the last, c was second_last
                    # We need sequences ending in (c, b) and now we append a
                    # a != b (checked), a != c, gcd(a, b) == 1 (checked)
                    for c in range(1, 7):
                        if a != c and dp[b][c] > 0:
                            new_dp[a][b] = (new_dp[a][b] + dp[b][c]) % MOD
            dp = new_dp

        ans = 0
        for a in range(1, 7):
            for b in range(1, 7):
                ans = (ans + dp[a][b]) % MOD

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.distinctSequences(4) == 184
    assert sol.distinctSequences(2) == 22
    assert sol.distinctSequences(1) == 6

    print("all tests passed")
