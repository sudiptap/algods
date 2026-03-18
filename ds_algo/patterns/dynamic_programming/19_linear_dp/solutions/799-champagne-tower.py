"""
799. Champagne Tower
https://leetcode.com/problems/champagne-tower/

Pattern: 19 - Linear DP

---
APPROACH: Simulation — pour from top, overflow splits equally to two glasses below.
- dp[i][j] = total liquid poured into glass at row i, column j
- Start by pouring all `poured` cups into dp[0][0].
- For each glass, if it has more than 1 cup, the excess overflows equally
  to the two glasses directly below: dp[i+1][j] and dp[i+1][j+1].
- The amount in a glass is min(dp[i][j], 1.0).
- Optimize space: only need current row and next row.

Time: O(query_row^2)  Space: O(query_row)
---
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """Return how full the glass at (query_row, query_glass) is (0.0 to 1.0)."""
        # dp[j] = total liquid poured into glass j of current row
        dp = [0.0] * (query_row + 2)
        dp[0] = float(poured)

        for row in range(query_row):
            new_dp = [0.0] * (query_row + 2)
            for j in range(row + 1):
                overflow = dp[j] - 1.0
                if overflow > 0:
                    new_dp[j] += overflow / 2.0
                    new_dp[j + 1] += overflow / 2.0
            dp = new_dp

        return min(1.0, dp[query_glass])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: 1 cup poured, check (1, 1) — not enough to overflow
    assert sol.champagneTower(1, 1, 1) == 0.0

    # Example 2: 2 cups poured, check (1, 1) — 0.5 overflow to each side
    assert sol.champagneTower(2, 1, 1) == 0.5

    # Large pour, top glass is full
    assert sol.champagneTower(100000009, 33, 17) == 1.0

    # Edge: 0 cups poured
    assert sol.champagneTower(0, 0, 0) == 0.0

    # 1 cup, top glass is exactly full
    assert sol.champagneTower(1, 0, 0) == 1.0

    # 2 cups into top glass — top full, each below gets 0.5
    assert sol.champagneTower(2, 1, 0) == 0.5

    print("all tests passed")
