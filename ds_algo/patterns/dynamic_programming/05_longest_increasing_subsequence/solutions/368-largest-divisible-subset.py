"""
368. Largest Divisible Subset (Medium)

Given a set of distinct positive integers nums, return the largest subset
such that every pair (nums[i], nums[j]) satisfies nums[i] % nums[j] == 0
or nums[j] % nums[i] == 0.

Pattern: LIS-like with divisibility check.

Approach:
    1. Sort the array so we only need to check one direction (larger % smaller).
    2. dp[i] = size of the largest divisible subset ending at index i.
    3. For each i, check all j < i: if nums[i] % nums[j] == 0, we can extend
       the subset ending at j.
    4. Track parent pointers to reconstruct the actual subset.

Time:  O(n^2)
Space: O(n)
"""

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """Return the largest subset where every pair is divisible."""
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n        # length of largest subset ending at i
        parent = [-1] * n   # parent pointer for reconstruction

        best_idx = 0         # index of the end of the best subset

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[best_idx]:
                best_idx = i

        # Reconstruct the subset by following parent pointers
        result = []
        idx = best_idx
        while idx != -1:
            result.append(nums[idx])
            idx = parent[idx]

        return result[::-1]


# ───────────────────────── Tests ─────────────────────────
def test():
    s = Solution()

    # Example 1
    res = s.largestDivisibleSubset([1, 2, 3])
    assert res == [1, 2] or res == [1, 3], f"Unexpected: {res}"

    # Example 2
    res = s.largestDivisibleSubset([1, 2, 4, 8])
    assert res == [1, 2, 4, 8], f"Unexpected: {res}"

    # Single element
    assert s.largestDivisibleSubset([7]) == [7]

    # Empty
    assert s.largestDivisibleSubset([]) == []

    # All pairwise divisible
    res = s.largestDivisibleSubset([1, 2, 4, 8, 16])
    assert res == [1, 2, 4, 8, 16], f"Unexpected: {res}"

    # No pair divisible except via 1
    res = s.largestDivisibleSubset([3, 5, 7, 11])
    assert len(res) == 1, f"Expected single element, got: {res}"

    # Larger mixed case
    res = s.largestDivisibleSubset([1, 3, 6, 24])
    assert res == [1, 3, 6, 24], f"Unexpected: {res}"

    print("All tests passed for 368!")


if __name__ == "__main__":
    test()
