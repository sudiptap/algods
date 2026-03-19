"""
3444. Minimum Increments for Target Multiples in an Array
https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

Pattern: 02 - 0/1 Knapsack (Bitmask DP)

---
APPROACH: dp[mask] = min increments so that subset of targets indicated by mask is satisfied.
- For each number in nums, for each subset of targets, compute cost to make this number
  a multiple of the LCM of that subset. Update dp[mask | subset] with dp[mask] + cost.
- LCM can overflow for large targets, but target values are small (up to 4 targets, values up to ~10^5).

Time: O(n * 2^m * 2^m) where m = len(target) <= 4  Space: O(2^m)
---
"""

from typing import List
from math import gcd, lcm
from functools import reduce


class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        m = len(target)
        full = (1 << m) - 1

        # Precompute LCM for each non-empty subset of target
        subset_lcm = [0] * (1 << m)
        for mask in range(1, 1 << m):
            elements = [target[i] for i in range(m) if mask & (1 << i)]
            subset_lcm[mask] = reduce(lcm, elements)

        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0

        for num in nums:
            # For each subset, compute cost to make num a multiple of subset_lcm
            cost = [0] * (1 << m)
            for s in range(1, 1 << m):
                l = subset_lcm[s]
                r = num % l
                cost[s] = (l - r) % l

            # Update dp: try assigning this num to cover subset s
            new_dp = dp[:]
            for mask in range(full, -1, -1):
                if dp[mask] == INF:
                    continue
                # Try all subsets of remaining targets
                remaining = full ^ mask
                sub = remaining
                while sub > 0:
                    new_mask = mask | sub
                    val = dp[mask] + cost[sub]
                    if val < new_dp[new_mask]:
                        new_dp[new_mask] = val
                    sub = (sub - 1) & remaining
            dp = new_dp

        return dp[full]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumIncrements([1, 2, 3], [4]) == 1
    assert sol.minimumIncrements([8, 4], [10, 5]) == 2
    assert sol.minimumIncrements([7, 9, 10], [7]) == 0

    print("Solution: all tests passed")
