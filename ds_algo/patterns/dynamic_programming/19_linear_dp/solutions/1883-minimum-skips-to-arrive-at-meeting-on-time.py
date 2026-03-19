"""
1883. Minimum Skips to Arrive at Meeting On Time (Hard)
https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

You travel along n roads with distances dist[i] at speed `speed`. After
each road (except the last) you rest and your time rounds up to the next
integer. You can skip some rests (no rounding). Return min skips needed
to arrive in <= hoursBefore, or -1 if impossible.

Pattern: Linear DP
Approach:
- dp[i][j] = minimum travel time after the first i roads with j skips.
- If we don't skip rest after road i:
    dp[i][j] = ceil(dp[i-1][j] + dist[i-1]/speed)
- If we skip rest after road i:
    dp[i][j] = dp[i-1][j-1] + dist[i-1]/speed
- Use EPS to handle floating point issues, or use integer arithmetic
  by multiplying everything by speed.
- Answer: smallest j such that dp[n][j] <= hoursBefore.

Time:  O(n^2)
Space: O(n^2), reducible to O(n)
"""

from typing import List
import math


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        """Return minimum skips to arrive on time, or -1.

        Args:
            dist: Road distances.
            speed: Travel speed.
            hoursBefore: Time limit.

        Returns:
            Minimum number of skips, or -1 if impossible.
        """
        n = len(dist)
        # Use integer DP: multiply time by speed to avoid floats
        # dp[j] = min (time * speed) with j skips after processing roads so far
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            # Process road i (0-indexed), traverse backwards to reuse array
            new_dp = [INF] * (n + 1)
            for j in range(n + 1):
                if dp[j] == INF:
                    continue
                # Don't skip (round up), but not after last road
                t = dp[j] + dist[i]
                if i < n - 1:
                    # Ceil to next multiple of speed
                    rounded = ((t + speed - 1) // speed) * speed
                    new_dp[j] = min(new_dp[j], rounded)
                else:
                    new_dp[j] = min(new_dp[j], t)

                # Skip rest (no rounding)
                if j + 1 <= n:
                    new_dp[j + 1] = min(new_dp[j + 1], t)
            dp = new_dp

        for j in range(n + 1):
            if dp[j] <= hoursBefore * speed:
                return j
        return -1


# ---------- tests ----------
def test_min_skips():
    sol = Solution()

    # Example 1
    assert sol.minSkips([1, 3, 2], 4, 2) == 1

    # Example 2
    assert sol.minSkips([7, 3, 5, 5], 2, 10) == 2

    # Example 3: impossible
    assert sol.minSkips([7, 3, 5, 5], 1, 10) == -1

    # No skips needed
    assert sol.minSkips([1, 1, 1], 1, 3) == 0

    # Single road
    assert sol.minSkips([10], 5, 2) == 0

    print("All tests passed for 1883. Minimum Skips to Arrive at Meeting On Time")


if __name__ == "__main__":
    test_min_skips()
