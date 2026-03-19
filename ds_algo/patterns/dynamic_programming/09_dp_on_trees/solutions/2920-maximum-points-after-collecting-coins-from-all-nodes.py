"""
2920. Maximum Points After Collecting Coins From All Nodes
https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

Pattern: 09 - DP on Trees (DFS with state: node, halvings)

---
APPROACH: Two choices at each node:
1. Collect coins[node]/(2^halvings) - k, children get same halvings.
2. Collect floor(coins[node]/(2^(halvings+1))), children get halvings+1.
Since coins <= 10^4, after ~14 halvings everything is 0. Cap halvings at 14.

Time: O(n * 14)  Space: O(n * 14)
---
"""

from typing import List
from collections import defaultdict
from functools import lru_cache
import sys

sys.setrecursionlimit(200001)


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        @lru_cache(maxsize=None)
        def dfs(node, parent, halvings):
            if halvings > 14:
                return 0
            val = coins[node] >> halvings

            # Option 1: collect val - k
            opt1 = val - k
            for nei in adj[node]:
                if nei != parent:
                    opt1 += dfs(nei, node, halvings)

            # Option 2: collect val // 2, children get halvings + 1
            opt2 = val >> 1
            for nei in adj[node]:
                if nei != parent:
                    opt2 += dfs(nei, node, halvings + 1)

            return max(opt1, opt2)

        return dfs(0, -1, 0)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumPoints([[0,1],[1,2],[2,3]], [10,10,3,3], 5) == 11
    assert sol.maximumPoints([[0,1],[0,2]], [8,4,4], 0) == 16

    print("All tests passed!")
