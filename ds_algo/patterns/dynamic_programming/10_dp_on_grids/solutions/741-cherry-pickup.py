"""
741. Cherry Pickup
https://leetcode.com/problems/cherry-pickup/

Pattern: 10 - DP on Grids (3D DP, two simultaneous walkers)

---
APPROACH: Model two people walking from (0,0) to (n-1,n-1) simultaneously.
- Instead of one person going there and back, simulate two people going
  from (0,0) to (n-1,n-1) at the same time (equivalent and avoids greediness).
- Both take the same number of steps t = r1+c1 = r2+c2, so c2 = t - r2.
- dp[r1][c1][r2] = max cherries collected when person1 is at (r1,c1)
  and person2 is at (r2, t-r2).
- At each step, both move either right or down → 4 transitions.
- If both are on the same cell, count the cherry only once.
- Thorns (grid[r][c] == -1) block passage entirely.

Time: O(n^3)  Space: O(n^3)
---
"""

from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Return max cherries collected on a round trip (0,0) -> (n-1,n-1) -> (0,0)."""
        n = len(grid)
        NEG_INF = float("-inf")

        # dp[r1][c1][r2]: max cherries when person1 at (r1,c1), person2 at (r2, r1+c1-r2)
        dp = [[[NEG_INF] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        # Total steps from 0 to 2*(n-1). At step t, r+c = t for both walkers.
        for t in range(1, 2 * n - 1):
            ndp = [[[NEG_INF] * n for _ in range(n)] for _ in range(n)]
            for r1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                c1 = t - r1
                if c1 < 0 or c1 >= n or grid[r1][c1] == -1:
                    continue
                for r2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    c2 = t - r2
                    if c2 < 0 or c2 >= n or grid[r2][c2] == -1:
                        continue

                    # Cherries collected at this step
                    cherries = grid[r1][c1]
                    if r1 != r2:  # different cells, add second person's cherry
                        cherries += grid[r2][c2]

                    # Previous states: each person came from up or left
                    best_prev = NEG_INF
                    for pr1, pc1 in ((r1 - 1, c1), (r1, c1 - 1)):
                        if pr1 < 0 or pc1 < 0:
                            continue
                        for pr2, pc2 in ((r2 - 1, c2), (r2, c2 - 1)):
                            if pr2 < 0 or pc2 < 0:
                                continue
                            val = dp[pr1][pc1][pr2]
                            if val > best_prev:
                                best_prev = val

                    if best_prev != NEG_INF:
                        ndp[r1][c1][r2] = best_prev + cherries

            dp = ndp

        return max(0, dp[n - 1][n - 1][n - 1])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: two paths collecting all cherries
    assert sol.cherryPickup([
        [0, 1, -1],
        [1, 0, -1],
        [1, 1, 1],
    ]) == 5

    # Example 2: single cell
    assert sol.cherryPickup([[1]]) == 1

    # All blocked except diagonal → 0 cherries
    assert sol.cherryPickup([
        [1, -1],
        [-1, 1],
    ]) == 0

    # Simple 2x2 grid
    assert sol.cherryPickup([
        [1, 1],
        [1, 1],
    ]) == 4

    # No cherries
    assert sol.cherryPickup([
        [0, 0],
        [0, 0],
    ]) == 0

    print("all tests passed")
