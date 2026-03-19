"""
3578. Count Partitions With Max-Min Difference at Most K
https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

Pattern: 19 - Linear DP

---
APPROACH: Sliding window + DP
- dp[i] = number of ways to partition nums[0..i-1].
- For each i, find the leftmost j such that max(nums[j..i-1]) - min(nums[j..i-1]) <= k.
- dp[i] = sum(dp[j] for all valid j).
- Use prefix sums for range sum of dp, and monotonic deques for sliding min/max.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import deque

MOD = 10**9 + 7


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty prefix

        prefix = [0] * (n + 2)
        prefix[1] = 1  # prefix[i+1] = sum(dp[0..i])

        max_q = deque()  # decreasing
        min_q = deque()  # increasing
        left = 0

        for i in range(n):
            # Add nums[i] to window
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)

            # Shrink window from left until max - min <= k
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()

            # dp[i+1] = sum of dp[left..i] = prefix[i+1] - prefix[left]
            dp[i + 1] = (prefix[i + 1] - prefix[left]) % MOD
            prefix[i + 2] = (prefix[i + 1] + dp[i + 1]) % MOD

        return dp[n] % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countPartitions([4, 2, 3], 2) == 4
    assert sol.countPartitions([1, 1, 1], 0) == 4
    assert sol.countPartitions([5], 0) == 1

    print("All tests passed!")
