"""
2809. Minimum Time to Make Array Sum At Most x
https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

Pattern: 19 - Linear DP (Sort by growth rate, dp on removal order)

---
APPROACH: At time t, element i has value nums1[i] + t*nums2[i]. When we zero
an element at time t_k, we save nums1[i] + t_k*nums2[i]. Sort by nums2.
dp[j] = max total savings using j operations on first i elements.
Transition: dp[j] = max(dp[j], dp[j-1] + nums1[i] + j*nums2[i]).
Check each t from 0..n.

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        pairs = sorted(zip(nums2, nums1))

        # dp[j] = max savings using exactly j resets
        dp = [0] * (n + 1)

        for i in range(n):
            b, a = pairs[i]
            for j in range(i + 1, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + a + b * j)

        s1 = sum(nums1)
        s2 = sum(nums2)

        for t in range(n + 1):
            if s1 + s2 * t - dp[t] <= x:
                return t

        return -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumTime([1, 2, 3], [1, 2, 3], 4) == 3
    assert sol.minimumTime([1, 2, 3], [3, 3, 3], 4) == -1

    print("All tests passed!")
