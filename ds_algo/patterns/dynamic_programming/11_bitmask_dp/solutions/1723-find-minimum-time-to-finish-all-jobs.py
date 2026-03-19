"""
1723. Find Minimum Time to Finish All Jobs
https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP - minimize maximum workload
- dp[mask] = minimum possible maximum working time when jobs in mask are assigned.
- Precompute sum of each subset.
- Binary search on the answer T (max time per worker).
- For a given T, check if jobs can be distributed to k workers with max time T.
- Alternative: dp[mask] = min number of workers needed if max time is T.
- Or: iterate over subsets, assign to workers greedily.

Actually, cleaner approach: binary search + backtracking with pruning.
Or: dp[i][mask] = min max-time using i workers for jobs in mask.
  -> dp[i][mask] = min over submask s of mask: max(dp[i-1][mask^s], sum[s])

Time: O(k * 3^n) where n = number of jobs
Space: O(k * 2^n) or O(2^n) with optimization
---
"""

from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        full = (1 << n) - 1

        # Precompute subset sums
        subset_sum = [0] * (full + 1)
        for mask in range(1, full + 1):
            lsb = mask & (-mask)
            idx = lsb.bit_length() - 1
            subset_sum[mask] = subset_sum[mask ^ lsb] + jobs[idx]

        # Binary search on answer
        def can_do(limit):
            # dp[mask] = min workers needed to handle jobs in mask with max time limit
            INF = k + 1
            dp = [INF] * (full + 1)
            dp[0] = 0

            # Precompute valid subsets (sum <= limit)
            valid = [mask for mask in range(full + 1) if subset_sum[mask] <= limit]

            for mask in range(1, full + 1):
                # Enumerate submasks of mask that are valid
                sub = mask
                while sub > 0:
                    if subset_sum[sub] <= limit:
                        dp[mask] = min(dp[mask], dp[mask ^ sub] + 1)
                    sub = (sub - 1) & mask
                if dp[mask] > k:
                    # Early termination not easy here, continue
                    pass

            return dp[full] <= k

        lo, hi = max(jobs), sum(jobs)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_do(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


# --- Tests ---
def test():
    sol = Solution()

    assert sol.minimumTimeRequired([3, 2, 3], 3) == 3
    assert sol.minimumTimeRequired([1, 2, 4, 7, 8], 2) == 11

    # Single job
    assert sol.minimumTimeRequired([5], 1) == 5

    # All same
    assert sol.minimumTimeRequired([1, 1, 1], 3) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
