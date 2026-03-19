"""
1563. Stone Game V
https://leetcode.com/problems/stone-game-v/

Pattern: 12 - Interval DP

---
APPROACH: Interval DP
- dp[i][j] = max score Alice can get from stones[i..j]
- For each split point k, left = sum(i..k), right = sum(k+1..j)
- If left < right: Alice gets left + dp[i][k]
- If left > right: Alice gets right + dp[k+1][j]
- If left == right: Alice picks the better side
- Use prefix sums for O(1) range sum queries.

Time: O(n^3) where n = len(stoneValue)
Space: O(n^2)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0
            res = 0
            for k in range(i, j):
                left = range_sum(i, k)
                right = range_sum(k + 1, j)
                if left < right:
                    res = max(res, left + dp(i, k))
                elif left > right:
                    res = max(res, right + dp(k + 1, j))
                else:
                    res = max(res, left + max(dp(i, k), dp(k + 1, j)))
            return res

        return dp(0, n - 1)


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.stoneGameV([6, 2, 3, 4, 5, 5]) == 18

    # Example 2
    assert sol.stoneGameV([7, 7, 7, 7, 7, 7, 7]) == 28

    # Example 3
    assert sol.stoneGameV([4]) == 0

    # Two elements
    assert sol.stoneGameV([3, 3]) == 3

    # Two different
    assert sol.stoneGameV([1, 5]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
