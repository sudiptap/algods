"""
120. Triangle
https://leetcode.com/problems/triangle/

Pattern: 10 - DP on Grids

---
APPROACH: Bottom-up 1D DP
- Start from the bottom row, work upward
- dp[j] = min path sum starting from position j in current row
- dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
- Bottom-up is cleaner than top-down here: no edge handling needed

Time: O(n^2)  Space: O(n) — reuse the bottom row
---
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]  # copy bottom row

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert sol.minimumTotal([[-10]]) == -10
    assert sol.minimumTotal([[1], [2, 3]]) == 3
    assert sol.minimumTotal([[-1], [2, 3], [1, -1, -3]]) == -1

    print("all tests passed")
