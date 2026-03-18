"""
329. Longest Increasing Path in a Matrix (Hard)
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an m x n integers matrix, return the length of the longest increasing
path. From each cell you can move in four directions (up, down, left, right).
You may NOT move diagonally or outside the boundary.

Pattern: DP on Grids (DFS + Memoization)
- memo[i][j] = length of the longest increasing path starting at (i, j).
- DFS from each cell; recurse to neighbors with strictly greater value.
- No visited set needed: strictly increasing guarantees no cycles.
- Answer = max(memo[i][j]) over all cells.

Time:  O(m * n) - each cell computed once
Space: O(m * n) - memo table + recursion stack
"""

from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Return the length of the longest strictly increasing path.

        Args:
            matrix: m x n grid of integers.

        Returns:
            Length of the longest increasing path.
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        @lru_cache(maxsize=None)
        def dfs(r: int, c: int) -> int:
            best = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        result = max(dfs(r, c) for r in range(m) for c in range(n))
        dfs.cache_clear()
        return result


# ---------- tests ----------
def test_longest_increasing_path():
    sol = Solution()

    # Example 1: path 1->2->6->9 length 4
    matrix1 = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1],
    ]
    assert sol.longestIncreasingPath(matrix1) == 4

    # Example 2: path 3->4->5->6 length 4
    matrix2 = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1],
    ]
    assert sol.longestIncreasingPath(matrix2) == 4

    # Single cell
    assert sol.longestIncreasingPath([[1]]) == 1

    # All same values -> every path length 1
    assert sol.longestIncreasingPath([[7, 7], [7, 7]]) == 1

    # Strictly increasing row
    assert sol.longestIncreasingPath([[1, 2, 3, 4, 5]]) == 5

    # 2x2
    matrix3 = [[1, 2], [4, 3]]
    assert sol.longestIncreasingPath(matrix3) == 4  # 1->2->3->4? No: 1->2->3 is 3, 1->4 is 2. Actually 1<2, 2<3, but 3<4 so 1->2->3->4 via path? Check adjacency.
    # 1(0,0)->2(0,1) ok, 2->?(1,1)=3>2 ok, 3->?(1,0)=4>3 ok => length 4
    assert sol.longestIncreasingPath(matrix3) == 4

    print("All tests passed for 329. Longest Increasing Path in a Matrix")


if __name__ == "__main__":
    test_longest_increasing_path()
