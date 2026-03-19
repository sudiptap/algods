"""
2919. Minimum Increment Operations to Make Array Beautiful
https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

Pattern: 19 - Linear DP (sliding window of size 3)

---
APPROACH: For every window of 3 consecutive elements, at least one must be >= k.
dp[i] = min cost to make array beautiful up to index i, where nums[i] is the
last element made >= k. Transition: dp[i] = cost_i + min(dp[i-1], dp[i-2], dp[i-3]).

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i] = min cost assuming we make nums[i] >= k (and all windows covered up to i)
        # cost to make nums[i] >= k: max(0, k - nums[i])

        # Use 3 variables for dp[i-1], dp[i-2], dp[i-3]
        a = b = c = 0  # dp for positions -3, -2, -1 (all 0)

        for i in range(n):
            cost = max(0, k - nums[i])
            new = min(a, b, c) + cost
            a, b, c = b, c, new

        return min(a, b, c)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minIncrementOperations([2, 3, 0, 0, 2], 4) == 3
    assert sol.minIncrementOperations([0, 1, 3, 3], 5) == 2
    assert sol.minIncrementOperations([1, 1, 2], 1) == 0

    print("All tests passed!")
