"""
834. Sum of Distances in Tree
https://leetcode.com/problems/sum-of-distances-in-tree/

Pattern: 09 - DP on Trees (Rerooting)

---
APPROACH: Rerooting DP with two DFS passes
- First DFS (post-order): compute subtree sizes count[node] and
  dist[0] = sum of distances from root 0 to all other nodes.
- Second DFS (pre-order): for each node, derive dist[node] from
  dist[parent].
  When moving root from parent to child:
  - All nodes in child's subtree get 1 closer: -count[child]
  - All other nodes get 1 farther: +(n - count[child])
  - dist[child] = dist[parent] - count[child] + (n - count[child])
                 = dist[parent] + n - 2*count[child]

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n  # subtree sizes
        dist = [0] * n

        # DFS 1: compute count[] and dist[0] (iterative)
        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            node = stack.pop()
            order.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = node
                    stack.append(nei)

        # Process in reverse order (post-order)
        for node in reversed(order):
            for nei in graph[node]:
                if nei != parent[node]:
                    count[node] += count[nei]
                    dist[node] += dist[nei] + count[nei]

        # dist[0] is now correct. Propagate using rerooting.
        # DFS 2: process in BFS order
        for node in order:
            if parent[node] != -1:
                dist[node] = dist[parent[node]] + n - 2 * count[node]

        return dist


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]) == [8,12,6,10,10,10]
    assert sol.sumOfDistancesInTree(1, []) == [0]
    assert sol.sumOfDistancesInTree(2, [[1,0]]) == [1, 1]
    assert sol.sumOfDistancesInTree(3, [[0,1],[1,2]]) == [3, 2, 3]

    print("all tests passed")
