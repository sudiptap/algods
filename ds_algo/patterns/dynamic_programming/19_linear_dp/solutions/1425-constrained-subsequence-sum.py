"""
1425. Constrained Subsequence Sum (Hard)
https://leetcode.com/problems/constrained-subsequence-sum/

Pattern: Linear DP + Monotonic Deque

Given an integer array nums and an integer k, return the maximum sum of a
non-empty subsequence such that for every two consecutive elements in the
subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k
is satisfied.

Approach:
    dp[i] = max sum of a valid subsequence ending at index i.
    dp[i] = nums[i] + max(0, max(dp[i-k], ..., dp[i-1]))

    To efficiently find the max over the last k dp values, use a monotonic
    deque (decreasing) that stores indices. The front of the deque holds the
    index of the maximum dp value in the window.

Time:  O(n)
Space: O(n)  — O(k) for the deque, O(n) for dp.
"""

from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """Return the maximum constrained subsequence sum."""
        n = len(nums)
        dp = nums[:]
        dq = deque()  # stores indices, dp values in decreasing order

        for i in range(n):
            # Add the best previous value if positive
            if dq and dp[dq[0]] > 0:
                dp[i] += dp[dq[0]]

            # Maintain decreasing monotonic deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

            # Remove elements outside the window
            if dq[0] <= i - k:
                dq.popleft()

        return max(dp)


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2) == 37

def test_example2():
    assert Solution().constrainedSubsetSum([-1, -2, -3], 1) == -1

def test_example3():
    assert Solution().constrainedSubsetSum([10, -2, -10, -5, 20], 2) == 23

def test_single():
    assert Solution().constrainedSubsetSum([5], 1) == 5

def test_all_positive():
    assert Solution().constrainedSubsetSum([1, 2, 3], 1) == 6

def test_k_equals_n():
    assert Solution().constrainedSubsetSum([1, -1, -1, 5], 4) == 6

def test_large_gap():
    assert Solution().constrainedSubsetSum([1, -100, -100, 5], 2) == 5


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
