"""
3593. Minimum Increments to Equalize Leaf Paths
https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

Pattern: 09 - DP on Trees

---
APPROACH: Post-order traversal
- All root-to-leaf paths must have equal total weight.
- We can only increment edge weights (not decrement).
- Post-order: for each internal node, all subtrees must have the same
  max-depth (longest path to leaf). Increment shorter paths to match longest.
- Return total increments needed.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(300000)


class Solution:
    def minIncrements(self, n: int, edges: List[List[int]], weights: List[int]) -> int:
        adj = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, weights[i]))
            adj[v].append((u, weights[i]))

        total_inc = 0

        def dfs(v, parent):
            nonlocal total_inc
            children = [(u, w) for u, w in adj[v] if u != parent]
            if not children:
                return 0  # leaf, distance to leaf = 0

            child_depths = []
            for u, w in children:
                d = dfs(u, v) + w
                child_depths.append(d)

            max_depth = max(child_depths)
            for d in child_depths:
                total_inc += max_depth - d

            return max_depth

        dfs(0, -1)
        return total_inc


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple: 0-1(w=1), 0-2(w=2). Leaf paths: 1, 2. Increment edge to 1 by 1.
    res = sol.minIncrements(3, [[0, 1], [0, 2]], [1, 2])
    assert res == 1, f"Got {res}"

    # Balanced: all paths equal
    res = sol.minIncrements(3, [[0, 1], [0, 2]], [3, 3])
    assert res == 0, f"Got {res}"

    print("All tests passed!")
