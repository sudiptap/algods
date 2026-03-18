"""
1340. Jump Game V (Hard)
https://leetcode.com/problems/jump-game-v/

Pattern: 19 - Linear DP

---
APPROACH: DFS + Memoization
- From index i you can jump to index j (|i - j| <= d) if:
    - arr[j] < arr[i], AND
    - all values between i and j are also strictly less than arr[i].
- dp[i] = max number of indices you can visit starting from i.
- DFS from each index, caching results. For each index, expand left and
  right up to distance d, stopping as soon as a value >= arr[i] is hit.

Time:  O(n * d)
Space: O(n)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """Return the maximum number of indices you can visit."""
        n = len(arr)

        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            best = 1  # at least visit i itself
            # Expand left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            # Expand right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            return best

        return max(dfs(i) for i in range(n))


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2) == 4

    # Example 2
    assert sol.maxJumps([3, 3, 3, 3, 3], 3) == 1

    # Example 3
    assert sol.maxJumps([7, 6, 5, 4, 3, 2, 1], 1) == 7

    # Single element
    assert sol.maxJumps([5], 1) == 1

    # Two elements, can jump
    assert sol.maxJumps([2, 1], 1) == 2

    # Two elements, equal (no jump)
    assert sol.maxJumps([2, 2], 1) == 1

    print("all tests passed")
