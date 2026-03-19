"""
2463. Minimum Total Distance Traveled
https://leetcode.com/problems/minimum-total-distance-traveled/

Pattern: 07 - Matrix Chain Multiplication

---
APPROACH: Sort robots and factories, DP assignment
- Sort robots and expand factories (each factory slot is separate).
- dp[i][j] = min distance assigning first i robots to first j factory slots.
- Transition: dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + |robot[i-1] - slot[j-1]|)
  Either skip factory slot j, or assign robot i to slot j.

Time: O(n * m) where n = robots, m = total factory slots  Space: O(n * m)
---
"""

from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        # Expand factories into individual slots
        slots = []
        for pos, cap in factory:
            slots.extend([pos] * cap)

        n, m = len(robot), len(slots)

        # dp[i][j] = min cost assigning first i robots to first j slots
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0] = [0] * (m + 1)

        for i in range(1, n + 1):
            for j in range(i, m + 1):  # need at least i slots
                # Skip slot j
                dp[i][j] = dp[i][j - 1]
                # Assign robot i to slot j
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(robot[i - 1] - slots[j - 1]))

        return dp[n][m]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]]) == 4
    assert sol.minimumTotalDistance([1, -1], [[-2, 1], [2, 1]]) == 2
    assert sol.minimumTotalDistance([9, 11, 99, 101], [[10, 2], [100, 2]]) == 4

    print("all tests passed")
