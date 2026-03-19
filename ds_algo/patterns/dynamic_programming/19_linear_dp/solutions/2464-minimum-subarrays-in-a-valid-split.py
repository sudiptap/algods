"""
2464. Minimum Subarrays in a Valid Split
https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

Pattern: 19 - Linear DP

---
APPROACH: dp[i] = min splits for nums[:i]
- dp[0] = 0 (empty prefix)
- dp[i] = min(dp[j] + 1) for all j < i where gcd(nums[j], nums[i-1]) > 1
  (subarray nums[j..i-1] is valid if first and last share common factor > 1).
- Answer: dp[n] or -1 if not reachable.

Time: O(n^2 * log(max_val))  Space: O(n)
---
"""

from typing import List
from math import gcd


class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] < float('inf') and gcd(nums[j], nums[i - 1]) > 1:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] < float('inf') else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.validSubarraySplit([2, 6, 3, 4, 3]) == 2
    assert sol.validSubarraySplit([3, 5]) == 2
    assert sol.validSubarraySplit([1, 2, 1]) == -1
    assert sol.validSubarraySplit([6]) == 1

    print("all tests passed")
