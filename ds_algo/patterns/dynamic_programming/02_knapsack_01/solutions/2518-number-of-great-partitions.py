"""
2518. Number of Great Partitions
https://leetcode.com/problems/number-of-great-partitions/

Pattern: 02 - 0/1 Knapsack

---
APPROACH: Total ways minus invalid ways
- Total ways to partition n elements into 2 groups = 2^n.
- Invalid: either group has sum < k.
- Count ways where group1 sum < k using knapsack. By symmetry, group2 sum < k
  has the same count. But subtract overlap (both < k only if total < 2k).
- Invalid = 2 * (ways with sum < k) using inclusion-exclusion.
  Actually: count subsets with sum < k. Each such subset means group1 < k.
  Answer = 2^n - 2 * count(subset sum < k).
  But this double-counts cases where both groups have sum < k (impossible if total >= 2k).

Time: O(n * k)  Space: O(k)
---
"""

from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        total = sum(nums)

        if total < 2 * k:
            return 0

        # Count subsets with sum < k
        # dp[j] = number of subsets with sum exactly j
        dp = [0] * k
        dp[0] = 1

        for x in nums:
            for j in range(k - 1, x - 1, -1):
                dp[j] = (dp[j] + dp[j - x]) % MOD

        bad = sum(dp) % MOD  # subsets with sum 0..k-1

        ans = (pow(2, len(nums), MOD) - 2 * bad) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countPartitions([1, 2, 3, 4], 4) == 6
    assert sol.countPartitions([3, 3, 3], 4) == 0
    assert sol.countPartitions([6, 6], 2) == 2

    print("all tests passed")
