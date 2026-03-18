"""
714. Best Time to Buy and Sell Stock with Transaction Fee (Medium)

You are given an array prices where prices[i] is the price of a given stock
on the ith day, and an integer fee representing a transaction fee. Find the
maximum profit you can achieve. You may complete as many transactions as you
like, but you need to pay the transaction fee for each transaction.

Pattern: State Machine DP
- Two states at each day:
  - cash: max profit when NOT holding stock
  - hold: max profit when holding stock
- Transitions:
  - cash = max(cash, hold + price - fee)   (sell today or do nothing)
  - hold = max(hold, cash - price)          (buy today or do nothing)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """Return max profit with unlimited transactions and a per-transaction fee."""
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash, hold = max(cash, hold + price - fee), max(hold, cash - price)
        return cash


# ----------------- Tests -----------------
def run_tests():
    sol = Solution()

    # Example 1
    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8, "Test 1 failed"

    # Example 2
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6, "Test 2 failed"

    # Single day - no transaction possible
    assert sol.maxProfit([5], 1) == 0, "Test 3 failed"

    # Prices always decreasing - best to do nothing
    assert sol.maxProfit([9, 7, 5, 3, 1], 1) == 0, "Test 4 failed"

    # Fee too high to profit
    assert sol.maxProfit([1, 2, 3], 5) == 0, "Test 5 failed"

    # Two profitable transactions
    assert sol.maxProfit([1, 4, 1, 4], 1) == 4, "Test 6 failed"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
