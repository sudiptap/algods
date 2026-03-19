"""
2152. Minimum Number of Lines to Cover Points (Medium)
https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

Given 2D points, find minimum number of straight lines to cover all points.

Pattern: Linear DP / Bitmask DP
Approach:
- n is small (<=10). Use bitmask DP on covered points.
- Precompute for each pair of points (or single point), the mask of
  all points on that line.
- dp[mask] = minimum lines to cover all points in mask.
- For each mask, find the lowest unset bit, try all lines through that
  point, update dp[mask | line_mask].

Time:  O(2^n * n^2)
Space: O(2^n)
"""

from typing import List


class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        """Return minimum number of lines to cover all points.

        Args:
            points: List of [x, y] points.

        Returns:
            Minimum number of lines.
        """
        n = len(points)
        if n <= 2:
            return 1

        # Precompute line masks: for each pair (i,j), find all collinear points
        line_masks = set()
        for i in range(n):
            # Single point as a "line"
            line_masks.add(1 << i)
            for j in range(i + 1, n):
                mask = (1 << i) | (1 << j)
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                for k in range(n):
                    if k == i or k == j:
                        continue
                    # Check if point k is on line (i, j)
                    dx2 = points[k][0] - points[i][0]
                    dy2 = points[k][1] - points[i][1]
                    if dx * dy2 == dy * dx2:
                        mask |= (1 << k)
                line_masks.add(mask)

        line_masks = list(line_masks)
        full = (1 << n) - 1
        INF = n + 1
        dp = [INF] * (full + 1)
        dp[0] = 0

        for mask in range(full + 1):
            if dp[mask] >= INF:
                continue
            # Find lowest unset bit
            first_unset = -1
            for b in range(n):
                if not (mask & (1 << b)):
                    first_unset = b
                    break
            if first_unset == -1:
                continue

            for lm in line_masks:
                if lm & (1 << first_unset):
                    new_mask = mask | lm
                    dp[new_mask] = min(dp[new_mask], dp[mask] + 1)

        return dp[full]


# ---------- tests ----------
def test_minimum_lines():
    sol = Solution()

    # Example 1: 3 collinear points -> 1 line
    assert sol.minimumLines([[0,1],[2,3],[4,5],[4,3]]) == 2

    # Example 2
    assert sol.minimumLines([[0,2],[-2,-2],[1,4]]) == 1

    # Two points
    assert sol.minimumLines([[0,0],[1,1]]) == 1

    # Single point
    assert sol.minimumLines([[0,0]]) == 1

    print("All tests passed for 2152. Minimum Number of Lines to Cover Points")


if __name__ == "__main__":
    test_minimum_lines()
