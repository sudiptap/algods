"""
546. Remove Boxes (Hard)
https://leetcode.com/problems/remove-boxes/

Given several boxes with different colors represented by positive integers.
You may remove boxes in rounds; each round you pick a contiguous group of
boxes of the same color (say k boxes), remove them, and earn k*k points.
Return the maximum points you can get.

Pattern: Interval DP
- dp[i][j][k] = maximum points obtainable from boxes[i..j] when there are
  k extra boxes identical to boxes[i] already attached to its left.
- Base case: dp[i][i][k] = (k+1)^2 (remove boxes[i] together with k
  copies already attached).
- Transition option 1: remove boxes[i] with its k attached copies
  immediately -> (k+1)^2 + dp[i+1][j][0].
- Transition option 2: for each m in (i+1..j) where boxes[m] == boxes[i],
  merge boxes[i] with boxes[m] by first removing boxes[i+1..m-1], then
  solving the rest with one more attached copy:
  dp[i][j][k] = max(dp[i+1][m-1][0] + dp[m][j][k+1]).

Time:  O(n^4)  (three dimensions each up to n, transition O(n))
Space: O(n^3)
"""

from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """Return the maximum points from removing all boxes.

        Args:
            boxes: List of box colors, 1 <= len(boxes) <= 100.

        Returns:
            Maximum points achievable.
        """
        n = len(boxes)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, k: int) -> int:
            """Max points from boxes[i..j] with k extra copies of boxes[i] on the left."""
            if i > j:
                return 0
            # Optimization: absorb consecutive duplicates of boxes[i]
            while i + 1 <= j and boxes[i + 1] == boxes[i]:
                i += 1
                k += 1

            # Option 1: remove boxes[i] together with k attached copies
            result = (k + 1) * (k + 1) + dp(i + 1, j, 0)

            # Option 2: try merging boxes[i] with a later box of the same color
            for m in range(i + 2, j + 1):
                if boxes[m] == boxes[i]:
                    result = max(result, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))

            return result

        return dp(0, n - 1, 0)


# ---------- tests ----------
def test_remove_boxes():
    sol = Solution()

    # Example 1: [1,3,2,2,2,3,4,3,1]
    # Optimal removal yields 23
    assert sol.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23

    # Example 2: [1,1,1]
    # Remove all 3 at once -> 9
    assert sol.removeBoxes([1, 1, 1]) == 9

    # Example 3: single box -> 1
    assert sol.removeBoxes([1]) == 1

    # All same color: n^2 points
    assert sol.removeBoxes([5, 5, 5, 5]) == 16

    # Two colors alternating: [1,2,1,2] -> best is 1+1+1+1 = 4
    # (cannot merge non-contiguous same-color without removing between)
    # Actually [1,2,1,2]: remove 2->1, remove 2->1, remove [1,1]->4 => 6
    assert sol.removeBoxes([1, 2, 1, 2]) == 6

    # Empty-ish: two boxes same color
    assert sol.removeBoxes([3, 3]) == 4

    print("All tests passed for 546. Remove Boxes")


if __name__ == "__main__":
    test_remove_boxes()
