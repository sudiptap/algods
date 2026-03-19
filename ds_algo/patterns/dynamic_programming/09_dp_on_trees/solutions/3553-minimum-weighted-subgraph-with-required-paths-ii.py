"""
3553. Minimum Weighted Subgraph With Required Paths II
https://leetcode.com/problems/minimum-weighted-subgraph-with-required-paths-ii/

Pattern: 09 - DP on Trees

---
APPROACH: Tree DP on LCA
- Given a weighted tree and queries (src, dest), find for each query the
  minimum weight subgraph that connects src to dest.
- On a tree, the unique path between two nodes IS the minimum subgraph.
- Compute the path weight between nodes using LCA with weighted distance.
- Preprocess: root the tree, compute depth[] and dist[] (weighted distance
  from root). Use binary lifting for LCA.
- Answer for query (u,v) = dist[u] + dist[v] - 2*dist[lca(u,v)].

Time: O((n + q) log n)  Space: O(n log n)
---
"""

from typing import List
from collections import defaultdict
import math


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = max(1, int(math.log2(n)) + 1) if n > 1 else 1
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n

        # BFS to set up parent, depth, dist
        from collections import deque
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    queue.append(v)

        # Binary lifting
        for k in range(1, LOG):
            for v in range(n):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        ans = []
        for src, dest in queries:
            l = lca(src, dest)
            ans.append(dist[src] + dist[dest] - 2 * dist[l])
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    res = sol.minimumWeight(5, [[0,1,3],[1,2,1],[1,3,2],[3,4,1]], [[0,2],[1,4],[3,0]])
    assert res == [4, 3, 5], f"Got {res}"

    # Simple: two nodes
    res = sol.minimumWeight(2, [[0,1,7]], [[0,1],[1,0]])
    assert res == [7, 7]

    print("All tests passed!")
