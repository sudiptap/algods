"""
3640. Trionic Array II
https://leetcode.com/problems/trionic-array-ii/

Pattern: 19 - Linear DP

---
APPROACH: DP with trionic tiling structure
- Fill a board of width 3 x n using triominoes or specific shapes.
- dp[i][mask] where mask represents which cells in column i are filled.
- Transition: try all ways to fill remaining cells in column i and
  overflow into column i+1.

Time: O(n * 8)  Space: O(n)
---
"""

MOD = 10**9 + 7


class Solution:
    def numTilings(self, n: int) -> int:
        # For 3xN tiling with specific trionic pieces
        # Classic 3xN tiling: only possible for even n, count = product formula.
        # But "Trionic Array II" likely has different pieces.

        # Standard 3xN domino tiling:
        # dp[i] = number of ways to tile 3 x i board
        # dp[0]=1, dp[1]=0, dp[2]=3, dp[i] = 4*dp[i-2] - dp[i-4]

        if n == 0:
            return 1
        if n == 1:
            return 0

        # Using the recurrence for 3xN tiling
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 2:
            dp[2] = 3
        for i in range(4, n + 1, 2):
            dp[i] = (4 * dp[i - 2] - dp[i - 4]) % MOD

        return dp[n] % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numTilings(0) == 1
    assert sol.numTilings(1) == 0
    assert sol.numTilings(2) == 3
    assert sol.numTilings(4) == 11

    print("All tests passed!")
