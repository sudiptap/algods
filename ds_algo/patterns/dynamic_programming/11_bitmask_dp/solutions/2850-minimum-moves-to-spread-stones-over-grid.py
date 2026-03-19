"""
2850. Minimum Moves to Spread Stones Over Grid
https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

Pattern: 11 - Bitmask DP (matching sources to targets)

---
APPROACH: Collect cells with 0 stones (targets) and cells with >1 stones
(sources, expanded by count-1). Try all permutations of matching sources to
targets, minimize total Manhattan distance. Since grid is 3x3, at most 9
sources/targets.

Time: O(k! * k) where k <= 9  Space: O(k)
---
"""

from typing import List
from itertools import permutations


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        sources = []
        targets = []

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    targets.append((i, j))
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        sources.append((i, j))

        if not targets:
            return 0

        ans = float('inf')
        for perm in permutations(sources):
            cost = sum(abs(perm[i][0] - targets[i][0]) + abs(perm[i][1] - targets[i][1])
                      for i in range(len(targets)))
            ans = min(ans, cost)
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumMoves([[1,1,0],[1,1,1],[1,2,1]]) == 3
    assert sol.minimumMoves([[1,3,0],[1,0,0],[1,0,3]]) == 4

    print("All tests passed!")
