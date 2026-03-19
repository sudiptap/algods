"""
2431. Maximize Total Tastiness of Purchased Fruits
https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

Pattern: 02 - 0/1 Knapsack

---
APPROACH: dp[j][k] = max tastiness with budget j and k coupons used
- For each fruit i with price[i] and tastiness[i]:
  - Without coupon: cost = price[i]
  - With coupon: cost = floor(price[i] / 2)
- Standard 0/1 knapsack with two capacity dimensions.

Time: O(n * maxAmount * maxCoupons)  Space: O(maxAmount * maxCoupons)
---
"""

from typing import List


class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)
        # dp[j][k] = max tastiness with budget j and k coupons
        dp = [[0] * (maxCoupons + 1) for _ in range(maxAmount + 1)]

        for i in range(n):
            p = price[i]
            t = tastiness[i]
            half_p = p // 2

            # Process in reverse for 0/1 knapsack
            for j in range(maxAmount, -1, -1):
                for k in range(maxCoupons, -1, -1):
                    # Buy without coupon
                    if j >= p:
                        dp[j][k] = max(dp[j][k], dp[j - p][k] + t)
                    # Buy with coupon
                    if k > 0 and j >= half_p:
                        dp[j][k] = max(dp[j][k], dp[j - half_p][k - 1] + t)

        return dp[maxAmount][maxCoupons]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxTastiness([10, 20, 20], [5, 8, 8], 20, 1) == 13
    assert sol.maxTastiness([10, 15, 7], [5, 8, 20], 10, 2) == 28
    assert sol.maxTastiness([100], [50], 10, 0) == 0

    print("all tests passed")
