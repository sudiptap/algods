"""
3469. Find Minimum Cost to Remove Array Elements
https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

Pattern: 19 - Linear DP (dp[last][i])

---
APPROACH: Always consider the first 3 elements. Remove 2 of them (cost = max of those 2).
The remaining element stays at front. Repeat until < 3 elements remain, then remove rest
(cost = max of remaining).
- dp(last, i): min cost when 'last' is the index of the surviving front element and
  i is the start of unprocessed elements.
- At each step, next pair is (i, i+1). Three choices: remove any 2 of {last, i, i+1}.

Time: O(n^2)  Space: O(n^2)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(last, i):
            if i == n:
                return nums[last]
            if i == n - 1:
                return max(nums[last], nums[i])
            # Three choices from {last, i, i+1}:
            a = max(nums[i], nums[i + 1]) + dp(last, i + 2)      # remove i and i+1, keep last
            b = max(nums[last], nums[i + 1]) + dp(i, i + 2)      # remove last and i+1, keep i
            c = max(nums[last], nums[i]) + dp(i + 1, i + 2)      # remove last and i, keep i+1
            return min(a, b, c)

        return dp(0, 1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minCost([6, 2, 8, 4]) == 12
    assert sol.minCost([2, 1, 3, 3]) == 5
    assert sol.minCost([5]) == 5

    print("Solution: all tests passed")
