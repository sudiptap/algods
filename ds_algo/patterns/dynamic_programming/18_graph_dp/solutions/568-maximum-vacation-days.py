"""
568. Maximum Vacation Days (Hard)
https://leetcode.com/problems/maximum-vacation-days/

Pattern: Graph DP

Given N cities and K weeks, you start in city 0. Each week you can
stay or fly to a connected city, then vacation for that week.
flights[i][j] == 1 means there's a flight from city i to city j.
days[i][j] = vacation days in city i during week j.
Maximize total vacation days.

Approach:
    dp[week][city] = max vacation days achievable from week onward
    starting in city.

    Process weeks backward. For each (week, city), try staying or
    flying to any reachable city next week.

    Forward DP alternative: dp[w][c] = max vacation days up to week w
    ending in city c.

Time:  O(K * N^2)
Space: O(N) with rolling array
"""

from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        """Return max vacation days over K weeks starting from city 0."""
        n = len(flights)
        k = len(days[0])

        # dp[c] = max vacation days up to current week, ending in city c
        # -1 means unreachable
        dp = [-1] * n
        dp[0] = 0

        for w in range(k):
            new_dp = [-1] * n
            for c in range(n):
                # Can we be in city c this week?
                # We could have been in any city prev_c last week and flown here
                for prev_c in range(n):
                    if dp[prev_c] < 0:
                        continue
                    if prev_c == c or flights[prev_c][c] == 1:
                        val = dp[prev_c] + days[c][w]
                        if val > new_dp[c]:
                            new_dp[c] = val
            dp = new_dp

        return max(dp)


# ───────────────────────── tests ─────────────────────────

def test_example1():
    flights = [[0,1,1],[1,0,1],[1,1,0]]
    days = [[1,3,1],[6,0,3],[3,3,3]]
    assert Solution().maxVacationDays(flights, days) == 12

def test_example2():
    flights = [[0,0,0],[0,0,0],[0,0,0]]
    days = [[1,1,1],[7,7,7],[7,7,7]]
    assert Solution().maxVacationDays(flights, days) == 3

def test_example3():
    flights = [[0,1,1],[1,0,1],[1,1,0]]
    days = [[7,0,0],[0,7,0],[0,0,7]]
    assert Solution().maxVacationDays(flights, days) == 21

def test_single_city():
    flights = [[0]]
    days = [[5, 3, 2]]
    assert Solution().maxVacationDays(flights, days) == 10

def test_two_cities_no_flight():
    flights = [[0, 0], [0, 0]]
    days = [[1, 1], [5, 5]]
    assert Solution().maxVacationDays(flights, days) == 2

def test_two_cities_with_flight():
    flights = [[0, 1], [1, 0]]
    days = [[1, 1], [5, 5]]
    assert Solution().maxVacationDays(flights, days) == 10


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
