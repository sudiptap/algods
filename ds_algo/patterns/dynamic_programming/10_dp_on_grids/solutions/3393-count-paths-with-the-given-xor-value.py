"""
3393. Count Paths With the Given XOR Value (Medium)

Pattern: 10_dp_on_grids
- Count paths from (0,0) to (m-1,n-1) moving right or down where XOR of all
  cells along path equals k.

Approach:
- dp[i][j][x] = number of paths to (i,j) with XOR value x.
- Transition: dp[i][j][x ^ grid[i][j]] += dp[i-1][j][x] + dp[i][j-1][x].
- Since values up to 15 (4 bits), XOR values are 0..15.

Complexity:
- Time:  O(m * n * 16)
- Space: O(n * 16) with rolling array
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MAX_XOR = 16

        # dp[j][x] = count of paths to current row, column j with XOR x
        dp = [[0] * MAX_XOR for _ in range(n)]
        # Initialize first cell
        dp[0][grid[0][0]] = 1

        # First row
        for j in range(1, n):
            for x in range(MAX_XOR):
                if dp[j - 1][x]:
                    dp[j][x ^ grid[0][j]] = (dp[j][x ^ grid[0][j]] + dp[j - 1][x]) % MOD

        for i in range(1, m):
            new_dp = [[0] * MAX_XOR for _ in range(n)]
            for j in range(n):
                for x in range(MAX_XOR):
                    total = 0
                    if i > 0:
                        total += dp[j][x]
                    if j > 0:
                        total += new_dp[j - 1][x]
                    if total:
                        new_dp[j][x ^ grid[i][j]] = (new_dp[j][x ^ grid[i][j]] + total) % MOD
            dp = new_dp

        return dp[n - 1][k]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.countPathsWithXorValue([[2, 1, 5], [7, 10, 0], [12, 6, 4]], 11) == 3

    # Example 2
    assert sol.countPathsWithXorValue([[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], 2) == 5

    # Single cell
    assert sol.countPathsWithXorValue([[5]], 5) == 1
    assert sol.countPathsWithXorValue([[5]], 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
