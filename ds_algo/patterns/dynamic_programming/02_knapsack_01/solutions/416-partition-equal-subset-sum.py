"""
416. Partition Equal Subset Sum (Medium)
https://leetcode.com/problems/partition-equal-subset-sum/

Pattern: 0/1 Knapsack

Given a non-empty array of positive integers, determine if the array can be
partitioned into two subsets with equal sum.

Approach:
    If total sum is odd, return False immediately.
    Target = sum // 2.  Use a boolean DP set tracking reachable sums.
    For each number, iterate the dp array right-to-left (to avoid reusing
    the same item) and mark new reachable sums.

Time:  O(n * target)
Space: O(target)
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Return True if nums can be split into two subsets with equal sum."""
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # iterate right-to-left so each num is used at most once
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True

        return dp[target]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().canPartition([1, 5, 11, 5]) is True

def test_example2():
    assert Solution().canPartition([1, 2, 3, 5]) is False

def test_single_element():
    assert Solution().canPartition([1]) is False

def test_two_equal():
    assert Solution().canPartition([3, 3]) is True

def test_odd_total():
    assert Solution().canPartition([1, 2, 4]) is False

def test_larger():
    assert Solution().canPartition([1, 2, 3, 4, 5, 6, 7]) is True  # sum=28, target=14

def test_all_ones():
    assert Solution().canPartition([1, 1, 1, 1]) is True

def test_all_ones_odd_count():
    assert Solution().canPartition([1, 1, 1]) is False


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
