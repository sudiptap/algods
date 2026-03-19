"""
2646. Minimize the Total Price of the Trips
https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

Pattern: 09 - DP on Trees (DFS path counting + House Robber on tree)

---
APPROACH:
1. For each trip, find the path and count how many times each node is visited.
2. Apply house-robber on tree: for each node, either halve its price (can't
   halve parent and child both) or keep it. Use post-order DP.

Time: O(trips * n + n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int],
                          trips: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Count how many times each node appears on trip paths
        count = [0] * n

        def dfs_path(node, parent, target, path):
            path.append(node)
            if node == target:
                for p in path:
                    count[p] += 1
                path.pop()
                return True
            for nei in adj[node]:
                if nei != parent:
                    if dfs_path(nei, node, target, path):
                        path.pop()
                        return True
            path.pop()
            return False

        for s, t in trips:
            dfs_path(s, -1, t, [])

        # House robber on tree: dp returns (full_price, halved_price)
        def dp(node, parent):
            full = price[node] * count[node]
            half = full // 2
            for nei in adj[node]:
                if nei != parent:
                    f, h = dp(nei, node)
                    full += min(f, h)  # if current not halved, children can be either
                    half += f  # if current halved, children must be full
            return full, half

        f, h = dp(0, -1)
        return min(f, h)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumTotalPrice(4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]]) == 23
    assert sol.minimumTotalPrice(2, [[0,1]], [2,2], [[0,0]]) == 1

    print("All tests passed!")
