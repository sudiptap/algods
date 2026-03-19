"""
3276. Select Cells in Grid With Maximum Score (Hard)

Pattern: 11_bitmask_dp
- Select cells from a grid such that no two selected cells are from the same row
  and all selected values are distinct. Maximize the sum of selected values.

Approach:
- Group cells by value: for each distinct value, record which rows contain it.
- Sort distinct values descending. Use dp[mask] where mask tracks which rows are used.
- For each value, either skip it or pick it from one of its available rows (if that row
  is not already in the mask).

Complexity:
- Time:  O(V * 2^m * m) where V = number of distinct values, m = number of rows
- Space: O(2^m)
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        # Map value -> set of row indices
        val_rows = defaultdict(set)
        for i in range(m):
            for v in grid[i]:
                val_rows[v].add(i)

        # Sort values descending for pruning (not strictly needed but nice)
        values = sorted(val_rows.keys(), reverse=True)

        dp = [0] * (1 << m)
        # Process each value: either skip or pick from one available row
        for v in values:
            rows = list(val_rows[v])
            # Iterate masks in reverse to avoid using same value twice
            for mask in range((1 << m) - 1, -1, -1):
                for r in rows:
                    if not (mask & (1 << r)):
                        new_mask = mask | (1 << r)
                        dp[new_mask] = max(dp[new_mask], dp[mask] + v)

        return max(dp)


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxScore([[1, 2, 3], [4, 3, 2], [1, 1, 1]]) == 8

    # Example 2
    assert sol.maxScore([[8, 7, 6], [8, 3, 2]]) == 15

    # Single cell
    assert sol.maxScore([[5]]) == 5

    # All same values
    assert sol.maxScore([[1, 1], [1, 1]]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
