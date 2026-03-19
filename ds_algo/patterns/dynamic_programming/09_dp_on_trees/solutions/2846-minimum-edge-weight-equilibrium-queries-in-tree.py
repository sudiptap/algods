"""
2846. Minimum Edge Weight Equilibrium Queries in a Tree
https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-tree/

Pattern: 09 - DP on Trees (LCA + frequency counting)

---
APPROACH: For each query (u,v), find path using LCA. Count edge weight
frequencies on the path. Answer = path_length - max_frequency (change all
but the most common weight). Use binary lifting for LCA and prefix frequency
arrays from root to each node.

Time: O((n + q) * W * log n) where W = 26 (max weight)
Space: O(n * W + n * log n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]],
                             queries: List[List[int]]) -> List[int]:
        W = 27  # weights 1..26
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = n.bit_length()
        depth = [0] * n
        parent = [[-1] * n for _ in range(LOG)]
        freq = [[0] * W for _ in range(n)]  # prefix freq from root

        # BFS to set depth, parent, freq
        from collections import deque
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    freq[v] = freq[u][:]
                    freq[v][w] += 1
                    queue.append(v)

        for j in range(1, LOG):
            for i in range(n):
                if parent[j - 1][i] != -1:
                    parent[j][i] = parent[j - 1][parent[j - 1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = parent[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]
            return parent[0][u]

        result = []
        for u, v in queries:
            l = lca(u, v)
            path_len = depth[u] + depth[v] - 2 * depth[l]
            max_freq = 0
            for w in range(1, W):
                cnt = freq[u][w] + freq[v][w] - 2 * freq[l][w]
                max_freq = max(max_freq, cnt)
            result.append(path_len - max_freq)

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperationsQueries(
        7,
        [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]],
        [[0,3],[3,6],[2,6],[0,6]]
    ) == [0, 0, 1, 3]

    assert sol.minOperationsQueries(
        8,
        [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]],
        [[4,6],[0,4],[6,5],[7,4]]
    ) == [1, 2, 2, 3]

    print("All tests passed!")
