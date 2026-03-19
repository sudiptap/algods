"""
3826. Minimum Partition Score
https://leetcode.com/problems/minimum-partition-score/

Pattern: 19 - Linear DP

---
APPROACH: Standard partition DP
- Partition nums into exactly k subarrays.
- Value of subarray = s*(s+1)/2 where s = sum of elements.
- dp[i][j] = min score partitioning first i elements into j parts.
- dp[i][j] = min over l of: dp[l][j-1] + value(nums[l..i-1])
- Since value is convex in sum (quadratic), we want to split sums
  as evenly as possible. Standard O(n^2 * k) DP works for n <= 1000.

Time: O(n^2 * k)  Space: O(n * k)
---
"""

from typing import List


class Solution:
    def minimumPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def value(s):
            return s * (s + 1) // 2

        INF = float('inf')
        # dp[j] = array where dp[j][i] = min cost for first i elements in j parts
        prev = [INF] * (n + 1)
        prev[0] = 0

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)
            for i in range(j, n + 1):
                for l in range(j - 1, i):
                    s = prefix[i] - prefix[l]
                    cost = prev[l] + value(s)
                    if cost < curr[i]:
                        curr[i] = cost
            prev = curr

        return prev[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumPartitionScore([5, 1, 2, 1], 2) == 25
    assert sol.minimumPartitionScore([1, 2, 3, 4], 1) == 55
    assert sol.minimumPartitionScore([1, 1, 1], 3) == 3

    print("all tests passed")
