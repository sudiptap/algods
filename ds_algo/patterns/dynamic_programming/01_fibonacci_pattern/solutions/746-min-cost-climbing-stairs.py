"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

Pattern: 01 - Fibonacci Pattern

---
APPROACH: Classic bottom-up DP with O(1) space.
- dp[i] = min cost to reach step i
- dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
- Can start from step 0 or step 1, so dp[0] = dp[1] = 0.
- Answer is dp[n] (reaching the top, one step past the last index).
- Only need two previous values → O(1) space.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Return minimum cost to reach the top of the staircase."""
        prev2, prev1 = 0, 0  # dp[0], dp[1]

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2, prev1 = prev1, curr

        return prev1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert sol.minCostClimbingStairs([0, 0]) == 0
    assert sol.minCostClimbingStairs([1, 2]) == 1
    assert sol.minCostClimbingStairs([5]) == 0  # can start at step 1 (past end)

    print("all tests passed")
