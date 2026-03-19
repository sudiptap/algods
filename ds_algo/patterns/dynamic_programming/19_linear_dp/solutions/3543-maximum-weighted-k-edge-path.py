"""
3543. Maximum Weighted K-Edge Path
https://leetcode.com/problems/maximum-weighted-k-edge-path/

Pattern: 19 - Linear DP

---
APPROACH: dp[node][edges_used] = max weight of path ending at node using edges_used edges
- Build adjacency list from edges with weights.
- For each node, dp[node][0] = 0 (path of 0 edges).
- For each edge count from 1..k, relax over all edges.
- Answer is max(dp[node][k]) for all nodes, or -1 if none.

Time: O(k * E)  Space: O(n * k)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int) -> int:
        """Return the maximum total edge weight of a path with exactly k edges."""
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        NEG_INF = float('-inf')
        # dp[node][j] = max weight path ending at node with j edges
        dp = [[NEG_INF] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0

        for j in range(1, k + 1):
            for u in range(n):
                if dp[u][j - 1] == NEG_INF:
                    continue
                for v, w in adj[u]:
                    dp[v][j] = max(dp[v][j], dp[u][j - 1] + w)

        ans = max(dp[node][k] for node in range(n))
        return ans if ans != NEG_INF else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maxWeight(3, [[0, 1, 1], [1, 2, 2]], 2) == 3
    # Example 2: no path of length 3
    assert sol.maxWeight(3, [[0, 1, 1], [1, 2, 2]], 3) == -1
    # Example 3
    assert sol.maxWeight(3, [[0, 1, 6], [1, 2, -1], [0, 2, 3]], 1) == 6
    # Single node, k=0 not possible since k>=1 per constraints?
    # k=1 with self-loop or simple edge
    assert sol.maxWeight(2, [[0, 1, 5]], 1) == 5

    print("All tests passed!")
