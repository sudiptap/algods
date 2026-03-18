"""
279. Perfect Squares (Medium)
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer (1, 4, 9, 16, ...).

Pattern: Unbounded Knapsack
- We can use each perfect square unlimited times (unbounded).
- dp[i] = minimum number of perfect squares that sum to i.
- Transition: dp[i] = min(dp[i - j*j] + 1) for all j where j*j <= i.
- Base case: dp[0] = 0 (zero squares sum to 0).

Time:  O(n * sqrt(n))
Space: O(n)
"""

import math
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """Return the fewest perfect squares that sum to n.

        Args:
            n: Target sum, 1 <= n <= 10^4.

        Returns:
            Minimum count of perfect square numbers summing to n.
        """
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]


# ---------- tests ----------
def test_perfect_squares():
    sol = Solution()

    # Example 1: 12 = 4 + 4 + 4
    assert sol.numSquares(12) == 3, f"Expected 3, got {sol.numSquares(12)}"

    # Example 2: 13 = 4 + 9
    assert sol.numSquares(13) == 2, f"Expected 2, got {sol.numSquares(13)}"

    # 1 is itself a perfect square
    assert sol.numSquares(1) == 1

    # 4 = 2^2
    assert sol.numSquares(4) == 1

    # 7 = 4 + 1 + 1 + 1
    assert sol.numSquares(7) == 4

    # Larger: 100 = 10^2
    assert sol.numSquares(100) == 1

    print("All tests passed for 279. Perfect Squares")


if __name__ == "__main__":
    test_perfect_squares()
