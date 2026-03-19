"""
2556. Disconnect Path in a Binary Matrix by at Most One Flip
https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

Pattern: 10 - DP on Grids

---
APPROACH: Find two node-disjoint paths; if they don't exist, answer is true
- If there's only one path (no two node-disjoint paths from (0,0) to (m-1,n-1)),
  then flipping one cell on that path disconnects it.
- Find first path greedily (prefer going down). Mark cells as visited (flip to 0).
  Restore start and end. Find second path. If second path doesn't exist, return True.

Time: O(m * n)  Space: O(m * n)
---
"""

from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def find_path():
            """Greedily find a path from (0,0) to (m-1,n-1) going right/down.
            Mark used cells as 0. Returns True if path found."""
            # DFS preferring down then right
            # Actually just use a greedy approach on the grid
            # Go from top-left, always try down first, then right
            visited = [[False] * n for _ in range(m)]

            def dfs(i, j):
                if i == m - 1 and j == n - 1:
                    return True
                visited[i][j] = True
                # Try down
                if i + 1 < m and grid[i + 1][j] == 1 and not visited[i + 1][j]:
                    if dfs(i + 1, j):
                        grid[i][j] = 0  # mark as used
                        return True
                # Try right
                if j + 1 < n and grid[i][j + 1] == 1 and not visited[i][j + 1]:
                    if dfs(i, j + 1):
                        grid[i][j] = 0
                        return True
                return False

            result = dfs(0, 0)
            # Restore start and end
            grid[0][0] = 1
            grid[m - 1][n - 1] = 1
            return result

        if not find_path():
            return True  # already disconnected

        if not find_path():
            return True  # only one path existed

        return False


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.isPossibleToCutPath([[1,1,1],[1,0,0],[1,1,1]]) == True
    assert sol.isPossibleToCutPath([[1,1,1],[1,0,1],[1,1,1]]) == False
    assert sol.isPossibleToCutPath([[1]]) == False

    print("all tests passed")
