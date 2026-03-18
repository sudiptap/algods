"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Pattern: 06 - Kadane's Pattern (product variant)

Given an integer array nums, find a contiguous non-empty subarray that has
the largest product, and return the product.

---
APPROACH: Modified Kadane's tracking max AND min products
- Negative * negative = positive, so the minimum product can become the
  maximum after one multiplication.
- At each element, track both max_prod and min_prod ending here.
- new_max = max(num, max_prod * num, min_prod * num)
- new_min = min(num, max_prod * num, min_prod * num)
- Update global answer with new_max.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:
            # candidates: start fresh, extend max, extend min
            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)

            result = max(result, max_prod)

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [2,3,-2,4] -> 6  (subarray [2,3])
    assert sol.maxProduct([2, 3, -2, 4]) == 6

    # Example 2: [-2,0,-1] -> 0
    assert sol.maxProduct([-2, 0, -1]) == 0

    # Single element
    assert sol.maxProduct([3]) == 3
    assert sol.maxProduct([-2]) == -2

    # Two negatives make a positive
    assert sol.maxProduct([-2, -3]) == 6

    # All negatives
    assert sol.maxProduct([-1, -2, -3, -4]) == 24

    # Zeros reset the subarray
    assert sol.maxProduct([0, 2]) == 2
    assert sol.maxProduct([-2, 0, -1]) == 0

    # Mixed with zeros and negatives
    assert sol.maxProduct([-2, 3, -4]) == 24

    # Large product across negatives
    assert sol.maxProduct([2, -5, -2, -4, 3]) == 24

    print("Solution: all tests passed")
