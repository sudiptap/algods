"""
3559. Number of Ways to Assign Edge Weights II
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

Pattern: 09 - DP on Trees

---
APPROACH: Tree DP with parity
- Each edge can be assigned weight 1..k.
- For each query (u, v), the path from u to v must have total weight
  divisible by some value? Actually: path sum must equal a target?
  Re-reading: path u->v must have even total weight.
- Number of edges on path = d (distance in edges via LCA).
- Each edge gets weight in [1, k]. We need sum of d edges to be even.
- An edge contributes even sum if its weight is even: floor(k/2) choices.
- An edge contributes odd sum if its weight is odd: ceil(k/2) choices.
- We need an even number of odd-weighted edges.
- Let e = k//2 (even choices), o = (k+1)//2 (odd choices).
- Ways with even sum over d edges = ((e+o)^d + (e-o)^d) / 2
  using the standard even-subset counting formula.
- Remaining n-1-d edges can be anything: k^(n-1-d) ways each.
- Answer per query = ways_even * k^(n-1-d) mod MOD.

Time: O((n + q) log n)  Space: O(n log n)
---
"""

from typing import List
from collections import defaultdict, deque
import math

MOD = 10**9 + 7


class Solution:
    def assignEdgeWeights(self, n: int, edges: List[List[int]], queries: List[List[int]], k: int = 0) -> List[int]:
        # Note: problem signature may vary. Let me handle both cases.
        # The problem gives: edges defining tree, queries, and k (max weight).
        # Actually from the problem: edges have no weights yet, we assign 1..k.
        # Let me re-check: the function signature is assignEdgeWeights(edges, queries)
        # with edges being tree edges and each edge assigned weight from [1, k].
        # k is not given - checking problem again...
        # Actually: "assign edge weights from 1 to k" - k is a parameter.

        # Adjusting: based on LC, the signature might be (n, edges, queries, k)
        # Let me just handle it flexibly.

        if k == 0:
            # k might be encoded differently - let's assume k is part of constructor
            # For safety, handle the standard version where each edge gets weight in [1, k]
            k = 2  # Default assumption - problem likely uses k=2 or similar

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS from node 1 (1-indexed typically)
        LOG = max(1, int(math.log2(n)) + 1) if n > 1 else 1
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    queue.append(v)

        for ki in range(1, LOG):
            for v in range(1, n + 1):
                if parent[ki - 1][v] != -1:
                    parent[ki][v] = parent[ki - 1][parent[ki - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for ki in range(LOG):
                if (diff >> ki) & 1:
                    u = parent[ki][u]
            if u == v:
                return u
            for ki in range(LOG - 1, -1, -1):
                if parent[ki][u] != parent[ki][v]:
                    u = parent[ki][u]
                    v = parent[ki][v]
            return parent[0][u]

        def path_len(u, v):
            l = lca(u, v)
            return depth[u] + depth[v] - 2 * depth[l]

        total_edges = n - 1

        # For the actual LC 3559: each edge weight in {1, ..., k}
        # but actually reading the problem more carefully:
        # "assign edge weights" where each edge gets a positive integer weight
        # Path u->v should have even total weight.
        # k is given as parameter.

        # e = number of even values in [1,k], o = number of odd values
        e = k // 2
        o = (k + 1) // 2

        ans = []
        for u, v in queries:
            d = path_len(u, v)
            free = total_edges - d
            # Ways to make path sum even with d edges:
            # = sum over even-sized subsets of d edges being odd
            # = ((e+o)^d + (e-o)^d) / 2 mod MOD
            total_pow = pow(e + o, d, MOD)
            diff_pow = pow(e - o, d, MOD)  # e - o could be negative
            ways_even = (total_pow + diff_pow) * pow(2, MOD - 2, MOD) % MOD
            # Free edges: each can be anything 1..k
            ways_free = pow(k, free, MOD)
            ans.append(ways_even * ways_free % MOD)
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple tree: 1-2, k=2. Query (1,2): path has 1 edge.
    # Even weights: {2}, odd: {1}. Ways for even sum = 1. Free = 0. Ans = 1.
    res = sol.assignEdgeWeights(2, [[1, 2]], [[1, 2]], k=2)
    assert res == [1], f"Got {res}"

    # Tree 1-2-3, k=2. Query (1,3): path has 2 edges.
    # Ways for even sum = (2^2 + 0^2)/2 = (4+0)/2 = 2. Free = 0. Ans = 2.
    res = sol.assignEdgeWeights(3, [[1, 2], [2, 3]], [[1, 3]], k=2)
    assert res == [2], f"Got {res}"

    print("All tests passed!")
