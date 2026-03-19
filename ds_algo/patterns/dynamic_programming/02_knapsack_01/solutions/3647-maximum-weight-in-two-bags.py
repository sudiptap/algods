"""
3647. Maximum Weight in Two Bags
https://leetcode.com/problems/maximum-weight-in-two-bags/

Pattern: 02 - 0/1 Knapsack

---
APPROACH: 0/1 Knapsack with two constraints (two bags)
- Two bags with capacities c1 and c2.
- Each item can go in bag 1, bag 2, or neither.
- Maximize total weight of items placed in either bag.
- dp[j1][j2] = max weight using j1 capacity in bag1, j2 in bag2.
- For each item of weight w: dp[j1][j2] = max of:
  - dp[j1][j2] (skip)
  - dp[j1-w][j2] + w (put in bag 1)
  - dp[j1][j2-w] + w (put in bag 2)

Time: O(n * c1 * c2)  Space: O(c1 * c2)
---
"""

from typing import List


class Solution:
    def maxWeight(self, items: List[int], c1: int, c2: int) -> int:
        dp = [[0] * (c2 + 1) for _ in range(c1 + 1)]

        for w in items:
            # Iterate backwards to avoid using same item twice
            for j1 in range(c1, -1, -1):
                for j2 in range(c2, -1, -1):
                    if j1 >= w:
                        dp[j1][j2] = max(dp[j1][j2], dp[j1 - w][j2] + w)
                    if j2 >= w:
                        dp[j1][j2] = max(dp[j1][j2], dp[j1][j2 - w] + w)

        return dp[c1][c2]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Items [1,2,3], bags capacity 3 and 3: put 3 in one, 1+2=3 in other. Total=6.
    res = sol.maxWeight([1, 2, 3], 3, 3)
    assert res == 6, f"Got {res}"

    # Items [5], bags 3,3: can't fit. Total=0.
    res = sol.maxWeight([5], 3, 3)
    assert res == 0, f"Got {res}"

    # Items [4,3], bags 4,3: 4 in bag1, 3 in bag2. Total=7.
    res = sol.maxWeight([4, 3], 4, 3)
    assert res == 7, f"Got {res}"

    print("All tests passed!")
