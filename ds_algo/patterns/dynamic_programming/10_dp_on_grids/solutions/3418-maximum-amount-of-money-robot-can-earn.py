"""
3418. Maximum Amount of Money Robot Can Earn
https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

Pattern: 10 - DP on Grids

---
APPROACH: Grid DP with k neutralizations.
- dp[i][j][k] = max money reaching (i,j) having used k neutralizations.
- Transition: from (i-1,j) or (i,j-1), either collect coins[i][j] or neutralize (if negative and k > 0).

Time: O(m * n * 3)  Space: O(m * n * 3)
---
"""

from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')

        # dp[i][j][k] = max money at (i,j) with k neutralizations used (k=0,1,2)
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]

        # Base case
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # neutralize first cell

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    # Best value arriving at (i,j) before deciding
                    prev = NEG_INF
                    if i > 0 and dp[i - 1][j][k] != NEG_INF:
                        prev = max(prev, dp[i - 1][j][k])
                    if j > 0 and dp[i][j - 1][k] != NEG_INF:
                        prev = max(prev, dp[i][j - 1][k])

                    if prev != NEG_INF:
                        # Collect coins[i][j]
                        dp[i][j][k] = max(dp[i][j][k], prev + coins[i][j])

                    # Neutralize coins[i][j] (use one more neutralization)
                    if k > 0 and coins[i][j] < 0:
                        prev2 = NEG_INF
                        if i > 0 and dp[i - 1][j][k - 1] != NEG_INF:
                            prev2 = max(prev2, dp[i - 1][j][k - 1])
                        if j > 0 and dp[i][j - 1][k - 1] != NEG_INF:
                            prev2 = max(prev2, dp[i][j - 1][k - 1])
                        if prev2 != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], prev2)

        return max(dp[m - 1][n - 1])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumAmount([[0, 1, -1], [1, -2, 3], [2, -3, 4]]) == 8
    assert sol.maximumAmount([[10, 10, 10], [10, 10, 10]]) == 40

    print("Solution: all tests passed")
