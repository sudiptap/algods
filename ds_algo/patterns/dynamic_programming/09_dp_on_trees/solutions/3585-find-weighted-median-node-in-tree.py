"""
3585. Find Weighted Median Node in Tree
https://leetcode.com/problems/find-weighted-median-node-in-tree/

Pattern: 09 - DP on Trees

---
APPROACH: Rerooting DP
- Weighted median node minimizes sum of weight[v] * dist(root, v) for all v.
- Compute total weighted distance from an initial root (node 0).
- Rerooting: when moving root from u to adjacent v via edge of weight w:
  - Nodes in subtree(v) get closer by w, others get farther by w.
  - total_dist changes by w * (total_weight - 2 * subtree_weight[v]).
- The median node is where moving to any neighbor increases total distance
  (or equivalently, subtree_weight >= total_weight/2 for all children).

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(300000)


class Solution:
    def findWeightedMedianNode(self, n: int, edges: List[List[int]], weights: List[int]) -> int:
        if n == 1:
            return 0

        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        subtree_w = [0] * n
        dist_from_root = [0] * n
        total_weight = sum(weights)

        # First DFS: compute subtree weights and total weighted distance from root 0
        def dfs1(v, par):
            subtree_w[v] = weights[v]
            for u, w in adj[v]:
                if u != par:
                    dist_from_root[u] = dist_from_root[v] + w
                    dfs1(u, v)
                    subtree_w[v] += subtree_w[u]

        dfs1(0, -1)
        total_dist = sum(weights[i] * dist_from_root[i] for i in range(n))

        # Rerooting: find node minimizing total weighted distance
        best_node = 0
        best_dist = total_dist
        node_dist = [0] * n
        node_dist[0] = total_dist

        def dfs2(v, par):
            nonlocal best_node, best_dist
            for u, w in adj[v]:
                if u != par:
                    # Moving root from v to u:
                    # subtree(u) gets closer by w, rest gets farther by w
                    node_dist[u] = node_dist[v] + w * (total_weight - 2 * subtree_w[u])
                    if node_dist[u] < best_dist or (node_dist[u] == best_dist and u < best_node):
                        best_dist = node_dist[u]
                        best_node = u
                    dfs2(u, v)

        dfs2(0, -1)
        return best_node


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple line: 0-1-2, weights [1,1,1], edge weights all 1
    res = sol.findWeightedMedianNode(3, [[0,1,1],[1,2,1]], [1,1,1])
    assert res == 1, f"Got {res}"  # middle node

    # Single node
    assert sol.findWeightedMedianNode(1, [], [5]) == 0

    # Star: center is best
    res = sol.findWeightedMedianNode(4, [[0,1,1],[0,2,1],[0,3,1]], [1,1,1,1])
    assert res == 0, f"Got {res}"

    print("All tests passed!")
