"""
2378. Choose Edges to Maximize Score in a Tree
https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

Pattern: 09 - DP on Trees

---
APPROACH: Post-order DFS
- dp[node] = (with_parent_edge, without_parent_edge)
- with_parent_edge: max score if we include the edge from node to its parent
- without_parent_edge: max score if we don't include that edge
- For each node, sum up children's "without" values (base). Then optionally
  pick the best child to include its "with" value minus its "without" value.
- No two adjacent edges can be selected (at most one edge incident to each node
  from children, and at most one to parent). Wait - re-reading: "no two chosen
  edges are adjacent" means they don't share an endpoint.
  So at each node, at most one of its incident edges can be chosen.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        n = len(edges)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            parent, weight = edges[i]
            children[parent].append((i, weight))

        # Returns (score_if_parent_edge_used, score_if_parent_edge_not_used)
        # "parent_edge_used" means the edge from this node to its parent is chosen,
        # which means no child edge of this node can be chosen.
        def dfs(node):
            base = 0  # sum of children's best scores when their edges to us are NOT used
            best_gain = 0  # best gain from choosing one child edge

            for child, weight in children[node]:
                with_edge, without_edge = dfs(child)
                base += without_edge
                # Gain from choosing this child's edge = weight + with_edge - without_edge... no
                # If we choose edge (node, child), then child cannot use any of its child edges
                # Wait, "with_edge" means child's edge to US is used. That means at child,
                # no other edge is used. And "without_edge" means child can use one of its
                # child edges.
                # Actually let me re-think:
                # For child c with edge weight w to node:
                #   If we use edge (node, c): score += w, and c cannot use any of its edges
                #     -> c contributes: w + (sum of grandchildren's without_edge)
                #   If we don't use edge (node, c): c can optionally use one of its child edges
                #     -> c contributes: without_edge
                # with_edge for child = sum of grandchildren's without_edge (no edge used at child)
                # gain = w + with_edge - without_edge
                gain = weight + with_edge - without_edge
                best_gain = max(best_gain, gain)

            # If parent edge is used, node can't use any child edge
            with_parent = base
            # If parent edge is not used, node can optionally use one child edge
            without_parent = base + best_gain

            return with_parent, without_parent

        _, ans = dfs(0)
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Tree: 0-1 (w=1), 0-2 (w=2), 2-3 (w=1), 2-4 (w=3), 2-5 (w=6)
    # edges[i] = [parent, weight], edges[0] = [-1, -1]
    assert sol.maxScore([[-1,-1],[0,5],[0,10],[2,6],[2,4]]) == 11

    # Simple: root with one child
    assert sol.maxScore([[-1,-1],[0,5]]) == 5

    print("all tests passed")
