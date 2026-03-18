"""
688. Knight Probability in Chessboard (Medium)
https://leetcode.com/problems/knight-probability-in-chessboard/

Pattern: 17 - Probability DP

---
APPROACH: 3D DP (moves x grid), space-optimised to two layers.
- dp[i][j] = probability of the knight being at cell (i, j) after the
  current number of moves.
- For each move, propagate probability from every cell to its 8 knight
  destinations.  Each destination gets dp[i][j] / 8.
- If a destination is off the board, that probability mass is lost
  (the knight fell off).
- Base: dp[row][column] = 1.0 (knight starts here with certainty).
- Answer: sum of all dp values after k moves.

Time:  O(k * n * n)
Space: O(n * n)
---
"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """Return the probability that the knight remains on the board after k moves.

        Args:
            n: Size of the n x n chessboard.
            k: Number of moves the knight will make.
            row: Starting row (0-indexed).
            column: Starting column (0-indexed).

        Returns:
            Probability of the knight still being on the board.
        """
        DIRS = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1),
        ]

        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp[i][j] == 0.0:
                        continue
                    prob = dp[i][j] / 8.0
                    for di, dj in DIRS:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            new_dp[ni][nj] += prob
            dp = new_dp

        return sum(dp[i][j] for i in range(n) for j in range(n))


# ---------- Tests ----------
def test_knight_probability():
    sol = Solution()

    # Example 1: n=3, k=2, row=0, col=0
    assert abs(sol.knightProbability(3, 2, 0, 0) - 0.0625) < 1e-6

    # Example 2: only 1 cell, no move -> prob = 1
    assert abs(sol.knightProbability(1, 0, 0, 0) - 1.0) < 1e-6

    # 1x1 board, 1 move -> all 8 destinations are off board
    assert abs(sol.knightProbability(1, 1, 0, 0) - 0.0) < 1e-6

    # Center of 3x3 board, 1 move: 0 of 8 destinations on board
    assert abs(sol.knightProbability(3, 1, 1, 1) - 0.0) < 1e-6

    # Larger board, 0 moves -> always on board
    assert abs(sol.knightProbability(8, 0, 4, 4) - 1.0) < 1e-6

    # n=8, k=30 from center: known expected value
    result = sol.knightProbability(8, 30, 6, 4)
    assert 0.0 < result < 1.0  # sanity check

    print("All tests passed for 688. Knight Probability in Chessboard")


if __name__ == "__main__":
    test_knight_probability()
