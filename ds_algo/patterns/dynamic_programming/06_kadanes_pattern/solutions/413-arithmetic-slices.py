"""
413. Arithmetic Slices (Medium)
https://leetcode.com/problems/arithmetic-slices/

Pattern: Kadane's Pattern (linear DP accumulating contiguous results)

An arithmetic slice is a contiguous subarray of length >= 3 where the
difference between consecutive elements is constant.

Approach:
    dp[i] = number of arithmetic slices ending at index i.
    If nums[i] - nums[i-1] == nums[i-1] - nums[i-2], then dp[i] = dp[i-1] + 1
    (the previous slices extend by one element, plus one new slice of length 3).
    Answer = sum of all dp[i].

    Space-optimised to a single variable since dp[i] only depends on dp[i-1].

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """Count the number of arithmetic subarrays of length >= 3."""
        n = len(nums)
        if n < 3:
            return 0

        dp = 0    # arithmetic slices ending at current index
        total = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                total += dp
            else:
                dp = 0

        return total


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3

def test_example2():
    assert Solution().numberOfArithmeticSlices([1]) == 0

def test_length_two():
    assert Solution().numberOfArithmeticSlices([1, 2]) == 0

def test_exact_three():
    assert Solution().numberOfArithmeticSlices([1, 2, 3]) == 1

def test_no_arithmetic():
    assert Solution().numberOfArithmeticSlices([1, 3, 2, 4]) == 0

def test_two_separate_runs():
    # [1,2,3] -> 1 slice; [3,5,7,9,11] (diff=2, length 5) -> 6 slices; total 7
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 5, 7, 9, 11]) == 7

def test_all_same():
    # [5,5,5,5] -> slices: (0-2),(1-3),(0-3) = 3
    assert Solution().numberOfArithmeticSlices([5, 5, 5, 5]) == 3

def test_negative_diff():
    assert Solution().numberOfArithmeticSlices([3, 1, -1, -3]) == 3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
