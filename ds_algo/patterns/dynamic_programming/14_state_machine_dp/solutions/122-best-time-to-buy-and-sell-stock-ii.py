"""
122. Best Time to Buy and Sell Stock II (Medium)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Problem:
    You are given an array prices where prices[i] is the price of a given stock
    on the ith day. On each day you may buy and/or sell. You can hold at most one
    share at a time. You may also buy and sell on the same day. Find the maximum
    profit you can achieve (unlimited transactions).

Pattern: 14 - State Machine DP

Approach:
    State machine with two states each day:
      - hold:     max profit when we own a share at end of day i
      - not_hold: max profit when we do NOT own a share at end of day i

    Transitions:
      hold[i]     = max(hold[i-1],     not_hold[i-1] - price)   # keep or buy
      not_hold[i] = max(not_hold[i-1], hold[i-1] + price)       # keep or sell

    Greedy equivalent: sum all positive day-over-day differences, since every
    upward move can be captured as a separate transaction.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """State machine approach."""
    hold = -prices[0]   # best profit if holding after day 0
    not_hold = 0        # best profit if not holding after day 0

    for price in prices[1:]:
        hold, not_hold = max(hold, not_hold - price), max(not_hold, hold + price)

    return not_hold


def max_profit_greedy(prices: List[int]) -> int:
    """Greedy: collect every upward move."""
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


# ─── Tests ───────────────────────────────────────────────────────────────────

def test():
    # Example 1: buy day 0, sell day 1, buy day 2, sell day 3 -> 4+3=7
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert max_profit_greedy([7, 1, 5, 3, 6, 4]) == 7

    # Example 2: monotonically increasing -> buy first, sell last = 4
    assert max_profit([1, 2, 3, 4, 5]) == 4
    assert max_profit_greedy([1, 2, 3, 4, 5]) == 4

    # Example 3: monotonically decreasing -> 0
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit_greedy([7, 6, 4, 3, 1]) == 0

    # Single element
    assert max_profit([5]) == 0
    assert max_profit_greedy([5]) == 0

    # Two elements up
    assert max_profit([1, 5]) == 4
    assert max_profit_greedy([1, 5]) == 4

    # Zigzag
    assert max_profit([1, 5, 2, 8]) == 10  # (5-1)+(8-2)
    assert max_profit_greedy([1, 5, 2, 8]) == 10

    print("All tests passed for 122. Best Time to Buy and Sell Stock II")


if __name__ == "__main__":
    test()
