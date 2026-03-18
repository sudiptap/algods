"""
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/

Pattern: 10 - DP on Grids

---
APPROACH: 1D DP (row by row)
- dp[j] = minimum falling path sum ending at column j in the current row.
- For each row i >= 1:
    dp[j] = matrix[i][j] + min(dp[j-1], dp[j], dp[j+1])  (clamped to bounds)
- Process left-to-right using a prev array to avoid overwrite issues.

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """Return the minimum sum of a falling path through matrix."""
        n = len(matrix)
        dp = matrix[0][:]

        for i in range(1, n):
            prev = dp[:]
            for j in range(n):
                best = prev[j]
                if j > 0:
                    best = min(best, prev[j - 1])
                if j < n - 1:
                    best = min(best, prev[j + 1])
                dp[j] = matrix[i][j] + best

        return min(dp)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert sol.minFallingPathSum([[-19, 57], [-40, -5]]) == -59
    assert sol.minFallingPathSum([[5]]) == 5
    assert sol.minFallingPathSum([[-48]]) == -48
    assert sol.minFallingPathSum([[1, 2], [3, 4]]) == 4

    print("all tests passed")
