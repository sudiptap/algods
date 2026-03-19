"""
2560. House Robber IV
https://leetcode.com/problems/house-robber-iv/

Pattern: 19 - Linear DP (Binary Search + Greedy)

---
APPROACH: Binary search on the answer (max stolen value) + greedy check
- Binary search on the maximum value we're allowed to steal (capability).
- For a given cap, greedily check if we can rob >= k houses where each has
  value <= cap and no two are adjacent.
- Greedy: scan left to right, rob a house if value <= cap and previous wasn't robbed.

Time: O(n * log(max_val))  Space: O(1)
---
"""

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2  # skip adjacent
                else:
                    i += 1
            return count >= k

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_rob(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minCapability([2, 3, 5, 9], 2) == 5
    assert sol.minCapability([2, 7, 9, 3, 1], 2) == 2
    assert sol.minCapability([1], 1) == 1

    print("all tests passed")
