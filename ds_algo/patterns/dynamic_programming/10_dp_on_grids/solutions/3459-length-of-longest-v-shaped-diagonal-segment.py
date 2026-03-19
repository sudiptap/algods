"""
3459. Length of Longest V-Shaped Diagonal Segment
https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

Pattern: 10 - DP on Grids

---
APPROACH: DFS/memoized DP per diagonal direction.
- Sequence: starts with 1, then alternates 2, 0, 2, 0, ...
- 4 diagonal directions: (-1,1), (1,1), (1,-1), (-1,-1).
- At most one clockwise 90-degree turn allowed.
- dfs(r, c, turned, expected_num, dir) = max length from (r,c).
- Start from each cell with value 1, try all 4 initial directions.

Time: O(m * n * 4 * 2 * 2)  Space: O(m * n * 4 * 2 * 2)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = ((-1, 1), (1, 1), (1, -1), (-1, -1))

        @lru_cache(maxsize=None)
        def dfs(r, c, turned, num, d):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if grid[r][c] != num:
                return 0

            next_num = 0 if num == 2 else 2
            dr, dc = DIRS[d]
            res = 1 + dfs(r + dr, c + dc, turned, next_num, d)

            if not turned:
                nd = (d + 1) % 4
                ndr, ndc = DIRS[nd]
                res = max(res, 1 + dfs(r + ndr, c + ndc, True, next_num, nd))

            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d, (dr, dc) in enumerate(DIRS):
                        ans = max(ans, 1 + dfs(i + dr, j + dc, False, 2, d))

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.lenOfVDiagonal([[2, 2, 1, 2, 2], [2, 0, 2, 2, 0], [2, 0, 1, 1, 0], [1, 0, 2, 2, 2], [2, 0, 0, 2, 2]]) == 5
    assert sol.lenOfVDiagonal([[1]]) == 1
    assert sol.lenOfVDiagonal([[0]]) == 0

    print("Solution: all tests passed")
