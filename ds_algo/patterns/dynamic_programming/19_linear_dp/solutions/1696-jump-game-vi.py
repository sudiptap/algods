"""
1696. Jump Game VI (Medium)
https://leetcode.com/problems/jump-game-vi/

Given a 0-indexed integer array nums and an integer k, you start at index 0
and want to reach index n-1. In one step from index i, you can jump to any
index in [i+1, min(n-1, i+k)].

Return the maximum score you can get. The score is the sum of nums[j] for
each index j you visit.

Approach - DP with Monotonic Deque:
    dp[i] = max score to reach index i = max(dp[j] for j in [i-k, i-1]) + nums[i].
    Use a monotonic decreasing deque to track the maximum dp value in the
    sliding window of size k, giving O(1) amortized per element.

Time:  O(n)
Space: O(n) for dp, O(k) for deque
"""

from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """Return maximum score to reach the last index.

        Uses a monotonic decreasing deque to efficiently find the max
        dp value in the sliding window [i-k, i-1].

        Args:
            nums: List of integers (can be negative), 1 <= len(nums) <= 10^5.
            k: Maximum jump length, 1 <= k <= 10^5.

        Returns:
            Maximum score achievable.
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        # Deque stores indices; dp values at those indices are monotonically decreasing
        dq = deque([0])

        for i in range(1, n):
            # Remove indices outside the window
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = dp[dq[0]] + nums[i]

            # Maintain decreasing order
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maxResult([1, -1, -2, 4, -7, 3], 2) == 7

    # Example 2
    assert sol.maxResult([10, -5, -2, 4, 0, 3], 3) == 17

    # Example 3
    assert sol.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2) == 0

    # Single element
    assert sol.maxResult([5], 1) == 5

    # All positive
    assert sol.maxResult([1, 2, 3, 4, 5], 1) == 15

    # k covers entire array
    assert sol.maxResult([1, -100, -100, -100, 50], 4) == 51

    print("All tests passed!")
