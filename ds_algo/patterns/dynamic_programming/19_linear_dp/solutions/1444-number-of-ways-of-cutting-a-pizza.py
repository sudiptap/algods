"""
1444. Number of Ways of Cutting a Pizza (Hard)
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

Problem:
    Given an r x c pizza grid with apples ('A') and empty ('.'), make k-1
    cuts to produce k pieces. Each cut is horizontal or vertical, giving
    the upper/left part to a person. Each piece must contain at least one
    apple. Count the number of ways.

Pattern: 19 - Linear DP

Approach:
    1. dp[r][c][k] = number of ways to cut the remaining pizza grid[r:][c:]
       into k pieces, each with at least one apple.
    2. Use 2D prefix sums to quickly count apples in any sub-rectangle.
    3. For horizontal cut at row i (r < i <= rows): upper part grid[r:i][c:]
       must have >= 1 apple, remaining grid[i:][c:] needs k-1 pieces.
    4. Similarly for vertical cut at column j.

Complexity:
    Time:  O(r * c * k * (r + c)) for transitions
    Space: O(r * c * k) for DP + O(r * c) for prefix sums
"""

from typing import List
from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])

        # Prefix sum: count of apples in pizza[i:][j:]
        # suffix[i][j] = number of apples in grid[i:rows][j:cols]
        suffix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                suffix[i][j] = (suffix[i + 1][j] + suffix[i][j + 1]
                                - suffix[i + 1][j + 1]
                                + (1 if pizza[i][j] == 'A' else 0))

        def has_apple(r1, c1, r2, c2):
            """Check if grid[r1:r2][c1:c2] has at least one apple."""
            return suffix[r1][c1] - suffix[r2][c1] - suffix[r1][c2] + suffix[r2][c2] > 0

        @lru_cache(maxsize=None)
        def dp(r, c, pieces):
            if pieces == 1:
                return 1 if has_apple(r, c, rows, cols) else 0

            result = 0
            # Horizontal cut at row i
            for i in range(r + 1, rows):
                if has_apple(r, c, i, cols):
                    result = (result + dp(i, c, pieces - 1)) % MOD

            # Vertical cut at column j
            for j in range(c + 1, cols):
                if has_apple(r, c, rows, j):
                    result = (result + dp(r, j, pieces - 1)) % MOD

            return result

        return dp(0, 0, k)


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    pizza = ["A..", "AAA", "..."]
    assert sol.ways(pizza, 3) == 3, f"Test 1 failed: {sol.ways(pizza, 3)}"

    # Test 2
    pizza = ["A..", "AA.", "..."]
    assert sol.ways(pizza, 3) == 1, f"Test 2 failed: {sol.ways(pizza, 3)}"

    # Test 3
    pizza = ["A..", "A..", "..."]
    assert sol.ways(pizza, 1) == 1, f"Test 3 failed: {sol.ways(pizza, 1)}"

    # Test 4: impossible
    pizza = ["A.."]
    assert sol.ways(pizza, 2) == 0, f"Test 4 failed: {sol.ways(pizza, 2)}"

    # Test 5
    pizza = ["..A.A", ".A...", "A.A.."]
    assert sol.ways(pizza, 3) == 14, f"Test 5 failed: {sol.ways(pizza, 3)}"

    print("All tests passed for 1444. Number of Ways of Cutting a Pizza!")


if __name__ == "__main__":
    run_tests()
