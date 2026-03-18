"""
518. Coin Change II (Medium)
https://leetcode.com/problems/coin-change-ii/

You are given an integer array coins representing coin denominations and an
integer amount. Return the number of combinations that make up that amount.
If no combination sums to the amount, return 0. You may use each coin an
unlimited number of times.

Pattern: Unbounded Knapsack
- dp[j] = number of combinations to make amount j.
- Outer loop over coins, inner loop over amounts ensures each combination
  is counted once (not permutations).
- Transition: dp[j] += dp[j - c] for each coin c.
- Base case: dp[0] = 1 (one way to make amount 0: use no coins).

Time:  O(amount * len(coins))
Space: O(amount)
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """Return the number of coin combinations that sum to amount.

        Args:
            amount: Target amount, 0 <= amount <= 5000.
            coins: Available coin denominations (distinct positive ints).

        Returns:
            Number of distinct combinations (order does not matter).
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:                    # outer loop: coins
            for j in range(c, amount + 1): # inner loop: amounts
                dp[j] += dp[j - c]

        return dp[amount]


# ---------- tests ----------
def test_coin_change_ii():
    sol = Solution()

    # Example 1: 5 = {5}, {2+2+1}, {2+1+1+1}, {1+1+1+1+1} => 4
    assert sol.change(5, [1, 2, 5]) == 4

    # Example 2: no way to make 3 with only [2]
    assert sol.change(3, [2]) == 0

    # Example 3: one way to make 0
    assert sol.change(0, [7]) == 1

    # Single coin divides amount exactly
    assert sol.change(10, [5]) == 1

    # Single coin does not divide amount
    assert sol.change(7, [5]) == 0

    # Multiple coins
    assert sol.change(100, [1, 5, 10, 25]) == 242

    print("All tests passed for 518. Coin Change II")


if __name__ == "__main__":
    test_coin_change_ii()
