"""
3466. Maximum Coin Collection
https://leetcode.com/problems/maximum-coin-collection/

Pattern: 19 - Linear DP (dp[i][lane][switches])

---
APPROACH: Mario drives on a 2-lane freeway. Enters lane 1 (index 0), can switch
lanes at most 2 times. Must travel at least 1 mile. Can enter and exit at any mile.
- dfs(i, lane, k) = max coins collectible starting from mile i on given lane with k
  switches remaining. Can also choose to start at a later mile.
- Optimization: iterate right to left, maintain dp states.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from functools import lru_cache
from math import inf


class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        n = len(lane1)
        lanes = [lane1, lane2]

        @lru_cache(maxsize=None)
        def dfs(i, j, k):
            """Max coins starting from position i, on lane j, with k switches left."""
            if i >= n:
                return 0
            x = lanes[j][i]
            # Option 1: collect x and stop (just this mile)
            ans = x
            # Option 2: collect x and continue on same lane
            ans = max(ans, dfs(i + 1, j, k) + x)
            if k > 0:
                # Option 3: collect x and switch lane for next mile
                ans = max(ans, dfs(i + 1, j ^ 1, k - 1) + x)
                # Option 4: switch lane now (before collecting), then continue from (i, j^1, k-1)
                ans = max(ans, dfs(i, j ^ 1, k - 1))
            return ans

        ans = -inf
        for i in range(n):
            ans = max(ans, dfs(i, 0, 2))
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxCoins([1, -2, -10, 3], [-5, 10, 0, 1]) == 14
    assert sol.maxCoins([1, -1, -1, -1], [0, 3, 4, -5]) == 8
    assert sol.maxCoins([-5, -4, -3], [-1, 2, 3]) == 5
    assert sol.maxCoins([-3, -3, -3], [9, -2, 4]) == 11
    assert sol.maxCoins([-10], [-2]) == -2

    print("Solution: all tests passed")
