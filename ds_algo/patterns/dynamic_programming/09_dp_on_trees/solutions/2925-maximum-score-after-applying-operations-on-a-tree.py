"""
2925. Maximum Score After Applying Operations on a Tree
https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

Pattern: 09 - DP on Trees (Post-order DP: take/skip)

---
APPROACH: Every root-to-leaf path must have at least one node with its value
kept (not taken). Equivalently, we want to maximize the sum of taken values
while keeping at least one value on every root-to-leaf path.
dp(node) returns min cost to keep the tree valid (min sum of values NOT taken).
Answer = total_sum - min_kept.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(200001)


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]],
                                     values: List[int]) -> int:
        n = len(values)
        if n == 1:
            return 0

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        total = sum(values)

        def dfs(node, parent):
            """Returns min sum that must be kept (not taken) to keep all paths valid."""
            children = [nei for nei in adj[node] if nei != parent]
            if not children:
                # Leaf: must keep its value
                return values[node]

            child_sum = sum(dfs(c, node) for c in children)
            # Either keep this node's value (then children can all be taken)
            # Or don't keep this node, then each child subtree must keep its own min
            return min(values[node], child_sum)

        min_kept = dfs(0, -1)
        return total - min_kept


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumScoreAfterOperations([[0,1],[0,2],[0,3],[2,4],[4,5]], [5,2,5,2,1,1]) == 11
    assert sol.maximumScoreAfterOperations([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]],
                                           [20,10,9,7,2,5,3]) == 39

    print("All tests passed!")
