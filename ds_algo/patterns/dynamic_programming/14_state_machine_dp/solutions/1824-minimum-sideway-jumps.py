"""
1824. Minimum Sideway Jumps
https://leetcode.com/problems/minimum-sideway-jumps/

Pattern: 14 - State Machine DP

---
APPROACH: State Machine DP with 3 lanes
- 3 lanes (1-indexed as 1,2,3), n+1 points (0 to n).
- Frog starts at lane 2, point 0. Goal: reach point n in any lane.
- obstacles[i] = lane blocked at point i (0 means no obstacle).
- dp[lane] = min sideway jumps to reach current point in that lane.
- At each point, first move forward (free if no obstacle), then consider
  sideway jumps: jump to another lane costs 1 if that lane is not blocked.
- Process point by point, updating dp greedily.

Time: O(n)  Space: O(1) — only 3 lane states
---
"""

from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        DP with 3 states (one per lane). At each point:
        1) If a lane is blocked, set its dp to infinity.
        2) For unblocked lanes, check if jumping from another unblocked
           lane (cost +1) is cheaper than current value.
        """
        INF = float('inf')
        # dp[lane] for lanes 1,2,3 (1-indexed); index 0 unused
        dp = [INF, 1, 0, 1]  # start at lane 2, point 0

        for obs in obstacles:
            # Block the obstacle lane
            if obs:
                dp[obs] = INF

            # Try to improve each unblocked lane by jumping from another lane
            for lane in range(1, 4):
                if lane == obs:
                    continue
                for other in range(1, 4):
                    if other == lane or other == obs:
                        continue
                    dp[lane] = min(dp[lane], dp[other] + 1)

        return min(dp[1], dp[2], dp[3])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: obstacles = [0,1,2,3,0]
    # Start lane 2 -> jump to lane 3 at some point -> 2 jumps total
    assert sol.minSideJumps([0, 1, 2, 3, 0]) == 2

    # Example 2: obstacles = [0,1,1,3,3,0]
    assert sol.minSideJumps([0, 1, 1, 3, 3, 0]) == 0

    # Example 3: obstacles = [0,2,1,0,3,0]
    assert sol.minSideJumps([0, 2, 1, 0, 3, 0]) == 2

    # No obstacles
    assert sol.minSideJumps([0, 0, 0, 0]) == 0

    # Obstacle in starting lane immediately
    assert sol.minSideJumps([0, 2, 0]) == 1

    print("Solution: all tests passed")
