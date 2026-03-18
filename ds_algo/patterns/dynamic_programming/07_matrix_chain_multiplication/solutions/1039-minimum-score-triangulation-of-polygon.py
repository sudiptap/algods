"""
1039. Minimum Score Triangulation of Polygon
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Pattern: 07 - Matrix Chain Multiplication

---
APPROACH: Interval DP (MCM style)
- dp[i][j] = minimum cost to triangulate the sub-polygon formed by
  vertices i, i+1, ..., j.
- For each diagonal (i, j), try every vertex k between i and j as the
  third vertex of a triangle with edge (i, j):
    dp[i][j] = min(dp[i][k] + dp[k][j] + values[i]*values[k]*values[j])
    for all k in (i+1, ..., j-1)
- Base case: dp[i][i+1] = 0 (an edge, no triangle).
- Answer: dp[0][n-1].

Time:  O(n^3)
Space: O(n^2)
---
"""

from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """Return minimum score to triangulate the polygon."""
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # length of sub-polygon (number of vertices)
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    cost = (
                        dp[i][k]
                        + dp[k][j]
                        + values[i] * values[k] * values[j]
                    )
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minScoreTriangulation([1, 2, 3]) == 6
    assert sol.minScoreTriangulation([3, 7, 4, 5]) == 144
    assert sol.minScoreTriangulation([1, 3, 1, 4, 1, 5]) == 13

    print("Solution: all tests passed")
