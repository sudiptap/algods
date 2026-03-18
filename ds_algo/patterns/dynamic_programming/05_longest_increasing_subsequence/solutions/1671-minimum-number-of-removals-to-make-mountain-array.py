"""
1671. Minimum Number of Removals to Make Mountain Array (Hard)
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

A mountain array has: len >= 3, some peak index i where
arr[0] < arr[1] < ... < arr[i] and arr[i] > arr[i+1] > ... > arr[-1].

Given nums, return the minimum number of elements to remove so the
remaining array is a mountain array.

Approach:
    1. Compute LIS[i] = length of longest increasing subsequence ending at i
       (from the left).
    2. Compute LDS[i] = length of longest decreasing subsequence starting at i
       (equivalently, LIS from the right).
    3. For each valid peak i (LIS[i] >= 2 and LDS[i] >= 2), the mountain
       length = LIS[i] + LDS[i] - 1.
    4. Answer = n - max(mountain length).

Time:  O(n^2) using basic LIS, or O(n log n) with patience sorting
Space: O(n)
"""

import bisect
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """Return minimum removals to make nums a mountain array.

        Compute LIS from left and LIS from right (LDS), then find the
        peak that maximizes mountain length.

        Args:
            nums: List of integers, 3 <= len(nums) <= 1000.

        Returns:
            Minimum number of elements to remove.
        """
        n = len(nums)

        # LIS ending at each index (O(n log n))
        lis = [0] * n
        tails = []
        for i in range(n):
            pos = bisect.bisect_left(tails, nums[i])
            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]
            lis[i] = pos + 1

        # LDS starting at each index = LIS from right
        lds = [0] * n
        tails = []
        for i in range(n - 1, -1, -1):
            pos = bisect.bisect_left(tails, nums[i])
            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]
            lds[i] = pos + 1

        # Find max mountain length
        max_mountain = 0
        for i in range(1, n - 1):
            if lis[i] >= 2 and lds[i] >= 2:
                max_mountain = max(max_mountain, lis[i] + lds[i] - 1)

        return n - max_mountain


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minimumMountainRemovals([1, 3, 1]) == 0

    # Example 2
    assert sol.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]) == 3

    # Need to remove elements to form [1,2,3,2,1]
    assert sol.minimumMountainRemovals([1, 2, 3, 4, 4, 3, 2, 1]) == 1

    # Already a mountain
    assert sol.minimumMountainRemovals([1, 2, 3, 2, 1]) == 0

    # Longer example
    assert sol.minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]) == 6

    print("All tests passed!")
