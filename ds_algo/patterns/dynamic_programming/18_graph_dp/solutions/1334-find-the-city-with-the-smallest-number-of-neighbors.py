"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium)
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

Pattern: 18 - Graph DP

---
APPROACH: Floyd-Warshall
- Compute all-pairs shortest paths using Floyd-Warshall.
- For each city, count how many other cities are reachable within
  distanceThreshold.
- Return the city with the smallest count; break ties by choosing
  the city with the largest index.

Time:  O(n^3)
Space: O(n^2)
---
"""

from typing import List
import math


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """Return the city with the smallest number of reachable cities
        within distanceThreshold. Ties broken by largest index."""
        # Initialize distance matrix
        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                if dist[i][k] == math.inf:
                    continue
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Count reachable cities for each city
        best_city = -1
        best_count = math.inf
        for i in range(n):
            count = sum(1 for j in range(n) if j != i and dist[i][j] <= distanceThreshold)
            if count <= best_count:
                best_count = count
                best_city = i

        return best_city


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.findTheCity(
        4,
        [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],
        4
    ) == 3

    # Example 2
    assert sol.findTheCity(
        5,
        [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
        2
    ) == 0

    # Two disconnected cities
    assert sol.findTheCity(2, [], 10) == 1  # both have count 0, pick larger

    # Single city
    assert sol.findTheCity(1, [], 0) == 0

    print("all tests passed")
