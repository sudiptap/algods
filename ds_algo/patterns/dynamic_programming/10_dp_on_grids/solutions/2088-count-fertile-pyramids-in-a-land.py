"""
2088. Count Fertile Pyramids in a Land (Hard)
https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

Count fertile pyramids and inverse pyramids in a binary grid. A pyramid
of height h has apex at (r,c) and each row i below has cells from
(r+i, c-i) to (r+i, c+i), all 1s. Inverse pyramid goes upward.

Pattern: DP on Grids
Approach:
- For downward pyramids: dp[r][c] = max pyramid height with apex at (r,c).
  dp[r][c] = 0 if grid[r][c] == 0.
  dp[r][c] = 1 + min(dp[r+1][c-1], dp[r+1][c], dp[r+1][c+1]) if grid[r][c]==1.
  Process bottom to top.
- For upward (inverse) pyramids: similar but apex at bottom.
  dp2[r][c] = 1 + min(dp2[r-1][c-1], dp2[r-1][c], dp2[r-1][c+1]).
  Process top to bottom.
- Count = sum of (dp[r][c] - 1) for all cells (pyramid of height h
  contributes h-1 pyramids).

Time:  O(m * n)
Space: O(m * n)
"""

from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        """Return total count of fertile pyramids and inverse pyramids.

        Args:
            grid: Binary matrix.

        Returns:
            Total count of pyramids.
        """
        m, n = len(grid), len(grid[0])

        def count_direction(g):
            """Count pyramids pointing downward in grid g."""
            rows = len(g)
            cols = len(g[0])
            dp = [row[:] for row in g]
            total = 0

            # Process from second-to-last row upward
            for r in range(rows - 2, -1, -1):
                for c in range(1, cols - 1):
                    if dp[r][c] == 0:
                        continue
                    dp[r][c] = 1 + min(dp[r + 1][c - 1], dp[r + 1][c], dp[r + 1][c + 1])
                    total += dp[r][c] - 1  # pyramids of height 2, 3, ..., dp[r][c]

            return total

        # Downward pyramids
        result = count_direction(grid)

        # Upward (inverse) pyramids: flip the grid vertically
        flipped = grid[::-1]
        result += count_direction(flipped)

        return result


# ---------- tests ----------
def test_count_pyramids():
    sol = Solution()

    # Example 1
    assert sol.countPyramids([[0,1,1,0],[1,1,1,1]]) == 2

    # Example 2
    assert sol.countPyramids([[1,1,1],[1,1,1]]) == 2

    # Example 3
    assert sol.countPyramids([[1,0,1],[0,0,0],[1,0,1]]) == 0

    # Larger grid: 3x5 with a zero
    # Down pyramids of height 2 at various apex positions + up pyramids
    result = sol.countPyramids([[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1]])
    assert result == 12

    # All zeros
    assert sol.countPyramids([[0,0],[0,0]]) == 0

    print("All tests passed for 2088. Count Fertile Pyramids in a Land")


if __name__ == "__main__":
    test_count_pyramids()
