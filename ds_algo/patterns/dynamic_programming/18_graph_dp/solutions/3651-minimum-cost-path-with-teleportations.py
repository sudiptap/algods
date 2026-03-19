"""
3651. Minimum Cost Path with Teleportations
https://leetcode.com/problems/minimum-cost-path-with-teleportations/

Pattern: 18 - Graph DP

---
APPROACH: Dijkstra with teleport edges
- Graph with normal weighted edges + teleportation portals.
- Portals: pairs of nodes that can teleport between each other at fixed cost.
- Add teleport edges to the graph, then run Dijkstra from source to target.

Time: O((V + E) log V)  Space: O(V + E)
---
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minCostPath(self, n: int, edges: List[List[int]], teleports: List[List[int]],
                    source: int, target: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Add teleport edges
        for u, v, cost in teleports:
            adj[u].append((v, cost))
            adj[v].append((u, cost))

        # Dijkstra
        dist = [float('inf')] * n
        dist[source] = 0
        heap = [(0, source)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            if u == target:
                return d
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        return -1 if dist[target] == float('inf') else dist[target]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Normal path 0->1->2 cost 5+5=10, teleport 0->2 cost 3.
    res = sol.minCostPath(3, [[0,1,5],[1,2,5]], [[0,2,3]], 0, 2)
    assert res == 3, f"Got {res}"

    # No teleports
    res = sol.minCostPath(3, [[0,1,2],[1,2,3]], [], 0, 2)
    assert res == 5, f"Got {res}"

    print("All tests passed!")
