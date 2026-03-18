"""
764. Largest Plus Sign
https://leetcode.com/problems/largest-plus-sign/

Pattern: 19 - Linear DP (precompute arm lengths)

---
APPROACH: Precompute consecutive-1 arm lengths in all 4 directions.
- For each cell (r, c) that is 1, compute how far the arm extends
  left, right, up, and down (including the cell itself).
- The order of the largest plus sign centered at (r, c) is the
  minimum of these four arm lengths.
- Answer is the max order across all cells.

Time: O(n^2)  Space: O(n^2)
---
"""

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """Return the order of the largest plus sign in an n x n grid with mines."""
        banned = set(map(tuple, mines))

        # dp[r][c] will hold the order of the largest plus sign centered at (r,c)
        # Initialize to n (max possible arm length), then shrink via 4 passes
        dp = [[0] * n for _ in range(n)]

        for r in range(n):
            # Left to right pass
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            # Right to left pass
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

        for c in range(n):
            # Top to bottom pass
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

            # Bottom to top pass
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

        return max(dp[r][c] for r in range(n) for c in range(n))


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.orderOfLargestPlusSign(5, [[4, 2]]) == 2
    assert sol.orderOfLargestPlusSign(1, [[0, 0]]) == 0
    assert sol.orderOfLargestPlusSign(1, []) == 1
    assert sol.orderOfLargestPlusSign(2, []) == 1
    assert sol.orderOfLargestPlusSign(3, []) == 2  # center of 3x3
    assert sol.orderOfLargestPlusSign(5, []) == 3  # center of 5x5

    print("all tests passed")
