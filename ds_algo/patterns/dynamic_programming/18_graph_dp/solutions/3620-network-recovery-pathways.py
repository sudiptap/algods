"""
3620. Network Recovery Pathways
https://leetcode.com/problems/network-recovery-pathways/

Pattern: 18 - Graph DP

---
APPROACH: Binary search + BFS (or modified Dijkstra for bottleneck)
- Find the path from source to target that maximizes the minimum edge weight
  (bottleneck path / widest path).
- Binary search on the answer: for threshold t, check if there's a path
  using only edges with weight >= t.
- Or: modified Dijkstra / max-heap BFS to find the widest path.

Time: O(E log V) with heap  Space: O(V + E)
---
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxBottleneck(self, n: int, edges: List[List[int]], source: int, target: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Max-heap (negate for min-heap): maximize minimum weight on path
        # dist[v] = max bottleneck to reach v
        dist = [-1] * n
        dist[source] = float('inf')
        heap = [(-float('inf'), source)]  # (-bottleneck, node)

        while heap:
            neg_bw, u = heapq.heappop(heap)
            bw = -neg_bw
            if bw < dist[u]:
                continue
            if u == target:
                return bw
            for v, w in adj[u]:
                new_bw = min(bw, w)
                if new_bw > dist[v]:
                    dist[v] = new_bw
                    heapq.heappush(heap, (-new_bw, v))

        return -1  # unreachable


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple: 0->1(w=3), 0->2(w=5), 2->1(w=4). Widest path 0->2->1: min(5,4)=4. Direct: 3.
    res = sol.maxBottleneck(3, [[0,1,3],[0,2,5],[2,1,4]], 0, 1)
    assert res == 4, f"Got {res}"

    # Direct path only
    res = sol.maxBottleneck(2, [[0,1,7]], 0, 1)
    assert res == 7, f"Got {res}"

    print("All tests passed!")
