"""
1575. Count All Possible Routes
https://leetcode.com/problems/count-all-possible-routes/

Pattern: 19 - Linear DP

---
APPROACH: Memoized DFS with (city, fuel) state
- dp[city][fuel] = number of ways to reach finish from city with fuel remaining
- From each city, try moving to every other city if fuel allows
- Base contribution: if city == finish, count 1 (can stop here but also continue)

Time: O(n^2 * fuel) where n = number of cities
Space: O(n * fuel)
---
"""

from typing import List
from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @lru_cache(maxsize=None)
        def dp(city, fuel_left):
            if fuel_left < 0:
                return 0
            res = 1 if city == finish else 0
            for next_city in range(n):
                if next_city != city:
                    cost = abs(locations[city] - locations[next_city])
                    if cost <= fuel_left:
                        res = (res + dp(next_city, fuel_left - cost)) % MOD
            return res

        return dp(start, fuel)


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.countRoutes([2, 3, 6, 8, 4], 1, 3, 5) == 4

    # Example 2
    assert sol.countRoutes([4, 3, 1], 1, 0, 6) == 5

    # Example 3
    assert sol.countRoutes([5, 2, 1], 0, 2, 3) == 0

    # Same start and finish
    assert sol.countRoutes([1, 2, 3], 0, 0, 0) == 1

    # No fuel
    assert sol.countRoutes([1, 2], 0, 1, 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
