"""
3500. Minimum Cost to Divide Array Into Subarrays
https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

Pattern: 19 - Linear DP

---
APPROACH: DP with prefix sums.
- Cost of subarray from i to j (as the m-th subarray):
  (prefix_nums[j+1] + k*m) * (cost[i] + ... + cost[j])
  where prefix_nums[j+1] = cumulative sum of nums[0..j] and m is 1-indexed subarray number.
- Actually: cost of subarray [i..j] = prefixNums[j+1] * (prefixCost[j+1] - prefixCost[i])
  + k * (prefixCost[n] - prefixCost[i])
  (from the reference solution pattern).
- dp[i] = min cost to partition nums[i..n-1].

Time: O(n^2)  Space: O(n)
---
"""

from typing import List
import itertools
import math


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        prefixNums = list(itertools.accumulate(nums, initial=0))
        prefixCost = list(itertools.accumulate(cost, initial=0))

        # dp[i] = min cost to divide nums[i..n-1]
        dp = [math.inf] * n + [0]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i] = min(dp[i],
                            prefixNums[j + 1] * (prefixCost[j + 1] - prefixCost[i]) +
                            k * (prefixCost[n] - prefixCost[i]) + dp[j + 1])

        return dp[0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumCost([3, 1, 4], [4, 6, 6], 1) == 110
    assert sol.minimumCost([4, 8, 5, 1, 14, 2, 2, 12, 1], [7, 2, 8, 4, 2, 2, 1, 1, 2], 7) == 985

    print("Solution: all tests passed")
