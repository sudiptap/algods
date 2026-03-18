"""
918. Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/

Pattern: 06 - Kadane's Pattern

---
APPROACH: The max-sum circular subarray is either:
  (a) A normal (non-wrapping) subarray → standard Kadane's max.
  (b) A wrapping subarray → totalSum - (minimum subarray sum via Kadane's min).

Answer = max(case_a, case_b).

Edge case: if ALL elements are negative, Kadane's min equals totalSum, making
case_b = 0 which is invalid (empty subarray not allowed). In that case, return
the maximum element (which equals case_a).

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Return the maximum sum of a non-empty subarray in the circular array."""
        total_sum = 0
        max_sum = nums[0]
        cur_max = 0
        min_sum = nums[0]
        cur_min = 0

        for x in nums:
            cur_max = max(cur_max + x, x)
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min + x, x)
            min_sum = min(min_sum, cur_min)

            total_sum += x

        # If all elements are negative, max_sum is the largest single element
        # and total_sum == min_sum, so the wrap case would give 0 (invalid).
        if total_sum == min_sum:
            return max_sum

        return max(max_sum, total_sum - min_sum)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: non-wrapping [3, -1, 2] or wrapping equivalent
    assert sol.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    # Example 2: no wrap needed, take all
    assert sol.maxSubarraySumCircular([5, -3, 5]) == 10
    # All negative — must pick single largest
    assert sol.maxSubarraySumCircular([-3, -2, -3]) == -2
    # Single element
    assert sol.maxSubarraySumCircular([3]) == 3
    # Kadane max = 7 (subarray [4,-1,4]), wrap also gives 7
    assert sol.maxSubarraySumCircular([4, -1, 4, -1]) == 7

    print("all tests passed")
