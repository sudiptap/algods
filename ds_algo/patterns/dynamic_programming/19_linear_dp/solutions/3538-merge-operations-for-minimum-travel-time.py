"""
3538. Merge Operations for Minimum Travel Time
https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

Pattern: 19 - Linear DP (dp[i][j])

---
APPROACH: DP with memoization.
- position[i] are sign positions, time[i] = time per km between position[i] and position[i+1].
- Merge: combine two adjacent signs, summing their times.
- dp(i, skips, last): min time from position i to end, with skips remaining,
  where last is the first sign of the current merged group.
- The "rate" (time per km) for current group = sum of time[last..i].
- At each sign, either skip it (merge into current group) or stop (start new group).

Time: O(k * n^2)  Space: O(k * n^2)
---
"""

from typing import List
from functools import lru_cache
import itertools
import math


class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        prefix = list(itertools.accumulate(time, initial=0))

        @lru_cache(maxsize=None)
        def dp(i, skips, last):
            """Min travel time from sign i to end, skips remaining, current group started at last."""
            if i == n - 1:
                return 0 if skips == 0 else math.inf

            rate = prefix[i + 1] - prefix[last]  # sum of time[last..i]
            res = math.inf
            # Try jumping to sign j (skipping j - i - 1 signs between i and j)
            end = min(n - 1, i + skips + 1)
            for j in range(i + 1, end + 1):
                distance = position[j] - position[i]
                cost = distance * rate + dp(j, skips - (j - i - 1), i + 1)
                res = min(res, cost)

            return res

        return dp(0, k, 0)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minTravelTime(10, 4, 1, [0, 3, 8, 10], [5, 8, 3, 1]) == 62
    assert sol.minTravelTime(4, 3, 0, [0, 2, 4], [3, 2]) == 10

    print("Solution: all tests passed")
