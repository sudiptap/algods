"""
3573. Best Time to Buy and Sell Stock V
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

Pattern: 14 - State Machine DP

---
APPROACH: DP with hold/cooldown/ready states
- States: ready (can buy), hold (holding stock), cooldown (just sold, must wait).
- Transitions each day:
  - ready -> ready (do nothing) or ready -> hold (buy at price[i])
  - hold -> hold (do nothing) or hold -> cooldown (sell at price[i])
  - cooldown -> ready (wait one day)
- Maximize profit at end.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ready = 0
        hold = float('-inf')
        cooldown = float('-inf')

        for price in prices:
            new_ready = max(ready, cooldown)
            new_hold = max(hold, ready - price)
            new_cooldown = hold + price
            ready, hold, cooldown = new_ready, new_hold, new_cooldown

        return max(ready, cooldown)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3  # buy@1,sell@3,cooldown,buy@0,sell@2
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1]) == 0
    assert sol.maxProfit([1, 2, 4]) == 3

    print("All tests passed!")
