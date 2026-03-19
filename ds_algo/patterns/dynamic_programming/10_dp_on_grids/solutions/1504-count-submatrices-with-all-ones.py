"""
1504. Count Submatrices With All Ones (Medium)
https://leetcode.com/problems/count-submatrices-with-all-ones/

Problem:
    Given an m x n binary matrix, count the number of submatrices that
    are all ones.

Pattern: 10 - DP on Grids

Approach:
    1. For each row, compute histogram heights: h[j] = consecutive 1s
       ending at current row in column j.
    2. For each cell (i, j) as bottom-right corner, extend left while
       tracking the minimum height. Each min height contributes that many
       submatrices ending at this bottom-right corner.
    3. Alternatively, use stack-based approach for O(m*n) total.

Complexity:
    Time:  O(m * n^2) with the simple approach, O(m * n) with stack
    Space: O(n) for heights array
"""

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

            # For each column j, count submatrices with bottom-right at (i, j)
            for j in range(n):
                min_h = heights[j]
                for k in range(j, -1, -1):
                    if heights[k] == 0:
                        break
                    min_h = min(min_h, heights[k])
                    total += min_h

        return total


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
    assert sol.numSubmat(mat) == 13, f"Test 1 failed: {sol.numSubmat(mat)}"

    # Test 2
    mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
    assert sol.numSubmat(mat) == 24, f"Test 2 failed: {sol.numSubmat(mat)}"

    # Test 3: all zeros
    mat = [[0, 0], [0, 0]]
    assert sol.numSubmat(mat) == 0, "Test 3 failed"

    # Test 4: all ones 2x2
    mat = [[1, 1], [1, 1]]
    assert sol.numSubmat(mat) == 9, f"Test 4 failed: {sol.numSubmat(mat)}"

    # Test 5: single element
    mat = [[1]]
    assert sol.numSubmat(mat) == 1, "Test 5 failed"

    print("All tests passed for 1504. Count Submatrices With All Ones!")


if __name__ == "__main__":
    run_tests()
