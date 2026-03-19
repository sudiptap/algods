"""
1548. The Most Similar Path in a Graph
https://leetcode.com/problems/the-most-similar-path-in-a-graph/

Pattern: 18 - Graph DP

---
APPROACH: DP on graph with path reconstruction
- dp[step][node] = minimum number of name edits to match targetPath[:step+1]
  ending at node
- Transition: dp[step][v] = min over all neighbors u of dp[step-1][u] + cost(v, step)
  where cost = 0 if names[v] == targetPath[step], else 1
- Base: dp[0][v] = 0 if names[v] == targetPath[0], else 1
- Reconstruct path by tracking parent at each step.

Time: O(T * E) where T = len(targetPath), E = number of edges
Space: O(T * n) where n = number of nodes
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str],
                    targetPath: List[str]) -> List[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        T = len(targetPath)

        # dp[t][v] = min edits for path of length t+1 ending at v
        INF = float('inf')
        dp = [[INF] * n for _ in range(T)]
        parent = [[-1] * n for _ in range(T)]

        # Base case
        for v in range(n):
            dp[0][v] = 0 if names[v] == targetPath[0] else 1

        # Fill DP
        for t in range(1, T):
            cost_t = targetPath[t]
            for v in range(n):
                edit = 0 if names[v] == cost_t else 1
                for u in graph[v]:
                    if dp[t - 1][u] + edit < dp[t][v]:
                        dp[t][v] = dp[t - 1][u] + edit
                        parent[t][v] = u

        # Find best ending node
        best_node = min(range(n), key=lambda v: dp[T - 1][v])

        # Reconstruct path
        path = [0] * T
        path[T - 1] = best_node
        for t in range(T - 2, -1, -1):
            path[t] = parent[t + 1][path[t + 1]]

        return path


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    result = sol.mostSimilar(
        5,
        [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
        ["ATL", "PEK", "LAX", "DXB", "HND"],
        ["ATL", "DXB", "HND", "LAX"]
    )
    assert len(result) == 4
    # Valid answer: [0, 2, 4, 2] with edit distance 1

    # Example 2
    result = sol.mostSimilar(
        4,
        [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],
        ["ATL", "PEK", "LAX", "DXB"],
        ["ABC", "DEF", "GHI", "JKL", "MNO"]
    )
    assert len(result) == 5

    # Simple case
    result = sol.mostSimilar(
        2,
        [[0, 1]],
        ["A", "B"],
        ["A", "B"]
    )
    assert result == [0, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
