"""
1594. Maximum Non Negative Product in a Matrix
https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

Pattern: 10 - DP on Grids

---
APPROACH: Track max and min product at each cell
- Negative * negative = positive, so we need to track both max and min products.
- max_dp[i][j] = maximum product of any path from (0,0) to (i,j)
- min_dp[i][j] = minimum product of any path from (0,0) to (i,j)
- When grid[i][j] < 0, max comes from min * negative, min from max * negative.
- Answer: max_dp[m-1][n-1] if >= 0, else -1.

Time: O(m * n)
Space: O(m * n), can be optimized to O(n)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        # First row
        for j in range(1, n):
            max_dp[0][j] = max_dp[0][j - 1] * grid[0][j]
            min_dp[0][j] = min_dp[0][j - 1] * grid[0][j]

        # First col
        for i in range(1, m):
            max_dp[i][0] = max_dp[i - 1][0] * grid[i][0]
            min_dp[i][0] = min_dp[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                candidates = [
                    max_dp[i - 1][j] * v, min_dp[i - 1][j] * v,
                    max_dp[i][j - 1] * v, min_dp[i][j - 1] * v
                ]
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        result = max_dp[m - 1][n - 1]
        return result % MOD if result >= 0 else -1


# --- Tests ---
def test():
    sol = Solution()

    # Example 1: all paths yield negative product
    assert sol.maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1

    # Example 2
    assert sol.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8

    # Example 3
    assert sol.maxProductPath([[1, 3], [0, -4]]) == 0

    # All positive
    assert sol.maxProductPath([[1, 2], [3, 4]]) == 12  # 1*3*4=12 or 1*2*4=8

    # Single cell
    assert sol.maxProductPath([[5]]) == 5
    assert sol.maxProductPath([[-5]]) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test()
