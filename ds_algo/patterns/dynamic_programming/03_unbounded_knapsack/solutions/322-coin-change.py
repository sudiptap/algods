"""
322. Coin Change (Medium)
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coin denominations and an
integer amount. Return the fewest number of coins needed to make up that
amount. If it cannot be made up, return -1. You may use each coin an unlimited
number of times.

Pattern: Unbounded Knapsack
- dp[i] = minimum coins to make amount i.
- dp[0] = 0 (base case).
- Transition: dp[i] = min(dp[i - c] + 1) for each coin c where c <= i.
- If dp[amount] is still inf, return -1.

Time:  O(amount * len(coins))
Space: O(amount)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Return the fewest coins to make up amount, or -1 if impossible.

        Args:
            coins: Available coin denominations.
            amount: Target amount, 0 <= amount <= 10^4.

        Returns:
            Minimum number of coins, or -1 if not achievable.
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i and dp[i - c] + 1 < dp[i]:
                    dp[i] = dp[i - c] + 1

        return dp[amount] if dp[amount] != float("inf") else -1


# ---------- tests ----------
def test_coin_change():
    sol = Solution()

    # Example 1: 11 = 10 + 1
    assert sol.coinChange([1, 5, 10], 11) == 2

    # Example 2: coins=[2], amount=3 -> impossible
    assert sol.coinChange([2], 3) == -1

    # Example 3: amount=0 -> 0 coins
    assert sol.coinChange([1], 0) == 0

    # Classic: [1,2,5], amount=11 -> 5+5+1 = 3 coins
    assert sol.coinChange([1, 2, 5], 11) == 3

    # Single coin matches exactly
    assert sol.coinChange([3], 9) == 3

    # Greedy fails: [1,3,4], amount=6 -> 3+3=2 (not 4+1+1=3)
    assert sol.coinChange([1, 3, 4], 6) == 2

    print("All tests passed for 322. Coin Change")


if __name__ == "__main__":
    test_coin_change()
