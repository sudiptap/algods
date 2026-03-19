"""
562. Longest Line of Consecutive One in Matrix (Medium)
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

Pattern: DP on Grids

Given an m x n binary matrix, find the longest line of consecutive 1s
in the matrix. The line could be horizontal, vertical, diagonal, or
anti-diagonal.

Approach:
    For each cell (i, j) with value 1, track 4 DP values:
    - horizontal: consecutive 1s ending at (i, j) going left
    - vertical: consecutive 1s ending at (i, j) going up
    - diagonal: consecutive 1s ending at (i, j) going upper-left
    - anti-diagonal: consecutive 1s ending at (i, j) going upper-right

    dp[i][j] = (horiz, vert, diag, anti_diag)

Time:  O(m * n)
Space: O(m * n)  (can be optimized to O(n) with rolling rows)
"""

from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        """Return the length of the longest line of consecutive 1s."""
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        # dp[j] = (horiz, vert, diag, anti_diag)
        dp = [[(0, 0, 0, 0)] * n for _ in range(m)]
        best = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    h = (dp[i][j - 1][0] + 1) if j > 0 else 1
                    v = (dp[i - 1][j][1] + 1) if i > 0 else 1
                    d = (dp[i - 1][j - 1][2] + 1) if i > 0 and j > 0 else 1
                    a = (dp[i - 1][j + 1][3] + 1) if i > 0 and j < n - 1 else 1
                    dp[i][j] = (h, v, d, a)
                    best = max(best, h, v, d, a)

        return best


# ───────────────────────── tests ─────────────────────────

def test_example1():
    mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
    assert Solution().longestLine(mat) == 3

def test_example2():
    mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
    assert Solution().longestLine(mat) == 4

def test_single_one():
    assert Solution().longestLine([[1]]) == 1

def test_all_zeros():
    assert Solution().longestLine([[0,0],[0,0]]) == 0

def test_diagonal():
    mat = [[1,0,0],[0,1,0],[0,0,1]]
    assert Solution().longestLine(mat) == 3

def test_anti_diagonal():
    mat = [[0,0,1],[0,1,0],[1,0,0]]
    assert Solution().longestLine(mat) == 3

def test_vertical():
    mat = [[1],[1],[1],[0]]
    assert Solution().longestLine(mat) == 3

def test_empty():
    assert Solution().longestLine([]) == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
