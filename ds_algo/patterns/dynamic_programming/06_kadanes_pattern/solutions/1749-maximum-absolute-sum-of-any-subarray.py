"""
1749. Maximum Absolute Sum of Any Subarray
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Dual Kadane's (Track max AND min subarray sums)
- The absolute sum of a subarray is maximized when either:
  (a) the subarray sum is maximally positive, OR
  (b) the subarray sum is maximally negative (its absolute value is large)
- Run Kadane's to find max subarray sum AND min subarray sum simultaneously.
- Answer = max(maxSum, -minSum) = max(maxSum, abs(minSum))

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Track running max subarray sum and running min subarray sum
        using Kadane's algorithm in both directions (max and min).
        The answer is the larger absolute value among the two.
        """
        max_end = min_end = 0
        max_sum = min_sum = 0

        for num in nums:
            # Kadane for max subarray sum
            max_end = max(num, max_end + num)
            max_sum = max(max_sum, max_end)

            # Kadane for min subarray sum
            min_end = min(num, min_end + num)
            min_sum = min(min_sum, min_end)

        return max(max_sum, -min_sum)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [1,-3,2,3,-4] -> max subarray sum = 5 (2+3), answer = 5
    assert sol.maxAbsoluteSum([1, -3, 2, 3, -4]) == 5
    # Example 2: [2,-5,1,-4,3,-2] -> min subarray sum = -8 (-5+1-4), answer = 8
    assert sol.maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8
    # Single element
    assert sol.maxAbsoluteSum([5]) == 5
    assert sol.maxAbsoluteSum([-5]) == 5
    # All positive
    assert sol.maxAbsoluteSum([1, 2, 3]) == 6
    # All negative
    assert sol.maxAbsoluteSum([-1, -2, -3]) == 6
    # Mixed
    assert sol.maxAbsoluteSum([1, -1, 1, -1]) == 1

    print("Solution: all tests passed")
