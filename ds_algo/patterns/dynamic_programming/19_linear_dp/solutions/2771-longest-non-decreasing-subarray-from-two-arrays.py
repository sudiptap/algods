"""
2771. Longest Non-decreasing Subarray From Two Arrays
https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

Pattern: 19 - Linear DP (Track best ending from arr1/arr2)

---
APPROACH: dp1[i] = length of longest non-decreasing subarray ending at i,
choosing nums1[i]. dp2[i] = same but choosing nums2[i]. Transition checks
which previous choices allow non-decreasing continuation.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = dp2 = 1  # length ending at current index choosing nums1/nums2
        ans = 1

        for i in range(1, n):
            new_dp1 = 1
            new_dp2 = 1

            # Choose nums1[i]: can extend from nums1[i-1] or nums2[i-1]
            if nums1[i] >= nums1[i - 1]:
                new_dp1 = max(new_dp1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                new_dp1 = max(new_dp1, dp2 + 1)

            # Choose nums2[i]: can extend from nums1[i-1] or nums2[i-1]
            if nums2[i] >= nums1[i - 1]:
                new_dp2 = max(new_dp2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                new_dp2 = max(new_dp2, dp2 + 1)

            dp1, dp2 = new_dp1, new_dp2
            ans = max(ans, dp1, dp2)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxNonDecreasingLength([2, 3, 1], [1, 2, 1]) == 2
    assert sol.maxNonDecreasingLength([1, 3, 2, 1], [2, 2, 3, 4]) == 4
    assert sol.maxNonDecreasingLength([1, 1], [2, 2]) == 2

    print("All tests passed!")
