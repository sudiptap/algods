"""
309. Best Time to Buy and Sell Stock with Cooldown (Medium)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You may complete as many transactions as you like (buy then sell one share)
with the restriction that after you sell, you must wait one day before buying
again (cooldown of 1 day).

Pattern: State Machine DP
Three states on each day:
    hold     - holding a stock (bought previously or today)
    sold     - just sold today (triggers cooldown tomorrow)
    cooldown - not holding, free to buy tomorrow

Transitions:
    hold[i]     = max(hold[i-1],     cooldown[i-1] - prices[i])  # keep or buy
    sold[i]     = hold[i-1] + prices[i]                          # sell
    cooldown[i] = max(cooldown[i-1], sold[i-1])                  # rest

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return max profit with unlimited transactions and 1-day cooldown.

        Args:
            prices: List of daily stock prices, 1 <= len(prices) <= 5000.

        Returns:
            Maximum achievable profit.
        """
        if not prices:
            return 0

        hold = -prices[0]  # bought on day 0
        sold = 0           # impossible to have sold on day 0, but 0 is safe
        cooldown = 0       # doing nothing on day 0

        for i in range(1, len(prices)):
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown

            hold = max(prev_hold, prev_cooldown - prices[i])
            sold = prev_hold + prices[i]
            cooldown = max(prev_cooldown, prev_sold)

        # Best answer is either we just sold or we are in cooldown
        return max(sold, cooldown)


# ---------- tests ----------
def test_stock_cooldown():
    sol = Solution()

    # Example 1: buy@1, sell@2, cooldown, buy@0, sell@2 -> profit 3
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3

    # Example 2: single day, no transaction
    assert sol.maxProfit([1]) == 0

    # Monotonically increasing: buy first, sell last (no cooldown needed)
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

    # Monotonically decreasing: no profit
    assert sol.maxProfit([5, 4, 3, 2, 1]) == 0

    # Two days, profit possible
    assert sol.maxProfit([1, 4]) == 3

    # Empty
    assert sol.maxProfit([]) == 0

    # Cooldown matters: [1, 2, 4] -> buy@1 sell@4 = 3
    assert sol.maxProfit([1, 2, 4]) == 3

    print("All tests passed for 309. Best Time to Buy and Sell Stock with Cooldown")


if __name__ == "__main__":
    test_stock_cooldown()
