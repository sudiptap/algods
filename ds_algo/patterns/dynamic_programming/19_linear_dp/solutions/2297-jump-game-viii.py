"""
2297. Jump Game VIII
https://leetcode.com/problems/jump-game-viii/

Pattern: 19 - Linear DP

---
APPROACH: Monotonic stack to build graph, then shortest path (DP)
- From index i, you can jump to j > i if:
  (1) nums[j] >= nums[i] and all nums[k] < nums[i] for k in (i,j) -- next >= element
  (2) nums[j] < nums[i] and all nums[k] >= nums[i] for k in (i,j) -- next < element
- Use two monotonic stacks:
  - Decreasing stack to find next >= (when nums[j] >= stack top, pop and create edge)
  - Increasing stack to find next < (when nums[j] < stack top, pop and create edge)
- dp[j] = min cost to reach j from 0.

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

        # Build adjacency via monotonic stacks and compute dp simultaneously
        # Stack for type 1: find next >= element (monotonic decreasing stack by value)
        # When nums[j] >= nums[stack[-1]], edge from stack[-1] -> j
        stack1 = []  # decreasing
        # Stack for type 2: find next < element (monotonic increasing stack by value)
        # When nums[j] < nums[stack[-1]], edge from stack[-1] -> j
        stack2 = []  # increasing (non-decreasing actually)

        for j in range(n):
            # Type 1: next >= (pop elements that are <= nums[j] from decreasing stack)
            while stack1 and nums[stack1[-1]] <= nums[j]:
                i = stack1.pop()
                dp[j] = min(dp[j], dp[i] + costs[j])
            stack1.append(j)

            # Type 2: next < (pop elements that are > nums[j] from increasing stack)
            while stack2 and nums[stack2[-1]] > nums[j]:
                i = stack2.pop()
                dp[j] = min(dp[j], dp[i] + costs[j])
            stack2.append(j)

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # [3,2,4,4,1]: edges 0->1,0->2,1->2,1->4,2->3,2->4,3->4
    # dp: [3,10,9,13,11]
    assert sol.minCost([3, 2, 4, 4, 1], [3, 7, 6, 4, 2]) == 11
    # [0,1,2]: monotonically increasing, 0->1->2
    assert sol.minCost([0, 1, 2], [1, 1, 1]) == 3
    assert sol.minCost([5], [10]) == 10

    print("all tests passed")
