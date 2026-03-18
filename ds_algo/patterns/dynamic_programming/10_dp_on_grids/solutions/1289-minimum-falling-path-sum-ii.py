"""
1289. Minimum Falling Path Sum II (Hard)
https://leetcode.com/problems/minimum-falling-path-sum-ii/

Pattern: 10 - DP on Grids

---
APPROACH: DP tracking first and second minimums
- Like 931 Minimum Falling Path Sum, but you cannot pick the same column
  in consecutive rows.
- Naive O(n^3) for each cell checks all columns in the previous row.
- Optimise to O(n^2) by tracking min1 (smallest), min2 (second smallest),
  and min1_col from the previous row.
- For column j in the current row:
    - If j != min1_col, add min1 value.
    - Otherwise add min2 value.

Time:  O(n^2)
Space: O(1) — modify grid in place (or O(n) with a copy)
---
"""

from typing import List
import math


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """Return the minimum falling path sum where no two consecutive
        rows use the same column."""
        n = len(grid)
        if n == 1:
            return min(grid[0])

        for i in range(1, n):
            # Find min1, min2 from previous row
            min1 = min2 = math.inf
            min1_col = -1
            for j in range(n):
                if grid[i - 1][j] < min1:
                    min2 = min1
                    min1 = grid[i - 1][j]
                    min1_col = j
                elif grid[i - 1][j] < min2:
                    min2 = grid[i - 1][j]

            for j in range(n):
                if j != min1_col:
                    grid[i][j] += min1
                else:
                    grid[i][j] += min2

        return min(grid[-1])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13

    # Example 2
    assert sol.minFallingPathSum([[7]]) == 7

    # Two rows
    assert sol.minFallingPathSum([[1, 2], [3, 4]]) == 5  # 1+4 or 2+3

    # Identical values
    assert sol.minFallingPathSum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3

    # Negative values: pick -2 (col 1) then -3 (col 0) = -5
    assert sol.minFallingPathSum([[-1, -2], [-3, -4]]) == -5

    print("all tests passed")
