"""
446. Arithmetic Slices II - Subsequence (Hard)

Given an integer array nums, return the number of all the arithmetic
subsequences of nums. A subsequence is arithmetic if it has at least 3
elements and the difference between consecutive elements is constant.

Approach:
    dp[i] is a dict mapping common_difference → count of arithmetic
    subsequences (of length >= 2) ending at index i with that difference.

    For every pair (j, i) with j < i:
        diff = nums[i] - nums[j]
        dp[i][diff] += dp[j].get(diff, 0) + 1
        total      += dp[j].get(diff, 0)

    We add dp[j][diff] to total (not +1) because dp[j][diff] counts
    subsequences of length >= 2 ending at j; extending each by nums[i]
    gives length >= 3. The "+1" in dp[i] accounts for the new length-2
    pair (nums[j], nums[i]) which isn't yet a valid slice but may be
    extended later.

Time:  O(n^2)
Space: O(n^2) — total entries across all dicts
"""

from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """Count arithmetic subsequences of length >= 3."""
        n = len(nums)
        if n < 3:
            return 0

        dp = [defaultdict(int) for _ in range(n)]
        total = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev = dp[j][diff]      # subseqs of len>=2 ending at j
                dp[i][diff] += prev + 1  # extend or start new pair
                total += prev            # only prev extensions give len>=3

        return total


# ── Tests ──────────────────────────────────────────────────────────────────
def test_example1():
    assert Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7

def test_example2():
    assert Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]) == 16

def test_too_short():
    assert Solution().numberOfArithmeticSlices([1, 2]) == 0

def test_three_elements():
    assert Solution().numberOfArithmeticSlices([1, 2, 3]) == 1

def test_no_arithmetic():
    assert Solution().numberOfArithmeticSlices([1, 2, 4, 8]) == 0

def test_negative_diff():
    assert Solution().numberOfArithmeticSlices([5, 3, 1]) == 1

def test_mixed():
    # [1,3,5], [1,3,5,7], [3,5,7], [1,5,9] ... etc.
    assert Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9]) == 7


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
