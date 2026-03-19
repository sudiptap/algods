"""
2495. Number of Subarrays Having Even Product
https://leetcode.com/problems/number-of-subarrays-having-even-product/

Pattern: 19 - Linear DP

---
APPROACH: Total subarrays minus subarrays with all odd elements
- A subarray has even product iff at least one element is even.
- Total subarrays = n*(n+1)/2.
- Subarrays with all odd = sum of L*(L+1)/2 for each maximal run of odd numbers.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        odd_run = 0
        all_odd = 0

        for x in nums:
            if x % 2 == 1:
                odd_run += 1
            else:
                all_odd += odd_run * (odd_run + 1) // 2
                odd_run = 0
        all_odd += odd_run * (odd_run + 1) // 2

        return total - all_odd


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.evenProduct([9, 6, 7, 13]) == 6
    assert sol.evenProduct([7, 3, 5]) == 0
    assert sol.evenProduct([2]) == 1
    assert sol.evenProduct([1, 2, 3]) == 4

    print("all tests passed")
