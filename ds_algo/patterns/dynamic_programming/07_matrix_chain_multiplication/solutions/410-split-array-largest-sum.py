"""
410. Split Array Largest Sum (Hard)
https://leetcode.com/problems/split-array-largest-sum/

Pattern: Binary Search on Answer (also fits Matrix Chain / Interval DP framing)

Given an integer array nums and an integer k, split nums into k non-empty
contiguous subarrays such that the largest sum among them is minimized.
Return the minimized largest sum.

Approach:
    Binary search on the answer space.
    - lo = max(nums)       (each subarray has at least one element)
    - hi = sum(nums)       (one subarray holds everything)
    - For a candidate max-sum `mid`, greedily check whether we can partition
      into <= k subarrays each with sum <= mid.

Time:  O(n * log(sum - max))
Space: O(1)
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """Split nums into k subarrays minimizing the largest subarray sum."""

        def can_split(max_sum: int) -> bool:
            """Return True if nums can be split into <= k parts, each <= max_sum."""
            parts = 1
            cur = 0
            for num in nums:
                if cur + num > max_sum:
                    parts += 1
                    cur = num
                    if parts > k:
                        return False
                else:
                    cur += num
            return True

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().splitArray([7, 2, 5, 10, 8], 2) == 18

def test_example2():
    assert Solution().splitArray([1, 2, 3, 4, 5], 2) == 9

def test_single_element():
    assert Solution().splitArray([10], 1) == 10

def test_k_equals_n():
    # Each element in its own subarray -> answer is max element
    assert Solution().splitArray([1, 4, 2, 3], 4) == 4

def test_all_equal():
    assert Solution().splitArray([5, 5, 5, 5], 2) == 10

def test_large_k():
    assert Solution().splitArray([1, 2, 3, 4, 5], 5) == 5

def test_descending():
    assert Solution().splitArray([10, 5, 3, 1], 3) == 10


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
