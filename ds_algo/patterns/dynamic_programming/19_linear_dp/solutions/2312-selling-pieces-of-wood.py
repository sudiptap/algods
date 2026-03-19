"""
2312. Selling Pieces of Wood
https://leetcode.com/problems/selling-pieces-of-wood/

Pattern: 19 - Linear DP

---
APPROACH: dp[h][w] = max revenue for a piece of height h and width w
- Base: dp[h][w] = price[h][w] if that piece can be sold directly.
- Try all horizontal cuts: dp[h][w] = max(dp[i][w] + dp[h-i][w]) for i in 1..h-1
- Try all vertical cuts: dp[h][w] = max(dp[h][j] + dp[h][w-j]) for j in 1..w-1
- Answer: dp[m][n]

Time: O(m * n * (m + n))  Space: O(m * n)
---
"""

from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Set base prices
        for h, w, p in prices:
            dp[h][w] = max(dp[h][w], p)

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                # Horizontal cuts
                for i in range(1, h // 2 + 1):
                    dp[h][w] = max(dp[h][w], dp[i][w] + dp[h - i][w])
                # Vertical cuts
                for j in range(1, w // 2 + 1):
                    dp[h][w] = max(dp[h][w], dp[h][j] + dp[h][w - j])

        return dp[m][n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.sellingWood(3, 5, [[1,4,2],[2,2,7],[2,1,3]]) == 19
    assert sol.sellingWood(4, 6, [[3,2,10],[1,4,2],[4,1,3]]) == 32
    assert sol.sellingWood(1, 1, []) == 0

    print("all tests passed")
