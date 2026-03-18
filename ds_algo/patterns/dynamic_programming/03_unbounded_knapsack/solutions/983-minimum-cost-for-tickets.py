"""
983. Minimum Cost For Tickets
https://leetcode.com/problems/minimum-cost-for-tickets/

Pattern: 03 - Unbounded Knapsack

---
APPROACH: DP over calendar days
- dp[d] = min cost to cover all travel days up to day d.
- If day d is not a travel day, dp[d] = dp[d-1] (no ticket needed).
- If day d is a travel day, take the minimum of:
    dp[d-1] + costs[0]   (buy 1-day pass)
    dp[d-7] + costs[1]   (buy 7-day pass — covers back 7 days)
    dp[d-30] + costs[2]  (buy 30-day pass — covers back 30 days)
  where dp[x] = 0 for x <= 0.

Time: O(max_day)  Space: O(max_day)  — at most 365
---
"""

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """Return minimum cost to travel on every day in `days`."""
        travel = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for d in range(1, last_day + 1):
            if d not in travel:
                dp[d] = dp[d - 1]
            else:
                dp[d] = min(
                    dp[max(0, d - 1)] + costs[0],
                    dp[max(0, d - 7)] + costs[1],
                    dp[max(0, d - 30)] + costs[2],
                )

        return dp[last_day]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
    assert sol.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
                              [2, 7, 15]) == 17
    assert sol.mincostTickets([1], [1, 5, 10]) == 1
    assert sol.mincostTickets([1, 365], [2, 7, 15]) == 4
    assert sol.mincostTickets([1, 2, 3, 4, 5, 6, 7], [2, 7, 15]) == 7

    print("all tests passed")
