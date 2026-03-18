"""
877. Stone Game
https://leetcode.com/problems/stone-game/

Pattern: 12 - Interval DP

---
APPROACH: dp[i][j] = max score difference for the current player from piles[i..j].
- Current player picks piles[i] or piles[j], then becomes the "behind" player.
- dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
- Base case: dp[i][i] = piles[i] (only one pile left, take it).
- If dp[0][n-1] > 0, first player (Alice) wins.

Math shortcut: Alice always wins because the pile count is even and total is odd,
so she can always choose to take all even-indexed or all odd-indexed piles,
whichever sum is larger. But the DP approach is shown for learning.

Time: O(n^2)  Space: O(n^2)
---
"""

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """Return True if Alice (first player) wins the stone game."""
        n = len(piles)
        # dp[i][j] = max score diff the current player can achieve from piles[i..j]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    piles[i] - dp[i + 1][j],
                    piles[j] - dp[i][j - 1],
                )

        return dp[0][n - 1] > 0


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.stoneGame([5, 3, 4, 5]) is True
    assert sol.stoneGame([3, 7, 2, 3]) is True
    # Alice can always win with even-length piles and odd total
    assert sol.stoneGame([1, 2]) is True
    assert sol.stoneGame([1, 100, 2, 99]) is True

    print("all tests passed")
