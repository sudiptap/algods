"""
1043. Partition Array for Maximum Sum
https://leetcode.com/problems/partition-array-for-maximum-sum/

Pattern: 19 - Linear DP

---
APPROACH: Linear DP
- dp[i] = maximum sum for the first i elements (arr[0..i-1]).
- For each position i, try ending the last partition at lengths 1..k:
    For length l in [1, min(k, i)]:
        last partition covers arr[i-l .. i-1]
        dp[i] = max(dp[i], dp[i-l] + max(arr[i-l..i-1]) * l)
- We track the running max as we extend the partition backward.

Time:  O(n * k)
Space: O(n)
---
"""

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """Return max sum after partitioning arr into subarrays of length <= k."""
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            cur_max = 0
            for l in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - l])
                dp[i] = max(dp[i], dp[i - l] + cur_max * l)

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3) == 84
    assert sol.maxSumAfterPartitioning(
        [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4
    ) == 83
    assert sol.maxSumAfterPartitioning([1], 1) == 1
    assert sol.maxSumAfterPartitioning([5, 5, 5], 2) == 15

    print("Solution: all tests passed")
