"""
3592. Inverse Coin Change
https://leetcode.com/problems/inverse-coin-change/

Pattern: 03 - Unbounded Knapsack

---
APPROACH: Reconstruct coins from DP array
- Given a dp array where dp[i] = min coins to make amount i (or -1),
  reconstruct the set of coin denominations that produced it.
- Key observations:
  1. dp[0] = 0 always.
  2. A denomination d exists iff dp[d] = 1.
  3. Verify: recompute dp with found coins and check it matches.
- Extract all d where dp[d] == 1, then verify.

Time: O(n * k) where k = number of coins  Space: O(n)
---
"""

from typing import List


class Solution:
    def inverseCoinChange(self, dp_array: List[int]) -> List[int]:
        n = len(dp_array)
        if n == 0:
            return []
        if dp_array[0] != 0:
            return []

        # Find candidate coins: positions where dp[d] == 1
        coins = []
        for d in range(1, n):
            if dp_array[d] == 1:
                coins.append(d)

        # Verify by recomputing dp
        recomputed = [0] + [float('inf')] * (n - 1)
        for i in range(1, n):
            for c in coins:
                if c <= i and recomputed[i - c] != float('inf'):
                    recomputed[i] = min(recomputed[i], recomputed[i - c] + 1)

        for i in range(n):
            expected = dp_array[i]
            got = recomputed[i] if recomputed[i] != float('inf') else -1
            if expected != got:
                return []  # No valid coin set

        return coins


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Coins [1,2,5]: dp = [0,1,1,2,2,1,2,2,3,3,2]
    dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2]
    res = sol.inverseCoinChange(dp)
    assert res == [1, 2, 5], f"Got {res}"

    # Coins [3]: dp = [0,-1,-1,1,-1,-1,2]
    dp = [0, -1, -1, 1, -1, -1, 2]
    res = sol.inverseCoinChange(dp)
    assert res == [3], f"Got {res}"

    print("All tests passed!")
