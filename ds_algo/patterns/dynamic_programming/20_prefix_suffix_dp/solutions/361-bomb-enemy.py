"""
361. Bomb Enemy (Medium)

Given an m x n grid where each cell is either:
- 'W' (wall), 'E' (enemy), or '0' (empty),
return the maximum number of enemies you can kill by placing a bomb in
one empty cell. The bomb kills all enemies in the same row and column
until a wall is hit.

Approach (prefix/suffix DP - row/col segment precomputation):
- For each row, sweep left-to-right counting enemies between walls.
  When hitting a wall or end-of-row, assign that count to all empty
  cells in that segment (row_kills).
- Do the same for each column (col_kills), sweeping top-to-bottom.
- Answer = max(row_kills[i][j] + col_kills[i][j]) over all empty cells.

Optimized single-pass approach:
- Maintain a running row_count that resets at each wall/row start.
- Maintain col_count[j] that resets when grid[i][j] == 'W' or i == 0.
- Recompute row_count when j == 0 or grid[i][j-1] == 'W' by scanning
  right until a wall.
- Recompute col_count[j] when i == 0 or grid[i-1][j] == 'W' by scanning
  down until a wall.

Time:  O(m * n) - each cell is visited a constant number of times.
Space: O(n) for col_count array.
"""

from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """Return max enemies killed by placing a bomb in one empty cell."""
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        col_counts = [0] * cols
        result = 0

        for i in range(rows):
            for j in range(cols):
                # Recompute row kills when at start of row or after a wall
                if j == 0 or grid[i][j - 1] == 'W':
                    row_count = 0
                    k = j
                    while k < cols and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_count += 1
                        k += 1

                # Recompute col kills when at start of col or after a wall
                if i == 0 or grid[i - 1][j] == 'W':
                    col_counts[j] = 0
                    k = i
                    while k < rows and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_counts[j] += 1
                        k += 1

                # If current cell is empty, consider placing bomb here
                if grid[i][j] == '0':
                    result = max(result, row_count + col_counts[j])

        return result


# ---------- Tests ----------

def test_basic():
    sol = Solution()
    grid = [
        ["0", "E", "0", "0"],
        ["E", "0", "W", "E"],
        ["0", "E", "0", "0"],
    ]
    # Placing bomb at (1,1) kills 3 enemies: row E at (1,0), col E at (0,1) and (2,1)
    assert sol.maxKilledEnemies(grid) == 3

def test_all_walls():
    sol = Solution()
    grid = [["W", "W"], ["W", "W"]]
    assert sol.maxKilledEnemies(grid) == 0

def test_no_enemies():
    sol = Solution()
    grid = [["0", "0"], ["0", "0"]]
    assert sol.maxKilledEnemies(grid) == 0

def test_single_empty():
    sol = Solution()
    grid = [["E", "0", "E"]]
    # Bomb at (0,1) kills 2 enemies
    assert sol.maxKilledEnemies(grid) == 2

def test_empty_grid():
    sol = Solution()
    assert sol.maxKilledEnemies([]) == 0

def test_wall_blocks():
    sol = Solution()
    grid = [
        ["E", "W", "0", "E"],
    ]
    # Bomb at (0,2) can only reach E at (0,3), wall blocks E at (0,0)
    assert sol.maxKilledEnemies(grid) == 1

def test_column_wall_blocks():
    sol = Solution()
    grid = [
        ["E"],
        ["W"],
        ["0"],
        ["E"],
    ]
    # Bomb at (2,0): wall blocks E at (0,0), only kills E at (3,0)
    assert sol.maxKilledEnemies(grid) == 1

def test_no_empty_cells():
    sol = Solution()
    grid = [["E", "E"], ["E", "E"]]
    assert sol.maxKilledEnemies(grid) == 0

def test_larger_grid():
    sol = Solution()
    grid = [
        ["0", "E", "0", "0", "E"],
        ["E", "0", "E", "W", "0"],
        ["0", "E", "0", "0", "E"],
        ["W", "0", "E", "0", "0"],
    ]
    # (2,0) -> row: E at (2,1); col: E at (1,0) => 2
    # (1,1) -> row: E at (1,0), E at (1,2); col: E at (0,1), E at (2,1) => 4
    assert sol.maxKilledEnemies(grid) == 4


if __name__ == "__main__":
    test_basic()
    test_all_walls()
    test_no_enemies()
    test_single_empty()
    test_empty_grid()
    test_wall_blocks()
    test_column_wall_blocks()
    test_no_empty_cells()
    test_larger_grid()
    print("All tests passed!")
