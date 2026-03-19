"""
2321. Maximum Score Of Spliced Array
https://leetcode.com/problems/maximum-score-of-spliced-array/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Kadane on difference arrays
- Splicing a subarray from nums2 into nums1 changes sum1 by sum of (nums2[i]-nums1[i])
  over the spliced range. We want to maximize this gain = max subarray of (nums2-nums1).
- Similarly for splicing nums1 into nums2.
- Answer = max(sum1 + maxSubarray(nums2-nums1), sum2 + maxSubarray(nums1-nums2))

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def max_gain(a, b):
            """Max subarray sum of (b[i] - a[i]), representing gain of splicing b into a."""
            cur = 0
            best = 0
            for x, y in zip(a, b):
                cur += y - x
                if cur < 0:
                    cur = 0
                best = max(best, cur)
            return best

        s1, s2 = sum(nums1), sum(nums2)
        return max(s1 + max_gain(nums1, nums2), s2 + max_gain(nums2, nums1))


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumsSplicedArray([60,60,60], [10,90,10]) == 210
    assert sol.maximumsSplicedArray([20,40,20,70,30], [50,20,50,40,20]) == 220
    assert sol.maximumsSplicedArray([7,11,13], [1,1,1]) == 31

    print("all tests passed")
