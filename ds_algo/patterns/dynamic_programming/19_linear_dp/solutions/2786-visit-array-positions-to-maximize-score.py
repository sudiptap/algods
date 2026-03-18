"""
2786. Visit Array Positions to Maximize Score
https://leetcode.com/problems/visit-array-positions-to-maximize-score/

Pattern: 19 - Linear DP

---
APPROACH: Track two states — best score ending on an even number and best
score ending on an odd number.
- Start at index 0 (must visit it). Its parity seeds the initial state.
- For each subsequent index i, we can extend from the same-parity best
  for free, or switch parity at a cost of x.
- Answer is the maximum of the two states at the end.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        """Return maximum score visiting positions where parity changes cost x."""
        # best[0] = best score ending on even, best[1] = best score ending on odd
        best = [float('-inf'), float('-inf')]
        best[nums[0] % 2] = nums[0]

        for i in range(1, len(nums)):
            p = nums[i] % 2
            # Either extend from same parity (free) or switch parity (cost x)
            val = nums[i] + max(best[p], best[1 - p] - x)
            best[p] = max(best[p], val)

        return max(best)


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.maxScore([2, 3, 6, 1, 9, 2], 5) == 13

    # Example 2
    assert sol.maxScore([2, 4, 6, 8], 3) == 20

    # Single element
    assert sol.maxScore([7], 10) == 7

    # All same parity
    assert sol.maxScore([1, 3, 5, 7], 100) == 16

    # Parity switch always beneficial despite cost
    assert sol.maxScore([10, 1], 0) == 11

    # Large cost makes switching bad
    assert sol.maxScore([1, 2, 3], 1000) == 4  # pick 1, skip 2, pick 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
