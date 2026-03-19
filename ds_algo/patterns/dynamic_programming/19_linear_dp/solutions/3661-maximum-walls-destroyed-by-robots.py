"""
3661. Maximum Walls Destroyed by Robots
https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

Pattern: 19 - Linear DP

---
APPROACH: DP per robot / greedy assignment
- Multiple robots, each can destroy walls in sequence.
- Each robot has a cost/capacity constraint.
- DP to assign walls to robots optimally.
- dp[i][j] = max walls destroyed using first i walls with j robots.

Time: O(n * k)  Space: O(n * k)
---
"""

from typing import List


class Solution:
    def maxWallsDestroyed(self, walls: List[int], robots: int) -> int:
        n = len(walls)
        if robots >= n:
            return n

        # Each robot can destroy a contiguous segment of walls.
        # We need to select 'robots' contiguous segments to maximize coverage.
        # This is equivalent to: remove (robots-1) "breaks" from the array,
        # keeping robots segments. But we want to maximize number of walls
        # destroyed, which is total if all are covered.

        # If robots destroy contiguous segments with gaps between them:
        # dp[i][j] = max walls destroyed considering walls[0..i-1] using j robots
        # Each robot takes a contiguous segment, segments don't overlap.

        # dp[i][j] = max(dp[i-1][j],  # wall i not destroyed
        #               max over l <= i of (dp[l-1][j-1] + (i - l + 1)))  # robot j takes walls[l..i]

        # Simplify: dp[i][j] = max(dp[i-1][j], i - l + 1 + dp[l-1][j-1]) for best l
        # The "i - l + 1 + dp[l-1][j-1]" = i + 1 + dp[l-1][j-1] - l
        # Maximize over l: dp[l-1][j-1] - l + i + 1
        # Track max_val = max(dp[l-1][j-1] - l) as we go.

        dp = [[0] * (robots + 1) for _ in range(n + 1)]

        for j in range(1, robots + 1):
            best = float('-inf')  # max(dp[l-1][j-1] - l) for l from 1..i
            for i in range(1, n + 1):
                best = max(best, dp[i - 1][j - 1] - i)
                dp[i][j] = max(dp[i - 1][j], best + i + 1)

        return dp[n][robots]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # 5 walls, 2 robots: take all (2 segments cover everything)
    res = sol.maxWallsDestroyed([1, 1, 1, 1, 1], 2)
    assert res == 5, f"Got {res}"

    # 5 walls, 1 robot: take all 5 (one contiguous segment)
    res = sol.maxWallsDestroyed([1, 1, 1, 1, 1], 1)
    assert res == 5, f"Got {res}"

    print("All tests passed!")
