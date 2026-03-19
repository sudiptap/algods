"""
3367. Maximize Sum of Weights After Edge Removals (Hard)

Pattern: 09_dp_on_trees
- Tree with weighted edges. Remove some edges so each node has degree <= k.
  Maximize sum of remaining edge weights.

Approach:
- Root the tree. For each node, decide which child edges to keep.
- dp[node] returns (keep, skip):
  - keep = max weight sum in subtree if the edge to parent IS kept (node uses 1 degree for parent)
  - skip = max weight sum in subtree if the edge to parent is NOT kept
- For each node with children, we can keep at most k edges (or k-1 if parent edge kept).
- Greedily pick the children edges with highest gain (benefit of keeping vs skipping).

Complexity:
- Time:  O(n log n) for sorting gains
- Space: O(n)
"""

from typing import List
from collections import defaultdict


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Iterative post-order to avoid recursion limit
        root = 0
        parent = [-1] * (len(edges) + 1)
        order = []
        visited = [False] * (len(edges) + 1)
        stack = [root]
        visited[root] = True
        while stack:
            node = stack.pop()
            order.append(node)
            for nei, w in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = node
                    stack.append(nei)

        n = len(edges) + 1
        # keep[node] = max subtree sum if edge to parent is kept
        # skip[node] = max subtree sum if edge to parent is not kept
        keep = [0] * n
        skip = [0] * n

        for node in reversed(order):
            # Collect children gains
            base_sum = 0  # sum of skip[child] for all children
            gains = []  # gain of keeping edge to child vs skipping

            for nei, w in adj[node]:
                if nei == parent[node]:
                    continue
                base_sum += skip[nei]
                # Gain of keeping edge (node-nei with weight w):
                # keep[nei] + w vs skip[nei]
                gain = keep[nei] + w - skip[nei]
                if gain > 0:
                    gains.append(gain)

            gains.sort(reverse=True)

            # skip[node]: can keep up to k child edges
            skip[node] = base_sum + sum(gains[:k])

            # keep[node]: parent edge uses 1 degree, so keep up to k-1 child edges
            keep[node] = base_sum + sum(gains[:max(0, k - 1)])

        return skip[root]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maximizeSumOfWeights([[0,1,4],[0,2,2],[2,3,12],[2,4,6]], 2) == 22

    # Example 2
    assert sol.maximizeSumOfWeights([[0,1,5],[1,2,10],[0,3,15],[3,4,20],[3,5,5],[0,6,2]], 3) == 57

    print("All tests passed!")


if __name__ == "__main__":
    test()
