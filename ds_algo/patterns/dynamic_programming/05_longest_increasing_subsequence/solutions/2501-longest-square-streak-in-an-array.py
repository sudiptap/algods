"""
2501. Longest Square Streak in an Array
https://leetcode.com/problems/longest-square-streak-in-an-array/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: Sort + DP with set lookup
- Sort array. For each x, dp[x] = dp[sqrt(x)] + 1 if sqrt(x) is perfect square
  and in the set.
- Answer: max dp[x] if >= 2, else -1.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List
import math


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        dp = {}
        ans = -1

        for x in sorted(nums):
            sq = int(math.isqrt(x))
            if sq * sq == x and sq in dp:
                dp[x] = dp[sq] + 1
            else:
                dp[x] = 1
            if dp[x] >= 2:
                ans = max(ans, dp[x])

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3
    assert sol.longestSquareStreak([2, 3, 5, 6, 7]) == -1
    assert sol.longestSquareStreak([2, 4, 16, 256]) == 4

    print("all tests passed")
