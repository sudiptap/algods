"""
542. 01 Matrix (Medium)
https://leetcode.com/problems/01-matrix/

Pattern: DP on Grids / Multi-source BFS

Given an m x n binary matrix mat, return the distance of the nearest 0
for each cell.

Approach:
    Multi-source BFS: start BFS from all cells that are 0 simultaneously.
    Each layer expands by 1 step. When we reach a cell with value 1 that
    hasn't been visited, its distance is the current BFS layer.

Time:  O(m * n)
Space: O(m * n)
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Return matrix of distances to nearest 0."""
        m, n = len(mat), len(mat[0])
        dist = [[float("inf")] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist


# ───────────────────────── tests ─────────────────────────

def test_example1():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().updateMatrix(mat) == [[0,0,0],[0,1,0],[0,0,0]]

def test_example2():
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    assert Solution().updateMatrix(mat) == [[0,0,0],[0,1,0],[1,2,1]]

def test_single_zero():
    mat = [[1,1],[1,0]]
    assert Solution().updateMatrix(mat) == [[2,1],[1,0]]

def test_all_zeros():
    mat = [[0,0],[0,0]]
    assert Solution().updateMatrix(mat) == [[0,0],[0,0]]

def test_single_cell():
    assert Solution().updateMatrix([[0]]) == [[0]]

def test_row():
    assert Solution().updateMatrix([[1,0,1,1]]) == [[1,0,1,2]]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
