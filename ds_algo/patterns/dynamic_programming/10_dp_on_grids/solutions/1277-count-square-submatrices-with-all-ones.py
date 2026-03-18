"""
1277. Count Square Submatrices with All Ones (Medium)
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Pattern: 10 - DP on Grids

---
APPROACH: DP (same idea as 221 Maximal Square)
- dp[i][j] = side length of the largest square with all ones whose
  bottom-right corner is (i, j).
- If matrix[i][j] == 1:
      dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
- A cell with dp value k contributes k squares (sizes 1x1, 2x2, ..., kxk).
  So the answer is the sum of all dp values.

Time:  O(m * n)
Space: O(m * n), reducible to O(n) with rolling array
---
"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """Return the total number of square submatrices with all ones."""
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    total += dp[i][j]

        return total


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]) == 15

    # Example 2
    assert sol.countSquares([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0],
    ]) == 7

    # Single cell
    assert sol.countSquares([[1]]) == 1
    assert sol.countSquares([[0]]) == 0

    # All ones 2x2
    assert sol.countSquares([[1, 1], [1, 1]]) == 5  # 4 singles + 1 big

    # Row of ones
    assert sol.countSquares([[1, 1, 1]]) == 3

    print("all tests passed")
