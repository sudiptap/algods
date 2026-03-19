"""
2439. Minimize Maximum of Array
https://leetcode.com/problems/minimize-maximum-of-array/

Pattern: 19 - Linear DP

---
APPROACH: Prefix average (ceiling)
- We can move value from right to left (decrease nums[i], increase nums[i-1]).
- The minimum possible maximum is the max of ceil(prefix_sum[i+1] / (i+1))
  for all i from 0 to n-1.
- This works because the first i+1 elements must hold at least prefix_sum[i+1]
  total, so at least one must be >= ceil(prefix_sum[i+1]/(i+1)).

Time: O(n)  Space: O(1)
---
"""

from typing import List
import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            ans = max(ans, math.ceil(prefix / (i + 1)))

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimizeArrayValue([3, 7, 1, 6]) == 5
    assert sol.minimizeArrayValue([10, 1]) == 10
    assert sol.minimizeArrayValue([1]) == 1
    assert sol.minimizeArrayValue([6, 9]) == 8

    print("all tests passed")
