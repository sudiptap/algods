"""
1959. Minimum Total Space Wasted With K Resizing Operations (Medium)
https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

Given array nums of required sizes at each time step and k allowed resizes,
return minimum total wasted space. Waste = allocated - required per step.
Initial size counts as free (not a resize).

Pattern: Linear DP
Approach:
- dp[i][j] = min waste for nums[0..i] using j resizes.
- Partition nums into (k+1) segments. Within each segment, allocated size
  = max of segment, waste = sum(max - nums[idx]) for idx in segment.
- dp[i][j] = min over all split points p of dp[p-1][j-1] + waste(p, i).
- Precompute waste for each segment efficiently.
- Base: dp[i][0] = waste(0, i) = max(0..i)*(i+1) - sum(0..i).

Time:  O(n^2 * k)
Space: O(n * k)
"""

from typing import List


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """Return minimum total space wasted with k resizes.

        Args:
            nums: Required sizes at each time step.
            k: Number of allowed resize operations.

        Returns:
            Minimum total wasted space.
        """
        n = len(nums)
        INF = float('inf')

        # dp[i][j] = min waste for nums[0..i] with j resizes
        dp = [[INF] * (k + 1) for _ in range(n)]

        # Base case: 0 resizes, one segment from 0 to i
        running_max = 0
        running_sum = 0
        for i in range(n):
            running_max = max(running_max, nums[i])
            running_sum += nums[i]
            dp[i][0] = running_max * (i + 1) - running_sum

        # Fill dp
        for j in range(1, k + 1):
            for i in range(n):
                # Try all split points: last segment is [p+1..i]
                seg_max = 0
                seg_sum = 0
                for p in range(i, 0, -1):
                    seg_max = max(seg_max, nums[p])
                    seg_sum += nums[p]
                    waste = seg_max * (i - p + 1) - seg_sum
                    dp[i][j] = min(dp[i][j], dp[p - 1][j - 1] + waste)
                # Also consider single element segments or the whole thing
                # p=0 case: segment [0..i] with j resizes but that's just dp[i][0]
                # Already handled by dp[i][j] potentially being dp[i][0]
                dp[i][j] = min(dp[i][j], dp[i][0])

        return dp[n - 1][k]


# ---------- tests ----------
def test_min_space_wasted():
    sol = Solution()

    # Example 1
    assert sol.minSpaceWastedKResizing([10, 20], 0) == 10

    # Example 2
    assert sol.minSpaceWastedKResizing([10, 20, 30], 1) == 10

    # Example 3
    assert sol.minSpaceWastedKResizing([10, 20, 15, 30, 20], 2) == 15

    # All same
    assert sol.minSpaceWastedKResizing([5, 5, 5], 0) == 0

    # k >= n-1 (can resize at every step)
    assert sol.minSpaceWastedKResizing([1, 2, 3], 2) == 0

    print("All tests passed for 1959. Minimum Total Space Wasted With K Resizing")


if __name__ == "__main__":
    test_min_space_wasted()
