"""
188. Best Time to Buy and Sell Stock IV (Hard)

Pattern: State Machine DP (14)
Approach:
    Track dp[t][0] = max profit completing at most t transactions, not holding stock
    Track dp[t][1] = max profit completing at most t transactions, holding stock
    Transitions:
        dp[t][0] = max(dp[t][0], dp[t][1] + price)   # sell
        dp[t][1] = max(dp[t][1], dp[t-1][0] - price)  # buy (uses t-1 since buying starts a new transaction)
    Optimization: if k >= n//2, unlimited transactions (greedy).

Complexity:
    Time:  O(n * k) normal case, O(n) if k >= n//2
    Space: O(k)
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # If k >= n//2, we can make unlimited transactions (greedy)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[t][0] = not holding, dp[t][1] = holding
        dp = [[0, float('-inf')] for _ in range(k + 1)]

        for price in prices:
            for t in range(k, 0, -1):
                dp[t][0] = max(dp[t][0], dp[t][1] + price)    # sell
                dp[t][1] = max(dp[t][1], dp[t - 1][0] - price)  # buy

        return dp[k][0]


# ---------- Tests ----------
import unittest


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # k=2, prices=[2,4,1] -> buy@2 sell@4 = 2
        self.assertEqual(self.sol.maxProfit(2, [2, 4, 1]), 2)

    def test_example2(self):
        # k=2, prices=[3,2,6,5,0,3] -> buy@2 sell@6, buy@0 sell@3 = 7
        self.assertEqual(self.sol.maxProfit(2, [3, 2, 6, 5, 0, 3]), 7)

    def test_k_zero(self):
        self.assertEqual(self.sol.maxProfit(0, [1, 2, 3]), 0)

    def test_empty(self):
        self.assertEqual(self.sol.maxProfit(2, []), 0)

    def test_single(self):
        self.assertEqual(self.sol.maxProfit(1, [5]), 0)

    def test_decreasing(self):
        self.assertEqual(self.sol.maxProfit(2, [5, 4, 3, 2, 1]), 0)

    def test_large_k_unlimited(self):
        # k >= n//2 triggers greedy: 1+1+1 = 3
        self.assertEqual(self.sol.maxProfit(100, [1, 2, 3, 4]), 3)

    def test_one_transaction(self):
        self.assertEqual(self.sol.maxProfit(1, [7, 1, 5, 3, 6, 4]), 5)


if __name__ == "__main__":
    unittest.main()
