"""
2209. Minimum White Tiles After Covering With Carpets
https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

Pattern: 19 - Linear DP

---
APPROACH: dp[i][j] = min white tiles in first i tiles using j carpets
- Base: dp[0][j] = 0
- Transition: dp[i][j] = min(dp[i-1][j] + (floor[i-1]=='1'), dp[i-carpetLen][j-1])
  Either don't place carpet at position i, or place carpet ending at i.
- Answer: dp[n][numCarpets]

Time: O(n * numCarpets)  Space: O(n * numCarpets)
---
"""

from typing import List


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j] = min white tiles considering first i tiles with j carpets
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(numCarpets + 1):
                # Option 1: don't place a carpet ending here
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                # Option 2: place a carpet ending at position i (covers i-carpetLen+1..i)
                if j > 0:
                    prev = max(0, i - carpetLen)
                    dp[i][j] = min(dp[i][j], dp[prev][j - 1])

        return dp[n][numCarpets]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumWhiteTiles("10110101", 2, 2) == 2
    assert sol.minimumWhiteTiles("11111", 2, 3) == 0
    assert sol.minimumWhiteTiles("101111", 2, 3) == 0
    assert sol.minimumWhiteTiles("0", 1, 1) == 0
    assert sol.minimumWhiteTiles("1", 0, 1) == 1

    print("all tests passed")
