"""
879. Profitable Schemes (Hard)
https://leetcode.com/problems/profitable-schemes/

There are n members in a gang. Given crimes described by group[i] (members
needed) and profit[i] (profit generated), count the number of subsets of
crimes (schemes) such that total members <= n and total profit >= minProfit.

Pattern: 0/1 Knapsack
Approach:
- dp[k][p] = number of ways to achieve exactly k members used and at least p profit.
- We cap p at minProfit (since any profit >= minProfit counts the same).
- For each crime, update dp in reverse order (0/1 knapsack style).
- Answer: sum of dp[k][minProfit] for k = 0..n.

Time:  O(len(group) * n * minProfit)
Space: O(n * minProfit)
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """Return number of profitable schemes modulo 10^9+7.

        Args:
            n: Max members available.
            minProfit: Minimum profit required.
            group: Members needed for each crime.
            profit: Profit for each crime.

        Returns:
            Count of subsets with total members <= n and profit >= minProfit.
        """
        # dp[k][p] = ways using exactly k members with min(profit_so_far, minProfit) == p
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            # Iterate in reverse to avoid using same crime twice
            for k in range(n, g - 1, -1):
                for pr in range(minProfit, -1, -1):
                    # New profit capped at minProfit
                    new_pr = min(pr + p, minProfit)
                    dp[k][new_pr] = (dp[k][new_pr] + dp[k - g][pr]) % MOD

        ans = 0
        for k in range(n + 1):
            ans = (ans + dp[k][minProfit]) % MOD
        return ans


# ---------- tests ----------
def test_profitable_schemes():
    sol = Solution()

    # Example 1: n=5, minProfit=3, group=[2,2], profit=[2,3]
    # Schemes: {1} profit=3>=3, {0,1} profit=5>=3 -> 2
    assert sol.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2

    # Example 2: n=10, minProfit=5, group=[2,3,5], profit=[6,7,8]
    assert sol.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7

    # No crimes available, minProfit=0 -> 1 (empty set)
    assert sol.profitableSchemes(5, 0, [], []) == 1

    # No crimes available, minProfit>0 -> 0
    assert sol.profitableSchemes(5, 1, [], []) == 0

    # Single crime, enough members
    assert sol.profitableSchemes(5, 3, [2], [5]) == 1

    print("All tests passed for 879. Profitable Schemes")


if __name__ == "__main__":
    test_profitable_schemes()
