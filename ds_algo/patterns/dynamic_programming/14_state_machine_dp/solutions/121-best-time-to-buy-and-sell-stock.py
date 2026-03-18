"""
121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
    You are given an array prices where prices[i] is the price of a given stock
    on the ith day. You want to maximize your profit by choosing a single day to
    buy and a single day to sell. Return the maximum profit you can achieve from
    this transaction. If you cannot achieve any profit, return 0.

Pattern: 14 - State Machine DP

Approach:
    Track the minimum price seen so far as we iterate. At each day, the best
    profit we could make by selling today is price - min_price_so_far. Track
    the global maximum of that value.

    This is a simplified state machine with two states:
      - "looking to buy": we track min price
      - "looking to sell": we compute profit against min price

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


# ─── Tests ───────────────────────────────────────────────────────────────────

def test():
    # Example 1: buy day 1 (price=1), sell day 4 (price=6) -> profit 5
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    # Example 2: prices only decrease -> no profit
    assert max_profit([7, 6, 4, 3, 1]) == 0

    # Single element
    assert max_profit([5]) == 0

    # Two elements, profit possible
    assert max_profit([1, 2]) == 1

    # Two elements, no profit
    assert max_profit([2, 1]) == 0

    # All same price
    assert max_profit([3, 3, 3, 3]) == 0

    # Buy at the very start, sell at the very end
    assert max_profit([1, 2, 3, 4, 5]) == 4

    # Min in the middle
    assert max_profit([10, 8, 2, 9]) == 7

    print("All tests passed for 121. Best Time to Buy and Sell Stock")


if __name__ == "__main__":
    test()
