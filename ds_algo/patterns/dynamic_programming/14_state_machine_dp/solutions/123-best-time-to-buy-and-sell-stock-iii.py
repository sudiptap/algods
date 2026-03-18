"""
123. Best Time to Buy and Sell Stock III (Hard)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Problem:
    You are given an array prices where prices[i] is the price of a given stock
    on the ith day. Find the maximum profit you can achieve with at most TWO
    transactions. You may not engage in multiple transactions simultaneously
    (you must sell before you buy again).

Pattern: 14 - State Machine DP

Approach:
    State machine with 4 states, processed left to right through prices:

      buy1  = max cost basis after 1st buy  (maximize -price, i.e. buy cheapest)
      sell1 = max profit after 1st sell
      buy2  = max "balance" after 2nd buy   (sell1 - price)
      sell2 = max profit after 2nd sell

    Transitions for each price:
      buy1  = max(buy1,  -price)
      sell1 = max(sell1, buy1 + price)
      buy2  = max(buy2,  sell1 - price)
      sell2 = max(sell2, buy2 + price)

    Answer is sell2 (which also covers the 0- or 1-transaction cases because
    states can stay unchanged and a zero-profit transaction is allowed).

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    buy1 = float('-inf')
    sell1 = 0
    buy2 = float('-inf')
    sell2 = 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2


# ─── Tests ───────────────────────────────────────────────────────────────────

def test():
    # Example 1: buy day 0, sell day 1 (profit 3), buy day 2, sell day 4 (profit 3) -> 6
    assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6

    # Example 2: only one increasing run -> 1 transaction suffices -> 4
    assert max_profit([1, 2, 3, 4, 5]) == 4

    # Example 3: monotonically decreasing -> 0
    assert max_profit([7, 6, 4, 3, 1]) == 0

    # Single element
    assert max_profit([1]) == 0

    # Two transactions clearly better than one
    # buy@1 sell@5 profit=4, buy@2 sell@8 profit=6 -> total=10
    assert max_profit([1, 5, 2, 8]) == 10

    # One transaction optimal
    assert max_profit([1, 2]) == 1

    # No profit
    assert max_profit([5, 5, 5]) == 0

    # Classic two-peak
    # buy@1 sell@10 profit=9, buy@3 sell@12 profit=9 -> total=18
    assert max_profit([8, 1, 10, 3, 12, 5]) == 18

    print("All tests passed for 123. Best Time to Buy and Sell Stock III")


if __name__ == "__main__":
    test()
