"""
2912. Number of Ways to Reach Destination in the Grid
(LeetCode 2912: Number of Ways to Reach Destination in a Grid)

Pattern: 15 - Counting / Combinatorial (Combinatorics with DP)

---
APPROACH: We have a grid of n rows and m columns. Count paths from (0,0) to
(n-1,m-1) moving right or down, but some cells are blocked. This is a standard
grid DP if there are blocked cells; if unrestricted it's C(n+m-2, n-1).
Using inclusion-exclusion with blocked cells sorted by position.

For the general version: dp[i][j] = number of paths from (0,0) to (i,j).

Time: O(n*m)  Space: O(m)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def numberOfWays(self, n: int, m: int, k: int) -> int:
        # Problem 2912: n x m grid, exactly k moves.
        # From any cell can move to any cell in same row or column (not staying).
        # After exactly k moves, count paths from (0,0) to (n-1, m-1).

        # States: (row, col) but with symmetry, only need to track
        # whether we're at target row and target col.
        # 4 states: (target_row & target_col), (target_row & !target_col),
        # (!target_row & target_col), (!target_row & !target_col)

        # Transitions from (tr, tc): same row other col: (tr, !tc) has (m-1) choices
        # same col other row: (!tr, tc) has (n-1) choices
        # From (!tr, tc): same row: (!tr, !tc) m-1 choices, (!tr, tc) 0... wait
        # Actually from any cell, we move to any other cell in same row or same col.
        # From (r,c), can go to (r, c') for c'!=c: m-1 choices, or (r', c) for r'!=r: n-1 choices

        # State: (is_target_row, is_target_col)
        # a = at (target_row, target_col) = 1 cell
        # b = at (target_row, other_col) = m-1 cells
        # c = at (other_row, target_col) = n-1 cells
        # d = at (other_row, other_col) = (n-1)(m-1) cells

        # From a: to b (m-1 ways), to c (n-1 ways)
        # From b: to a (1 way, same row), to other b ((m-2) ways), to d ((n-1) ways)
        # From c: to a (1 way, same col), to d ((m-1) ways), to other c ((n-2) ways)
        # From d: to b (1 way, same row target col... wait)

        # Let me think in terms of aggregated counts:
        # A = # paths ending at target cell
        # B = # paths ending at (target_row, non-target_col) -- total across all such cells
        # C = # paths ending at (non-target_row, target_col)
        # D = # paths ending at (non-target_row, non-target_col)

        # From A (1 cell): goes to any of m-1 cells in row (contributes to B)
        #                   goes to any of n-1 cells in col (contributes to C)
        # From B (m-1 cells, each can go to): same row cells: 1 to A, m-2 to other B cells
        #                                      same col cells: n-1 to D cells
        # Total from B: to A: B*1, to B: B*(m-2), to C: 0, to D: B*(n-1)
        # From C: to A: C*1, to B: 0, to C: C*(n-2), to D: C*(m-1)
        # From D: to A: 0, to B: D*1 (go to target_col same row), to C: D*1 (go to target_row same col)
        #         to D: D*(m-2) + D*(n-2) = D*(m+n-4)
        # Wait, from a cell in D at (r,c) where r!=tr, c!=tc:
        #   same row: (r, tc) -> C, and (r, c') for c'!=c, c'!=tc -> D: m-2 cells
        #   same col: (tr, c) -> B, and (r', c) for r'!=r, r'!=tr -> D: n-2 cells
        # So from each D cell: 1 to C-type, 1 to B-type, (m-2)+(n-2) to D-type
        # Aggregated from D (total D paths): to B: D, to C: D, to D: D*(m+n-4)

        a, b, c, d = 1, 0, 0, 0  # start at (0,0) which is the source

        # But wait - source is (0,0), target is (n-1, m-1).
        # If n==1 and m==1, target=source, so a=1 initially.
        # Otherwise, (0,0) relative to target (n-1,m-1):
        # if n==1: source is at target row, non-target col -> b
        # if m==1: source is at target col, non-target row -> c
        # else: source is at non-target row, non-target col -> d

        if n == 1 and m == 1:
            a, b, c, d = 1, 0, 0, 0
        elif n == 1:
            a, b, c, d = 0, 1, 0, 0
        elif m == 1:
            a, b, c, d = 0, 0, 1, 0
        else:
            a, b, c, d = 0, 0, 0, 1

        for _ in range(k):
            na = (b + c) % MOD
            nb = (a * (m - 1) + b * (m - 2) + d) % MOD
            nc = (a * (n - 1) + c * (n - 2) + d) % MOD
            nd = (b * (n - 1) + c * (m - 1) + d * (m + n - 4)) % MOD
            a, b, c, d = na, nb, nc, nd

        return a


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfWays(2, 2, 2) == 2
    assert sol.numberOfWays(1, 1, 0) == 1

    print("All tests passed!")
