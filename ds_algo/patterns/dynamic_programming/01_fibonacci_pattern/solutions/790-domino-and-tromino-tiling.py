"""
790. Domino and Tromino Tiling
https://leetcode.com/problems/domino-and-tromino-tiling/

Pattern: 01 - Fibonacci Pattern

---
APPROACH: The recurrence dp[n] = 2*dp[n-1] + dp[n-3].
- dp[i] = number of ways to tile a 2 x i board with dominoes and trominoes
- Base cases: dp[0] = 1 (empty board), dp[1] = 1, dp[2] = 2
- The 2*dp[n-1] accounts for adding a vertical domino or an L-tromino pair,
  and dp[n-3] accounts for the additional new tromino arrangements.
- Result modulo 10^9 + 7.

Time: O(n)  Space: O(1)
---
"""

MOD = 10**9 + 7


class Solution:
    def numTilings(self, n: int) -> int:
        """Return number of ways to tile a 2 x n board with dominoes and trominoes."""
        if n <= 2:
            return n if n >= 1 else 1  # dp[0]=1, dp[1]=1, dp[2]=2

        # dp[0] = 1, dp[1] = 1, dp[2] = 2
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numTilings(1) == 1
    assert sol.numTilings(2) == 2
    assert sol.numTilings(3) == 5
    assert sol.numTilings(4) == 11
    assert sol.numTilings(5) == 24
    # Large n to verify modular arithmetic
    assert sol.numTilings(1000) == 979232805

    print("all tests passed")
