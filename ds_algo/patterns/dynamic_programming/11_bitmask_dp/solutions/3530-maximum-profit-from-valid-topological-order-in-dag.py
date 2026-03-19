"""
3530. Maximum Profit from Valid Topological Order in DAG
https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

Pattern: 11 - Bitmask DP (dp[mask])

---
APPROACH: dp[mask] = max profit when the set of nodes in mask have been placed.
- mask represents which nodes have been selected so far.
- At each step, place the next unselected node whose prerequisites are all in mask.
- Profit for placing node v at position |mask|+1 = score[v] * position.
- n <= 22 from constraints, so 2^n bitmask DP is feasible.

Time: O(2^n * n)  Space: O(2^n)
---
"""

from typing import List


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # Precompute prerequisite masks for each node
        pre_mask = [0] * n
        for u, v in edges:
            pre_mask[v] |= (1 << u)

        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            pos = bin(mask).count('1') + 1  # 1-indexed position for next node
            for v in range(n):
                if mask & (1 << v):
                    continue  # already placed
                if (mask & pre_mask[v]) != pre_mask[v]:
                    continue  # prerequisites not met
                new_mask = mask | (1 << v)
                profit = dp[mask] + score[v] * pos
                if profit > dp[new_mask]:
                    dp[new_mask] = profit

        return dp[(1 << n) - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit(2, [[0, 1]], [2, 3]) == 8  # node 0 at pos 1 (2), node 1 at pos 2 (6)
    assert sol.maxProfit(3, [[0, 1], [0, 2]], [1, 6, 3]) == 25

    print("Solution: all tests passed")
