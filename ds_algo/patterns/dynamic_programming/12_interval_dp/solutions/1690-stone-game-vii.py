"""
1690. Stone Game VII
https://leetcode.com/problems/stone-game-vii/

Pattern: 12 - Interval DP

---
APPROACH: Interval DP
- dp[i][j] = max score difference (current player - opponent) for stones[i..j].
- Current player picks either left or right stone. They score the sum of remaining.
- If pick left (stones[i]): score = sum(i+1..j), then opponent plays dp[i+1][j].
- If pick right (stones[j]): score = sum(i..j-1), then opponent plays dp[i][j-1].
- dp[i][j] = max(sum(i+1..j) - dp[i+1][j], sum(i..j-1) - dp[i][j-1])

Time: O(n^2)
Space: O(n^2)
---
"""

from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pick_left = range_sum(i + 1, j) - dp[i + 1][j]
                pick_right = range_sum(i, j - 1) - dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)

        return dp[0][n - 1]


# --- Tests ---
def test():
    sol = Solution()

    assert sol.stoneGameVII([5, 3, 1, 4, 2]) == 6
    assert sol.stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]) == 122
    assert sol.stoneGameVII([1, 2]) == 2  # pick the 1, score 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
