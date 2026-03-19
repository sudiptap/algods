"""
1786. Number of Restricted Paths From First to Last Node
https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

Pattern: 18 - Graph DP

---
APPROACH: Dijkstra from last node + DFS with memoization
- Run Dijkstra from node n to compute distToLastNode[v] for all v.
- A restricted path from u to v requires distToLastNode[u] > distToLastNode[v].
- Count paths from node 1 to node n using memoized DFS:
  dp[u] = number of restricted paths from u to n.
  dp[n] = 1. For other u: dp[u] = sum of dp[v] for neighbors v where dist[u] > dist[v].

Time: O(E log V) for Dijkstra + O(V + E) for DFS
Space: O(V + E)
---
"""

from typing import List
from collections import defaultdict
import heapq
from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        # DFS with memoization
        @lru_cache(maxsize=None)
        def dp(u):
            if u == n:
                return 1
            total = 0
            for v, w in graph[u]:
                if dist[u] > dist[v]:
                    total = (total + dp(v)) % MOD
            return total

        return dp(1)


# --- Tests ---
def test():
    sol = Solution()

    assert sol.countRestrictedPaths(5, [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]) == 3
    assert sol.countRestrictedPaths(7, [[1, 3, 1], [4, 1, 2], [7, 3, 4], [2, 5, 3], [5, 6, 1], [6, 7, 2], [7, 5, 3], [2, 6, 4]]) == 1

    # Simple path
    assert sol.countRestrictedPaths(2, [[1, 2, 1]]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
