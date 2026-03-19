"""
487. Max Consecutive Ones II (Medium)
https://leetcode.com/problems/max-consecutive-ones-ii/

Pattern: Linear DP / Sliding Window

Given a binary array, find the maximum number of consecutive 1s
if you can flip at most one 0.

Approach:
    Sliding window with at most one zero inside.
    Track the count of zeros in the window [left, right].
    When zeros > 1, shrink from the left until zeros <= 1.
    Answer is max(right - left + 1).

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Return max consecutive 1s with at most one flip."""
        left = 0
        zeros = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)

        return best


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().findMaxConsecutiveOnes([1,0,1,1,0]) == 4

def test_all_ones():
    assert Solution().findMaxConsecutiveOnes([1,1,1,1]) == 4

def test_all_zeros():
    assert Solution().findMaxConsecutiveOnes([0,0,0]) == 1

def test_single_zero():
    assert Solution().findMaxConsecutiveOnes([0]) == 1

def test_single_one():
    assert Solution().findMaxConsecutiveOnes([1]) == 1

def test_alternating():
    assert Solution().findMaxConsecutiveOnes([1,0,1,0,1]) == 3

def test_two_elements():
    assert Solution().findMaxConsecutiveOnes([0,1]) == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
