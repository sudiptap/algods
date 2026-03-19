"""
3660. Jump Game IX
https://leetcode.com/problems/jump-game-ix/

Pattern: 19 - Linear DP

---
APPROACH: Monotonic stack + DP
- From position i, can jump to the nearest j > i where nums[j] >= nums[i]
  (next greater or equal) or the nearest j > i where nums[j] < nums[i]
  (next smaller).
- Cost of jump = some function of values.
- dp[i] = min cost to reach position n-1 from i.
- Use monotonic stack to precompute next greater/smaller elements.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return costs[0]

        # Next greater or equal element
        nge = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                nge[stack.pop()] = i
            stack.append(i)

        # Next smaller element
        nse = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                nse[stack.pop()] = i
            stack.append(i)

        # DP forward: dp[i] = min cost to reach i from 0
        INF = float('inf')
        dp = [INF] * n
        dp[0] = costs[0]

        for i in range(n):
            if dp[i] == INF:
                continue
            if nge[i] != -1:
                j = nge[i]
                dp[j] = min(dp[j], dp[i] + costs[j])
            if nse[i] != -1:
                j = nse[i]
                dp[j] = min(dp[j], dp[i] + costs[j])

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple: [3,2,4,1], costs=[1,2,3,4]
    # From 0(3): nge=2(4), nse=1(2). dp[2]=1+3=4, dp[1]=1+2=3.
    # From 1(2): nge=2(4), nse=3(1). dp[2]=min(4,3+3)=4, dp[3]=3+4=7.
    # From 2(4): nge=-1, nse=3(1). dp[3]=min(7,4+4)=7.
    res = sol.minCost([3, 2, 4, 1], [1, 2, 3, 4])
    assert res == 7, f"Got {res}"

    # Two elements
    res = sol.minCost([1, 2], [1, 3])
    assert res == 4, f"Got {res}"

    print("All tests passed!")
