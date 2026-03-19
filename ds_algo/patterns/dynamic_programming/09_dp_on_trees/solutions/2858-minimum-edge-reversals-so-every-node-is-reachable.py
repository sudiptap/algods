"""
2858. Minimum Edge Reversals So Every Node Is Reachable
https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

Pattern: 09 - DP on Trees (Rerooting DP)

---
APPROACH: Build tree with directed edges. First DFS from root 0 counts
reversals needed. Second DFS reroots: when moving root from parent to child,
if edge parent->child exists (no reversal), moving root adds 1 reversal;
if edge was child->parent (needed reversal), moving root removes 1.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(300001)


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append((v, 0))  # forward edge, no reversal
            adj[v].append((u, 1))  # reverse edge, needs reversal

        ans = [0] * n

        # First DFS: count reversals from node 0
        def dfs1(node, parent):
            total = 0
            for nei, cost in adj[node]:
                if nei != parent:
                    total += cost + dfs1(nei, node)
            return total

        ans[0] = dfs1(0, -1)

        # Second DFS: reroot
        def dfs2(node, parent):
            for nei, cost in adj[node]:
                if nei != parent:
                    # cost=0 means edge node->nei (forward). Rerooting adds 1.
                    # cost=1 means edge nei->node (reverse). Rerooting removes 1.
                    ans[nei] = ans[node] + (1 if cost == 0 else -1)
                    dfs2(nei, node)

        dfs2(0, -1)
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minEdgeReversals(4, [[2,0],[2,1],[1,3]]) == [1, 1, 0, 2]

    print("All tests passed!")
