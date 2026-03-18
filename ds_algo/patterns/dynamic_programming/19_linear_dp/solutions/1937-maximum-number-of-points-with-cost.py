"""
1937. Maximum Number of Points with Cost
https://leetcode.com/problems/maximum-number-of-points-with-cost/

Pattern: 19 - Linear DP (Row-by-row with left/right max optimization)

---
APPROACH:
- dp[j] = max points obtainable ending at column j of the current row.
- Naive transition: dp_new[j] = points[row][j] + max(dp[k] - |j - k|)
  over all k. This is O(m) per cell -> O(n*m^2) total.
- Optimization: split |j - k| into two cases.
  Left pass:  left[j]  = max(dp[k] + k) for k <= j  => value = left[j] - j
  Right pass: right[j] = max(dp[k] - k) for k >= j  => value = right[j] + j
  dp_new[j] = points[row][j] + max(left[j] - j, right[j] + j)

Time:  O(n * m)   — n rows, m columns
Space: O(m)
---
"""

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """Return the maximum points we can achieve picking one cell per row."""
        m = len(points[0])
        dp = points[0][:]

        for row in points[1:]:
            # Left pass: left[j] = max(dp[k] + k) for k in [0..j]
            left = [0] * m
            left[0] = dp[0]  # dp[0] + 0
            for j in range(1, m):
                left[j] = max(left[j - 1], dp[j] + j)

            # Right pass: right[j] = max(dp[k] - k) for k in [j..m-1]
            right = [0] * m
            right[m - 1] = dp[m - 1] - (m - 1)
            for j in range(m - 2, -1, -1):
                right[j] = max(right[j + 1], dp[j] - j)

            # Combine
            for j in range(m):
                dp[j] = row[j] + max(left[j] - j, right[j] + j)

        return max(dp)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxPoints([[1,2,3],[1,5,1],[3,1,1]]) == 9
    assert sol.maxPoints([[1,5],[2,3],[4,2]]) == 11
    # Single row
    assert sol.maxPoints([[5,3,1,4]]) == 5
    # Single column
    assert sol.maxPoints([[1],[2],[3]]) == 6
    # 2x2 choosing diagonals
    assert sol.maxPoints([[0,10],[10,0]]) == 19  # 10 + 10 - 1

    print("all tests passed")
