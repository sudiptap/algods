"""
1617. Count Subtrees With Max Distance Between Cities
https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

Pattern: 11 - Bitmask DP

---
APPROACH: Enumerate all subsets, check connected, compute diameter
- n <= 15, so enumerate all 2^n subsets of cities.
- For each subset with >= 2 cities:
  1. Check if it forms a connected subtree (edges = nodes - 1 in the subset)
  2. Compute the diameter (max pairwise distance) using BFS/Floyd-Warshall
- Precompute all-pairs shortest paths with BFS from each node.
- Count subsets by their diameter d for d = 1..n-1.

Time: O(2^n * n^2) - enumerate subsets, check connectivity and diameter
Space: O(n^2 + 2^n)
---
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list (0-indexed)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        # Precompute all-pairs shortest paths via BFS
        dist = [[0] * n for _ in range(n)]
        for start in range(n):
            visited = [False] * n
            q = deque([start])
            visited[start] = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        dist[start][v] = dist[start][u] + 1
                        q.append(v)

        result = [0] * (n - 1)

        # Enumerate all subsets of size >= 2
        for mask in range(3, 1 << n):
            nodes = [i for i in range(n) if mask & (1 << i)]
            if len(nodes) < 2:
                continue

            # Check connectivity: count edges in subset, must be len(nodes)-1
            edge_count = 0
            for u in nodes:
                for v in adj[u]:
                    if v > u and (mask & (1 << v)):
                        edge_count += 1
            if edge_count != len(nodes) - 1:
                continue

            # Compute diameter
            diameter = 0
            for i in range(len(nodes)):
                for j in range(i + 1, len(nodes)):
                    diameter = max(diameter, dist[nodes[i]][nodes[j]])

            if 1 <= diameter <= n - 1:
                result[diameter - 1] += 1

        return result


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]) == [3, 4, 0]

    # Example 2
    assert sol.countSubgraphsForEachDiameter(2, [[1, 2]]) == [1]

    # Example 3
    assert sol.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]) == [2, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
