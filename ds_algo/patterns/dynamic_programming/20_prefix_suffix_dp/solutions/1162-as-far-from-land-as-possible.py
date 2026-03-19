"""
1162. As Far from Land as Possible (Medium)

Pattern: 20_prefix_suffix_dp
- Multi-source BFS from all land cells to find the water cell farthest from any land.

Approach:
- Initialize a queue with all land cells (value 1).
- BFS outward, level by level. Each level increments distance by 1.
- The last distance reached is the answer.
- If there are no water cells or no land cells, return -1.

Complexity:
- Time:  O(n^2) where n is the grid side length
- Space: O(n^2)
"""

from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) == 0 or len(q) == n * n:
            return -1

        dist = -1
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

        return dist


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2

    # Example 2
    assert sol.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4

    # All land
    assert sol.maxDistance([[1, 1], [1, 1]]) == -1

    # All water
    assert sol.maxDistance([[0, 0], [0, 0]]) == -1

    # Corner land
    assert sol.maxDistance([[1, 0], [0, 0]]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
