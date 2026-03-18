"""
1976. Number of Ways to Arrive at Destination
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

Pattern: 18 - Graph DP (Dijkstra + path counting)

---
APPROACH: Modified Dijkstra that also tracks path counts.
- dist[i] = shortest distance from 0 to i.
- ways[i] = number of shortest paths from 0 to i.
- When we find a shorter path to v, reset ways[v] = ways[u].
- When we find an equal-length path to v, add ways[u] to ways[v].
- Return ways[n-1] mod 10^9+7.

Time: O(E log V)  Space: O(V + E)
---
"""

from typing import List
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """Return number of shortest paths from node 0 to node n-1, mod 10^9+7."""
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD


# --- Tests ---
def test():
    sol = Solution()

    # Example 1: 7 nodes, multiple shortest paths
    assert sol.countPaths(7, [
        [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
        [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
        [0, 4, 5], [4, 6, 2]
    ]) == 4

    # Example 2: 2 nodes, single path
    assert sol.countPaths(2, [[1, 0, 10]]) == 1

    # Single node
    assert sol.countPaths(1, []) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
