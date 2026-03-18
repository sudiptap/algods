"""
2684. Maximum Number of Moves in a Grid
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

Pattern: 10 - DP on Grids

---
APPROACH: Column-by-column BFS/DP
- Process the grid column by column (left to right).
- Track which cells in the current column are reachable.
- From each reachable cell (r, c), try moving to (r-1, c+1), (r, c+1), (r+1, c+1)
  if the destination has a strictly greater value.
- The answer is the rightmost column index reached (= max number of moves).

Time:  O(m * n)
Space: O(m)
---
"""

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """Return the maximum number of moves starting from any cell in column 0."""
        m, n = len(grid), len(grid[0])
        # Start: all rows in column 0 are reachable
        current = set(range(m))
        ans = 0

        for col in range(n - 1):
            nxt = set()
            for r in current:
                for dr in (-1, 0, 1):
                    nr = r + dr
                    if 0 <= nr < m and grid[nr][col + 1] > grid[r][col]:
                        nxt.add(nr)
            if not nxt:
                break
            current = nxt
            ans = col + 1

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]) == 3
    # Example 2
    assert sol.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
    # Single column
    assert sol.maxMoves([[1], [2], [3]]) == 0
    # Single row
    assert sol.maxMoves([[1, 2, 3, 4]]) == 3
    # All equal
    assert sol.maxMoves([[5, 5], [5, 5]]) == 0
    # 1x1 grid
    assert sol.maxMoves([[1]]) == 0

    print("Solution: all tests passed")
