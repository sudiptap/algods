"""
221. Maximal Square (Medium)

Pattern: DP on Grids
Approach:
    dp[i][j] = side length of the largest square whose bottom-right corner is (i, j).
    If matrix[i][j] == '1':
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    The answer is max(dp[i][j])^2.

    Intuition: a square of side k ending at (i,j) requires squares of side >= k-1
    ending at the three neighboring cells (top, left, top-left diagonal).

Complexity:
    Time:  O(m * n)
    Space: O(m * n), reducible to O(n) with rolling array
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert sol.maximalSquare(matrix1) == 4, f"Expected 4, got {sol.maximalSquare(matrix1)}"

    # Example 2: single 0
    assert sol.maximalSquare([["0"]]) == 0

    # Example 3: single 1
    assert sol.maximalSquare([["1"]]) == 1

    # All ones 3x3 -> square of side 3 -> area 9
    matrix2 = [["1"] * 3 for _ in range(3)]
    assert sol.maximalSquare(matrix2) == 9

    # Empty matrix
    assert sol.maximalSquare([]) == 0

    # Row of ones
    assert sol.maximalSquare([["1", "1", "1", "1"]]) == 1

    # Column of ones
    assert sol.maximalSquare([["1"], ["1"], ["1"]]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
