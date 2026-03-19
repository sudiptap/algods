"""
2742. Painting the Walls
https://leetcode.com/problems/painting-the-walls/

Pattern: 19 - Linear DP (Knapsack: paid painter + free painter trick)

---
APPROACH: If paid painter paints wall i (taking time[i] units), the free
painter can paint time[i] other walls during that time. So painting wall i
with paid painter effectively covers (1 + time[i]) walls. DP: dp[j] = min
cost to cover j walls using paid painters.

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            # Process in reverse to avoid using same wall twice
            new_dp = dp[:]
            for j in range(n + 1):
                if dp[j] < float('inf'):
                    covered = min(n, j + 1 + time[i])
                    new_dp[covered] = min(new_dp[covered], dp[j] + cost[i])
            dp = new_dp

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.paintWalls([1, 2, 3, 2], [1, 2, 3, 2]) == 3
    assert sol.paintWalls([2, 3, 4, 2], [1, 1, 1, 1]) == 4

    print("All tests passed!")
