"""
3772. Maximum Subgraph Score in a Tree
https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

Pattern: 09 - DP on Trees

---
APPROACH: Re-rooting DP
- score(subgraph) = good_nodes - bad_nodes = sum of (2*good[i]-1) for nodes in subgraph.
- Let val[i] = 1 if good[i]==1, else -1.
- For each node, find max-weight connected subgraph containing it.
- First root at 0. For each subtree, compute max sum of connected subgraph
  containing the root: dp[u] = val[u] + sum(max(0, dp[child]) for children).
  (Include a child's subtree only if it adds positive value.)
- Then re-root: when moving root from parent to child, update the contribution
  from the parent's side.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        val = [1 if g == 1 else -1 for g in good]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 1: Root at 0, compute dp_down[u] = max weight connected subgraph
        # rooted at u considering only the subtree of u.
        dp_down = [0] * n
        parent = [-1] * n
        order = []

        # BFS to get order
        from collections import deque
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)

        # Bottom-up
        for u in reversed(order):
            dp_down[u] = val[u]
            for v in adj[u]:
                if parent[v] == u:  # v is child of u
                    dp_down[u] += max(0, dp_down[v])

        # Step 2: Re-root to compute answer for each node.
        # dp_up[u] = max contribution from parent's side (everything except u's subtree).
        # ans[u] = val[u] + sum(max(0, dp_down[child])) + max(0, dp_up[u])
        # dp_up[u] = val[parent] + sum(max(0, dp_down[sibling]) for siblings of u) + max(0, dp_up[parent])
        #          = (dp_down[parent] - max(0, dp_down[u])) + max(0, dp_up[parent])
        #          But dp_down[parent] already includes max(0, dp_down[u]).
        #          So parent_without_u = dp_down[parent] - max(0, dp_down[u])
        #          dp_up[u] = parent_without_u + max(0, dp_up[parent])

        dp_up = [0] * n
        ans = [0] * n
        ans[0] = dp_down[0]

        for u in order:
            for v in adj[u]:
                if parent[v] == u:
                    parent_without_v = dp_down[u] - max(0, dp_down[v])
                    dp_up[v] = parent_without_v + max(0, dp_up[u])
                    ans[v] = dp_down[v] + max(0, dp_up[v])

        # Also update ans[0]
        ans[0] = dp_down[0] + max(0, dp_up[0])

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSubgraphScore(3, [[0, 1], [1, 2]], [1, 0, 1]) == [1, 1, 1]
    assert sol.maxSubgraphScore(5, [[1, 0], [1, 2], [1, 3], [3, 4]], [0, 1, 0, 1, 1]) == [2, 3, 2, 3, 3]
    assert sol.maxSubgraphScore(2, [[0, 1]], [0, 0]) == [-1, -1]

    print("all tests passed")
