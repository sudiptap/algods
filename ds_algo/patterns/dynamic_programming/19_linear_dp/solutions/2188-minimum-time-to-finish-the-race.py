"""
2188. Minimum Time to Finish the Race (Hard)
https://leetcode.com/problems/minimum-time-to-finish-the-race/

Given tires with [f, r] (f=first lap time, r=degradation factor) and
changeTime cost, find minimum time to complete numLaps laps.

Pattern: Linear DP
Approach:
- Precompute best[j] = minimum time to run j consecutive laps on one tire
  (without changing). Cap at changeTime + f_min (otherwise better to change).
- dp[i] = minimum time to complete i laps.
- dp[i] = min over j in [1, min(i, max_consecutive)] of
  dp[i-j] + changeTime + best[j].
- dp[0] = -changeTime (offset to cancel first "change" which doesn't exist).

Time:  O(numLaps * maxConsecutive)
Space: O(numLaps)
"""

from typing import List


class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        """Return minimum time to complete numLaps laps.

        Args:
            tires: List of [f, r] tire specifications.
            changeTime: Time to change tires.
            numLaps: Total laps to complete.

        Returns:
            Minimum total time.
        """
        # Precompute best[j] = min time for j consecutive laps on one tire
        # Maximum useful consecutive laps: when f*r^(j-1) > changeTime + f_min
        # For r >= 2, this is at most ~18 laps
        max_consec = min(numLaps, 20)
        best = [float('inf')] * (max_consec + 1)

        for f, r in tires:
            total = 0
            lap_time = f
            for j in range(1, max_consec + 1):
                total += lap_time
                best[j] = min(best[j], total)
                lap_time *= r
                if lap_time > 2 * 10**9:  # overflow protection
                    break

        # dp[i] = min time for i laps
        dp = [float('inf')] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(1, min(i, max_consec) + 1):
                # Cost: changeTime (for changing to new tire) + best[j]
                # First segment doesn't need changeTime, handle via:
                # dp[i] = min(dp[i-j] + changeTime + best[j])
                dp[i] = min(dp[i], dp[i - j] + changeTime + best[j])

        # Subtract one changeTime (the first segment doesn't need a change)
        return dp[numLaps] - changeTime


# ---------- tests ----------
def test_minimum_finish_time():
    sol = Solution()

    # Example 1
    assert sol.minimumFinishTime([[2,3],[3,4]], 5, 4) == 21

    # Example 2
    assert sol.minimumFinishTime([[1,10],[2,2],[3,4]], 6, 5) == 25

    # Single lap
    assert sol.minimumFinishTime([[1,2]], 5, 1) == 1

    # All same tire: change after each lap: 2+1+2+1+2=8
    assert sol.minimumFinishTime([[2,2]], 1, 3) == 8

    print("All tests passed for 2188. Minimum Time to Finish the Race")


if __name__ == "__main__":
    test_minimum_finish_time()
