"""
1770. Maximum Score from Performing Multiplication Operations
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

Pattern: 19 - Linear DP

---
APPROACH: Memoized DFS (Top-Down DP)
- At each step we pick either the leftmost or rightmost remaining element from nums.
- State: (i, left) where i = index into multipliers, left = how many taken from left.
  Then right elements taken = i - left, so right pointer = n - 1 - (i - left).
- dp(i, left) = max score from step i onward having taken 'left' from the left side.
- Base case: i == m -> return 0.
- Transition: dp(i, left) = max(
      multipliers[i] * nums[left] + dp(i+1, left+1),        # take from left
      multipliers[i] * nums[n-1-(i-left)] + dp(i+1, left)   # take from right
  )

Time: O(m^2)  Space: O(m^2) where m = len(multipliers)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        Top-down DP. State is (step index, count taken from left).
        The right index is derived: n - 1 - (step - left).
        """
        n, m = len(nums), len(multipliers)

        @lru_cache(maxsize=None)
        def dp(i: int, left: int) -> int:
            if i == m:
                return 0
            right_idx = n - 1 - (i - left)

            pick_left = multipliers[i] * nums[left] + dp(i + 1, left + 1)
            pick_right = multipliers[i] * nums[right_idx] + dp(i + 1, left)

            return max(pick_left, pick_right)

        return dp(0, 0)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maximumScore([1, 2, 3], [3, 2, 1]) == 14
    # Explanation: pick 3*3=9, then 2*2=4, then 1*1=1 -> 14

    # Example 2
    assert sol.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]) == 102

    # Single element
    assert sol.maximumScore([1], [1]) == 1

    # All from left
    assert sol.maximumScore([1, 2, 3, 4, 5], [1]) == 5  # pick 5 from right or 1 from left -> max is 5

    # Negative multipliers
    assert sol.maximumScore([9, 1], [-1]) == -1  # pick 1 * -1 = -1

    print("Solution: all tests passed")
