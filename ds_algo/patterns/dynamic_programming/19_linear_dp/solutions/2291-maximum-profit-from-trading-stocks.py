"""
2291. Maximum Profit From Trading Stocks
https://leetcode.com/problems/maximum-profit-from-trading-stocks/

Pattern: 19 - Linear DP (0/1 Knapsack)

---
APPROACH: 0/1 knapsack where dp[j] = max profit with budget j
- For each stock i, cost = present[i], gain = future[i] - present[i].
- Only buy if gain > 0 and cost <= budget.
- dp[j] = max profit using exactly j budget.
- Transition: dp[j] = max(dp[j], dp[j - present[i]] + future[i] - present[i])
- Process stocks in outer loop, budget in reverse (0/1 knapsack).

Time: O(n * budget)  Space: O(budget)
---
"""

from typing import List


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget + 1)

        for i in range(len(present)):
            cost = present[i]
            profit = future[i] - present[i]
            if profit <= 0 or cost > budget:
                continue
            for j in range(budget, cost - 1, -1):
                dp[j] = max(dp[j], dp[j - cost] + profit)

        return dp[budget]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumProfit([5, 4, 6, 2, 3], [8, 5, 4, 3, 5], 10) == 6
    assert sol.maximumProfit([2, 2, 5], [3, 4, 10], 6) == 5
    assert sol.maximumProfit([3, 3, 12], [0, 3, 15], 10) == 0
    assert sol.maximumProfit([1], [2], 0) == 0

    print("all tests passed")
