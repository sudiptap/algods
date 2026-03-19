"""
1595. Minimum Cost to Connect Two Groups of Points
https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP on group2 membership
- Process group1 points one by one. For each, decide which group2 points to connect.
- dp[i][mask] = min cost after processing first i group1 points, where mask
  represents which group2 points have been connected.
- After all group1 points processed, remaining unconnected group2 points must
  be connected to their cheapest group1 point.
- Optimization: precompute min cost for each group2 point.

Time: O(m * 2^n * n) where m = |group1|, n = |group2|
Space: O(m * 2^n)
---
"""

from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m = len(cost)
        n = len(cost[0])
        full_mask = (1 << n) - 1

        # Precompute min cost for each group2 point (for leftover assignment)
        min_cost_g2 = [min(cost[i][j] for i in range(m)) for j in range(n)]

        INF = float('inf')
        # dp[mask] = min cost with mask of group2 connected, after processing current group1 row
        dp = [INF] * (full_mask + 1)
        dp[0] = 0

        for i in range(m):
            new_dp = [INF] * (full_mask + 1)
            for mask in range(full_mask + 1):
                if dp[mask] == INF:
                    continue
                # Connect group1[i] to at least one group2[j]
                for j in range(n):
                    new_mask = mask | (1 << j)
                    new_dp[new_mask] = min(new_dp[new_mask], dp[mask] + cost[i][j])
            # Also allow connecting to multiple group2 points in same row
            # We need to iterate until stable - or handle via subset enumeration
            # Actually, after connecting i to j, we can still connect i to more j's
            # Do another pass allowing adding more connections
            changed = True
            while changed:
                changed = False
                for mask in range(full_mask + 1):
                    if new_dp[mask] == INF:
                        continue
                    for j in range(n):
                        new_mask = mask | (1 << j)
                        val = new_dp[mask] + cost[i][j]
                        if val < new_dp[new_mask]:
                            new_dp[new_mask] = val
                            changed = True
            dp = new_dp

        # After all group1 points, connect remaining group2 points to cheapest
        result = INF
        for mask in range(full_mask + 1):
            if dp[mask] == INF:
                continue
            extra = sum(min_cost_g2[j] for j in range(n) if not (mask & (1 << j)))
            result = min(result, dp[mask] + extra)

        return result


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.connectTwoGroups([[15, 96], [36, 2]]) == 17

    # Example 2
    assert sol.connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4

    # Example 3
    assert sol.connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10

    # Single elements
    assert sol.connectTwoGroups([[5]]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test()
