"""
1301. Number of Paths with Max Score (Hard)
https://leetcode.com/problems/number-of-paths-with-max-score/

Problem:
    Given a square board of characters, find the maximum sum of numeric
    characters you can collect moving from bottom-right to top-left,
    moving only up, left, or diagonally up-left. Also return the number
    of paths achieving this maximum. 'S' is start (bottom-right), 'E' is
    end (top-left), 'X' is obstacle.

Pattern: 10 - DP on Grids

Approach:
    1. dp[i][j] = (max_score, count) from cell (i,j) to (0,0).
    2. Process from bottom-right to top-left. For each cell, consider
       moves to (i-1,j), (i,j-1), (i-1,j-1).
    3. Skip obstacles. Merge results: pick max score, sum counts of
       paths achieving that max.
    4. Answer is dp[0][0], modulo 10^9+7.

Complexity:
    Time:  O(n^2) - visit each cell once, check 3 neighbors
    Space: O(n^2) for the DP table
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        # dp[i][j] = (max_score, count)
        dp = [[(-1, 0)] * n for _ in range(n)]

        # Start position (bottom-right)
        dp[n - 1][n - 1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    dp[i][j] = (-1, 0)
                    continue
                if i == n - 1 and j == n - 1:
                    continue

                best_score = -1
                best_count = 0

                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and dp[ni][nj][0] >= 0:
                        sc = dp[ni][nj][0]
                        ct = dp[ni][nj][1]
                        if sc > best_score:
                            best_score = sc
                            best_count = ct
                        elif sc == best_score:
                            best_count = (best_count + ct) % MOD

                if best_score >= 0:
                    val = 0 if board[i][j] in ('E', 'S') else int(board[i][j])
                    dp[i][j] = (best_score + val, best_count)
                else:
                    dp[i][j] = (-1, 0)

        if dp[0][0][0] < 0:
            return [0, 0]
        return [dp[0][0][0] % MOD, dp[0][0][1] % MOD]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    board = ["E23", "2X2", "12S"]
    assert sol.pathsWithMaxScore(board) == [7, 1], f"Test 1 failed: {sol.pathsWithMaxScore(board)}"

    # Test 2
    board = ["E12", "1X1", "21S"]
    assert sol.pathsWithMaxScore(board) == [4, 2], f"Test 2 failed: {sol.pathsWithMaxScore(board)}"

    # Test 3: blocked
    board = ["E1", "XS"]
    # Path: S(1,1)->left(1,0)=X blocked, up(0,1)=1, diag(0,0)=E
    # only path through (0,1): score=1
    assert sol.pathsWithMaxScore(board) == [1, 1], f"Test 3 failed: {sol.pathsWithMaxScore(board)}"

    # Test 4: diagonal path only (S -> E directly)
    board = ["EX", "XS"]
    assert sol.pathsWithMaxScore(board) == [0, 1], f"Test 4 failed: {sol.pathsWithMaxScore(board)}"

    # Test 5: 1x1 trivial (just E and S same cell conceptually not valid, but let's test)
    # Actually per problem, min size is 2x2

    print("All tests passed for 1301. Number of Paths with Max Score!")


if __name__ == "__main__":
    run_tests()
