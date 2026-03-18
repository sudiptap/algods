"""
2304. Minimum Path Cost in a Grid (Medium)
https://leetcode.com/problems/minimum-path-cost-in-a-grid/

Pattern: DP on Grids

Given an m x n grid of non-negative integers and a moveCost array where
moveCost[v][k] is the cost to move from a cell with value v to column k in the
next row, return the minimum cost of a path from any cell in the first row to
any cell in the last row. The path cost is the sum of cell values plus move costs.

Approach:
    Use a 1D DP array. Initialize dp[j] = grid[0][j]. For each subsequent row,
    compute new_dp[k] = min over all j of (dp[j] + moveCost[grid[i-1][j]][k] + grid[i][k]).
    Answer is min(dp) after processing all rows.

Time:  O(m * n^2)
Space: O(n)
"""

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        """Return the minimum cost path from first row to last row."""
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]  # cost to reach each cell in first row

        for i in range(1, m):
            new_dp = [float('inf')] * n
            for k in range(n):
                for j in range(n):
                    cost = dp[j] + moveCost[grid[i - 1][j]][k] + grid[i][k]
                    new_dp[k] = min(new_dp[k], cost)
            dp = new_dp

        return min(dp)


# ---------- Tests ----------
import unittest


class TestMinPathCost(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        grid = [[5, 3], [4, 0], [2, 1]]
        moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
        self.assertEqual(self.sol.minPathCost(grid, moveCost), 17)

    def test_example2(self):
        grid = [[5, 1, 2], [4, 0, 3]]
        moveCost = [[12, 10, 15], [20, 23, 8], [21, 7, 1],
                     [8, 1, 13], [9, 10, 25], [5, 3, 2]]
        self.assertEqual(self.sol.minPathCost(grid, moveCost), 6)

    def test_single_row(self):
        grid = [[1, 2, 3]]
        moveCost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.sol.minPathCost(grid, moveCost), 1)

    def test_single_column(self):
        grid = [[5], [3], [1]]
        moveCost = [[2], [4], [6], [1], [3], [5]]
        # Path: 5 + moveCost[5][0] + 3 + moveCost[3][0] + 1
        # moveCost[5][0] = 5, moveCost[3][0] = 1
        # total = 5 + 5 + 3 + 1 + 1 = 15
        self.assertEqual(self.sol.minPathCost(grid, moveCost), 15)

    def test_two_rows(self):
        grid = [[1, 2], [3, 4]]
        moveCost = [[5, 6], [7, 8], [0, 0], [0, 0]]
        # moveCost indexed by cell value. grid[0][0]=1 -> moveCost[1]=[7,8]
        # grid[0][1]=2 -> moveCost[2]=[0,0]
        # From (0,0) val=1: to col0 = 1+7+3=11, to col1 = 1+8+4=13
        # From (0,1) val=2: to col0 = 2+0+3=5, to col1 = 2+0+4=6
        # min = 5
        self.assertEqual(self.sol.minPathCost(grid, moveCost), 5)


if __name__ == "__main__":
    unittest.main()
