"""
2297. Jump Game VIII
https://leetcode.com/problems/jump-game-viii/

Pattern: 19 - Linear DP

---
APPROACH: Monotonic stack to build graph, then shortest path (DP)
- From index i, you can jump to the nearest j>i where:
  (1) nums[j] >= nums[i] and all between are < nums[i] (next greater or equal)
  (2) nums[j] < nums[i] and all between are >= nums[i] (next smaller)
- Use two monotonic stacks to find these edges.
- Then dp[j] = min(dp[i] + costs[j]) over valid edges i->j.

Time: O(n)  Space: O(n)
---
"""

from typing import List
import math


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        dp[0] = costs[0]

        # Stack for next >= (decreasing stack)
        stack_ge = []
        # Stack for next < (increasing stack)
        stack_lt = []

        for j in range(n):
            # Next greater or equal: pop elements < nums[j]
            while stack_ge and nums[stack_ge[-1]] <= nums[j]:
                i = stack_ge.pop()
                if nums[j] >= nums[i]:
                    dp[j] = min(dp[j], dp[i] + costs[j])
            # Next smaller: pop elements >= nums[j]
            while stack_lt and nums[stack_lt[-1]] > nums[j]:
                i = stack_lt.pop()
                dp[j] = min(dp[j], dp[i] + costs[j])

            stack_ge.append(j)
            stack_lt.append(j)

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minCost([3, 2, 4, 4, 1], [3, 7, 6, 4, 2]) == 8
    assert sol.minCost([0, 1, 2], [1, 1, 1]) == 2
    assert sol.minCost([5], [10]) == 10

    print("all tests passed")
