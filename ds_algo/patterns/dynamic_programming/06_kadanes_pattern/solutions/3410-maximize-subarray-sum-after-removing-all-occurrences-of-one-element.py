"""
3410. Maximize Subarray Sum After Removing All Occurrences of One Element
https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

Pattern: 06 - Kadane's Pattern

---
APPROACH: For each candidate element to remove, run a modified Kadane.
- Key insight: only negative elements are worth removing.
- For each unique negative value v, run Kadane treating all occurrences of v as 0 (removed).
- Also run standard Kadane (remove nothing).
- Optimization: track running contribution of removing each negative value seen so far.

Time: O(n * unique_negatives) ~ O(n * n) worst case  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        # Approach: for each unique negative value, run Kadane skipping that value
        # Plus run normal Kadane
        neg_vals = set(x for x in nums if x < 0)

        ans = max(nums)  # at least pick one element

        # Normal Kadane
        cur = 0
        for x in nums:
            cur += x
            if cur > ans:
                ans = cur
            if cur < 0:
                cur = 0

        # Kadane removing all occurrences of each negative value
        for v in neg_vals:
            cur = 0
            best = float('-inf')
            for x in nums:
                if x == v:
                    continue
                cur += x
                if cur > best:
                    best = cur
                if cur < 0:
                    cur = 0
            if best > ans:
                ans = best

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSubarraySum([-3, 2, -2, -1, 3, -2, 3]) == 7
    assert sol.maxSubarraySum([1, 2, 3, 4]) == 10
    assert sol.maxSubarraySum([-1, -2, -3]) == -1
    assert sol.maxSubarraySum([5, -2, 5, -2, 5]) == 15

    print("Solution: all tests passed")
