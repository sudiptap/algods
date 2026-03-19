"""
3473. Sum of K Subarrays With Length at Least M
https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

Pattern: 06 - Kadane's Pattern (DP selecting k non-overlapping subarrays)

---
APPROACH: DP selecting k non-overlapping subarrays each of length >= m.
- dp[j][i] = max sum using j subarrays from first i elements.
- For each new subarray ending at i with length >= m:
  dp[j][i] = max over L >= m of (dp[j-1][i-L] + sum(nums[i-L+1..i]))
- Use prefix sums. Optimize with rolling max of dp[j-1][t] - prefix[t] for t <= i-m.

Time: O(n * k)  Space: O(n * k)
---
"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        INF = float('-inf')

        # Prefix sums
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        # dp[j][i] = max sum using j subarrays from nums[0..i-1]
        # dp[0][i] = 0 for all i
        # dp[j][i] = max(dp[j][i-1],  -- don't end a subarray at i
        #                max over L>=m: dp[j-1][i-L] + pre[i] - pre[i-L])
        #          = max(dp[j][i-1], pre[i] + max(dp[j-1][t] - pre[t]) for t <= i-m)

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k + 1):
            best = INF  # max of dp[j-1][t] - pre[t] for valid t
            for i in range(1, n + 1):
                # t = i - m: this t becomes newly valid
                t = i - m
                if t >= 0 and dp[j - 1][t] != INF:
                    best = max(best, dp[j - 1][t] - pre[t])

                dp[j][i] = dp[j][i - 1]  # don't end subarray at i
                if best != INF:
                    dp[j][i] = max(dp[j][i], pre[i] + best)

        return dp[k][n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSum([1, 2, -1, 3, 3, 4], 2, 2) == 13
    assert sol.maxSum([-10, 3, -1, -2], 1, 1) == 3

    print("Solution: all tests passed")
