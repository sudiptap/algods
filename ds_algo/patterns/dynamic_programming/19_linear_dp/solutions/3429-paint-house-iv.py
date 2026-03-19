"""
3429. Paint House IV
https://leetcode.com/problems/paint-house-iv/

Pattern: 19 - Linear DP

---
APPROACH: DP with two painters from opposite ends.
- Constraints: (1) no two adjacent houses same color, (2) equidistant houses (i, n-1-i) differ.
- Process pairs (i, n-1-i) for i = 0..n/2-1.
- State: dp[c_left][c_right] = min cost where left painter's last color is c_left,
  right painter's last color is c_right.
- Transitions ensure: new_c_left != prev_c_left (left adjacency),
  new_c_right != prev_c_right (right adjacency), new_c_left != new_c_right (equidistant).

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        INF = float('inf')
        half = n // 2

        # dp[c1][c2] for left painter color c1, right painter color c2
        dp = [[INF] * 3 for _ in range(3)]

        # First pair: house 0 (left) and house n-1 (right)
        for c1 in range(3):
            for c2 in range(3):
                if c1 != c2:
                    dp[c1][c2] = cost[0][c1] + cost[n - 1][c2]

        for step in range(1, half):
            left_house = step
            right_house = n - 1 - step
            new_dp = [[INF] * 3 for _ in range(3)]

            for nc1 in range(3):
                for nc2 in range(3):
                    if nc1 == nc2:
                        continue
                    add_cost = cost[left_house][nc1] + cost[right_house][nc2]
                    for pc1 in range(3):
                        if pc1 == nc1:
                            continue
                        for pc2 in range(3):
                            if pc2 == nc2:
                                continue
                            val = dp[pc1][pc2] + add_cost
                            if val < new_dp[nc1][nc2]:
                                new_dp[nc1][nc2] = val

            dp = new_dp

        return min(dp[c1][c2] for c1 in range(3) for c2 in range(3))


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minCost(4, [[3, 5, 7], [6, 2, 9], [4, 8, 1], [7, 3, 5]]) == 9
    assert sol.minCost(6, [[2, 4, 6], [5, 3, 8], [7, 1, 9], [4, 6, 2], [3, 5, 7], [8, 2, 4]]) == 18

    print("Solution: all tests passed")
