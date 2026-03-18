"""
1463. Cherry Pickup II (Hard)
https://leetcode.com/problems/cherry-pickup-ii/

Pattern: DP on Grids

Given a rows x cols grid, two robots start at the top-left (0,0) and
top-right (0, cols-1). Each robot moves down one row per step and can
shift one column left, stay, or shift one column right. They collect
cherries from visited cells. If both visit the same cell, only one
collects. Return the maximum total cherries collected.

Approach:
    dp[row][c1][c2] = max cherries both robots can collect from row
    onward when Robot 1 is at column c1 and Robot 2 is at column c2.

    At each row, try all 9 combinations of moves (3 for each robot).
    If c1 == c2, only count cherries once.

    We iterate bottom-up. Answer is dp[0][0][cols-1].

Time:  O(rows * cols^2 * 9)
Space: O(cols^2)  — only need current and next row.
"""

from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Return the maximum cherries two robots can collect."""
        rows, cols = len(grid), len(grid[0])

        # next_dp[c1][c2] = best from row+1 onward
        next_dp = [[0] * cols for _ in range(cols)]

        for row in range(rows - 1, -1, -1):
            cur_dp = [[0] * cols for _ in range(cols)]
            for c1 in range(cols):
                for c2 in range(c1, cols):  # c1 <= c2 by symmetry
                    # Cherries collected at this row
                    cherries = grid[row][c1]
                    if c1 != c2:
                        cherries += grid[row][c2]

                    # Best move from next row
                    best = 0
                    if row < rows - 1:
                        for dc1 in (-1, 0, 1):
                            nc1 = c1 + dc1
                            if nc1 < 0 or nc1 >= cols:
                                continue
                            for dc2 in (-1, 0, 1):
                                nc2 = c2 + dc2
                                if nc2 < 0 or nc2 >= cols:
                                    continue
                                # Use symmetry: ensure nc1 <= nc2
                                a, b = min(nc1, nc2), max(nc1, nc2)
                                best = max(best, next_dp[a][b])

                    cur_dp[c1][c2] = cherries + best

            next_dp = cur_dp

        return next_dp[0][cols - 1]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    grid = [
        [3, 1, 1],
        [2, 5, 1],
        [1, 5, 5],
        [2, 1, 1],
    ]
    assert Solution().cherryPickup(grid) == 24

def test_example2():
    grid = [
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0],
        [1, 0, 2, 3, 0, 0, 6],
    ]
    assert Solution().cherryPickup(grid) == 28

def test_single_row():
    assert Solution().cherryPickup([[1, 2, 3]]) == 4  # robot1 at 0, robot2 at 2

def test_two_cols():
    grid = [[5, 3], [1, 2]]
    assert Solution().cherryPickup(grid) == 11

def test_all_zeros():
    grid = [[0, 0], [0, 0]]
    assert Solution().cherryPickup(grid) == 0

def test_single_column():
    grid = [[5], [3], [1]]
    # Both robots at column 0 (same cell), collect each row once
    assert Solution().cherryPickup(grid) == 9


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
