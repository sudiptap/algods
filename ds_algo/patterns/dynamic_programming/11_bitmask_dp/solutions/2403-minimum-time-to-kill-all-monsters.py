"""
2403. Minimum Time to Kill All Monsters
https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

Pattern: 11 - Bitmask DP

---
APPROACH: dp[mask] = min time to kill monsters in mask
- Power increases as you kill more monsters. After killing j monsters, your
  power = j+1 (or gain+1 per kill).
- Time to kill monster i with power p = ceil(power[i] / p).
- dp[mask] = min over all i in mask of dp[mask ^ (1<<i)] + ceil(power[i] / popcount(mask))
- Process masks in order of increasing popcount.

Time: O(2^n * n)  Space: O(2^n)
---
"""

from typing import List
import math


class Solution:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1, 1 << n):
            kills = bin(mask).count('1')
            # Current power (gain) = kills (we've killed `kills` monsters)
            p = kills
            for i in range(n):
                if mask & (1 << i):
                    prev = mask ^ (1 << i)
                    cost = math.ceil(power[i] / p)
                    dp[mask] = min(dp[mask], dp[prev] + cost)

        return dp[(1 << n) - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumTime([3, 1, 4]) == 4
    assert sol.minimumTime([1, 1, 4]) == 4
    assert sol.minimumTime([1, 2, 4, 9]) == 6
    assert sol.minimumTime([5]) == 5

    print("all tests passed")
