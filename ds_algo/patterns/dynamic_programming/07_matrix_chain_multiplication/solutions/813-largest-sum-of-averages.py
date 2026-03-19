"""
813. Largest Sum of Averages
https://leetcode.com/problems/largest-sum-of-averages/

Pattern: 07 - Matrix Chain Multiplication

---
APPROACH: DP on partitioning into k groups
- dp[i][k] = max sum of averages partitioning nums[:i] into k groups.
- Transition: dp[i][k] = max over j in [k-1, i-1] of
  dp[j][k-1] + avg(nums[j:i])
- Base: dp[i][1] = avg(nums[:i]) = prefix_sum[i] / i
- Use prefix sums for O(1) average computation.

Time: O(k * n^2)  Space: O(n * k) or O(n) with rolling
---
"""

from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def avg(i, j):
            """Average of nums[i:j]"""
            return (prefix[j] - prefix[i]) / (j - i)

        # dp[i] = best sum of averages for nums[:i] with current number of groups
        dp = [0.0] + [avg(0, i) for i in range(1, n + 1)]  # 1 group, dp[0]=0 unused

        for g in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            for i in range(g, n + 1):  # need at least g elements
                for j in range(g - 1, i):  # last group is nums[j:i]
                    new_dp[i] = max(new_dp[i], dp[j] + avg(j, i))
            dp = new_dp

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert abs(sol.largestSumOfAverages([9, 1, 2, 3, 9], 3) - 20.0) < 1e-6
    assert abs(sol.largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4) - 20.5) < 1e-6
    assert abs(sol.largestSumOfAverages([4, 1, 7, 5, 6, 2, 3], 4) - 18.16667) < 1e-4
    assert abs(sol.largestSumOfAverages([1], 1) - 1.0) < 1e-6

    print("all tests passed")
