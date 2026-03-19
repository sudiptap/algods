"""
1997. First Day Where You Have Been in All the Rooms (Medium)
https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

You visit rooms starting at room 0. On odd-numbered visits to room i,
go to room i+1. On even-numbered visits, go to room nextVisit[i].
nextVisit[i] <= i. Find the first day you've visited all rooms.

Pattern: Linear DP
Approach:
- dp[i] = first day you visit room i for the first time.
- To move from room i to room i+1, you need to visit room i twice.
- After first visit to room i (day dp[i]), you go to nextVisit[i].
- You need to revisit all rooms from nextVisit[i] to i again.
- dp[i+1] = dp[i] + 1 + (dp[i] - dp[nextVisit[i]]) + 1
  = 2*dp[i] - dp[nextVisit[i]] + 2

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        """Return first day all rooms have been visited.

        Args:
            nextVisit: Array where nextVisit[i] <= i.

        Returns:
            First day (0-indexed) all rooms visited, mod 10^9+7.
        """
        MOD = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD

        return dp[n - 1]


# ---------- tests ----------
def test_first_day_all_rooms():
    sol = Solution()

    # Example 1: [0,0] -> day 0:room0, day1:room0, day2:room1 -> 2
    assert sol.firstDayBeenInAllRooms([0, 0]) == 2

    # Example 2: [0,0,2] -> day 6
    assert sol.firstDayBeenInAllRooms([0, 0, 2]) == 6

    # Example 3: [0,1,2,0] -> 6
    assert sol.firstDayBeenInAllRooms([0, 1, 2, 0]) == 6

    # Single room
    assert sol.firstDayBeenInAllRooms([0]) == 0

    print("All tests passed for 1997. First Day Where You Have Been in All the Rooms")


if __name__ == "__main__":
    test_first_day_all_rooms()
