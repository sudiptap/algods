"""
494. Target Sum (Medium)
https://leetcode.com/problems/target-sum/

Pattern: 0/1 Knapsack

Given an integer array nums and an integer target, assign + or - to each
element so they sum to target.  Return the number of ways.

Approach:
    Let P = sum of elements assigned +, N = sum assigned -.
    P + N = total,  P - N = target  =>  P = (target + total) / 2.
    If (target + total) is odd or negative, answer is 0.
    Problem reduces to: count subsets of nums that sum to P.
    Use 0/1 knapsack counting with 1-D dp.

Time:  O(n * P)
Space: O(P)
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Return the number of ways to assign +/- to reach target."""
        total = sum(nums)
        if (target + total) % 2 != 0 or target + total < 0:
            return 0

        subset_sum = (target + total) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5

def test_example2():
    assert Solution().findTargetSumWays([1], 1) == 1

def test_zero_target():
    assert Solution().findTargetSumWays([0, 0, 0, 0, 0], 0) == 32

def test_impossible():
    assert Solution().findTargetSumWays([1, 2, 3], 7) == 0

def test_negative_target():
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], -3) == 5

def test_single_zero():
    assert Solution().findTargetSumWays([0], 0) == 2

def test_larger():
    assert Solution().findTargetSumWays([1, 2, 1], 0) == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
