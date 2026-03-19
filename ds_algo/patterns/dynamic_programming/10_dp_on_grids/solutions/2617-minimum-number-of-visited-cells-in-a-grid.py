"""
2617. Minimum Number of Visited Cells in a Grid
https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

Pattern: 10 - DP on Grids (BFS with pruning using heaps)

---
APPROACH: Process cells in BFS order. For each row and column, maintain a
min-heap of (dist, index) for reachable but unprocessed positions. For cell
(i,j) with value v, it can reach cells in same row up to j+v or same column
up to i+v. Use heaps per row/col to efficiently find next reachable cells.

Time: O(m*n * log(m*n))  Space: O(m*n)
---
"""

from typing import List
from collections import deque
import heapq


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1

        # For each row, min-heap of (dist, col) for cells that can still propagate
        row_heaps = [[] for _ in range(m)]
        col_heaps = [[] for _ in range(n)]

        # Add (0,0) to row 0 and col 0 heaps
        if grid[0][0] > 0:
            heapq.heappush(row_heaps[0], (1, 0))  # (dist, col)
            heapq.heappush(col_heaps[0], (1, 0))  # (dist, row)

        for i in range(m):
            for j in range(n):
                # Try to reach (i,j) from row_heaps[i] and col_heaps[j]
                # From row heap: cells (i, c) with c < j and c + grid[i][c] >= j
                while row_heaps[i] and row_heaps[i][0][1] + grid[i][row_heaps[i][0][1]] < j:
                    heapq.heappop(row_heaps[i])
                if row_heaps[i] and (dist[i][j] == -1 or row_heaps[i][0][0] + 1 < dist[i][j]):
                    dist[i][j] = row_heaps[i][0][0] + 1

                # From col heap: cells (r, j) with r < i and r + grid[r][j] >= i
                while col_heaps[j] and col_heaps[j][0][1] + grid[col_heaps[j][0][1]][j] < i:
                    heapq.heappop(col_heaps[j])
                if col_heaps[j] and (dist[i][j] == -1 or col_heaps[j][0][0] + 1 < dist[i][j]):
                    dist[i][j] = col_heaps[j][0][0] + 1

                if i == 0 and j == 0:
                    dist[i][j] = 1
                    continue

                if dist[i][j] != -1 and grid[i][j] > 0:
                    heapq.heappush(row_heaps[i], (dist[i][j], j))
                    heapq.heappush(col_heaps[j], (dist[i][j], i))

        return dist[m - 1][n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumVisitedCells([[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]) == 4
    assert sol.minimumVisitedCells([[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]) == 3
    assert sol.minimumVisitedCells([[2, 1, 0], [1, 0, 0]]) == -1

    print("All tests passed!")
