"""
2713. Maximum Strictly Increasing Cells in a Matrix
https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

Pattern: 10 - DP on Grids (Sort by value, DP per row/col)

---
APPROACH: Sort all cells by value. Process groups of same value together.
For each cell, dp = 1 + max(best in its row, best in its col) using only
previously processed (smaller) values. Update row/col bests after processing
each group.

Time: O(m*n * log(m*n))  Space: O(m*n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_best = [0] * m
        col_best = [0] * n

        # Group cells by value
        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[mat[i][j]].append((i, j))

        ans = 0
        for val in sorted(groups.keys()):
            cells = groups[val]
            # Compute dp for all cells in this group before updating row/col bests
            results = []
            for i, j in cells:
                dp = max(row_best[i], col_best[j]) + 1
                results.append((i, j, dp))
                ans = max(ans, dp)
            # Now update row/col bests
            for i, j, dp in results:
                row_best[i] = max(row_best[i], dp)
                col_best[j] = max(col_best[j], dp)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxIncreasingCells([[3, 1], [3, 4]]) == 2
    assert sol.maxIncreasingCells([[1, 1], [1, 1]]) == 1
    assert sol.maxIncreasingCells([[3, 1, 6], [-9, 5, 7]]) == 4

    print("All tests passed!")
