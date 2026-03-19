"""
2538. Difference Between Maximum and Min Price Sum
https://leetcode.com/problems/difference-between-maximum-and-min-price-sum/

Pattern: 09 - DP on Trees

---
APPROACH: Rerooting DP tracking max path sum
- For any root, the max cost path starts at root and extends to some leaf.
  The min cost path is just the root itself (single node, cost = price[root]).
- So answer = max over all nodes of (max_path_from_node - price[node])
  = max over all nodes of (max_path_from_node_excluding_endpoint... no).
- Actually: max_path_from_node = price[node] + max sum of a path going down.
  Difference = max_path_sum - price[node] only if we remove the far endpoint.
  Wait: the path includes both endpoints. The "cost" is sum of prices.
  For a rooted subtree at r: max cost = max path sum from r to any node.
  Min cost = just price[r] (path of length 0? No, a path has at least one node).
  Actually min cost path from root r is price[r] (the path is just r).
  So diff = max_path - price[r]. But which leaf do we exclude?

  The answer is: for each possible root, the max path to a leaf minus the leaf's
  price is the maximum "inner path sum" (path from root to parent of leaf).

  Better: for each node, find the longest path (by sum) starting from it. The answer
  for that node as root = longest_path - (value of the endpoint if it's a leaf... no).

  Actually re-reading: we want max(maxCost(r) - minCost(r)) over all r.
  maxCost(r) = max sum path from r. minCost(r) = min sum path from r = price[r].
  So answer = max over r of (max_path_sum_from_r - price[r]).

  This equals max over r of (max_path_sum_from_r) - price[r].
  = max over r of (longest path starting at r, minus r's contribution... no, r IS included).
  = max over r of (sum of path from r to farthest node - price[r]).

  Use rerooting to find max path sum from each node efficiently.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # First pass: root at 0, compute max path sum going down (including self)
        # and max path sum excluding the leaf endpoint
        # down_with[u] = max path sum from u going into subtree (including u and leaf)
        # down_without[u] = max path sum from u excluding the leaf at the end

        down_with = [0] * n    # includes leaf
        down_without = [0] * n  # excludes leaf

        # Iterative DFS for tree rooted at 0
        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)

        # Process in reverse order (leaves first)
        for u in reversed(order):
            down_with[u] = price[u]
            down_without[u] = 0
            for v in adj[u]:
                if v == parent[u]:
                    continue
                if down_with[v] + price[u] > down_with[u]:
                    down_with[u] = down_with[v] + price[u]
                if down_without[v] + price[u] > down_without[u]:
                    down_without[u] = down_without[v] + price[u]

        # Second pass: rerooting
        # up_with[u] = max path sum going up from u (through parent) including far endpoint
        # up_without[u] = same but excluding far endpoint
        up_with = [0] * n
        up_without = [0] * n

        # For rerooting, we need top-2 children values for each node
        # to handle the case where the best child is the one we're rerooting to
        # Store top-2 down_with and down_without for each node's children
        top2_with = [[] for _ in range(n)]  # list of (value, child_index)
        top2_without = [[] for _ in range(n)]

        for u in order:
            children_with = []
            children_without = []
            for v in adj[u]:
                if v == parent[u]:
                    continue
                children_with.append((down_with[v], v))
                children_without.append((down_without[v], v))
            children_with.sort(reverse=True)
            children_without.sort(reverse=True)
            top2_with[u] = children_with[:2]
            top2_without[u] = children_without[:2]

        ans = 0

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                # Compute up_with[v] and up_without[v]
                # Path goes from v -> u -> (up from u or down into another subtree of u)
                # Best "with leaf" from u excluding subtree v:
                best_down_with = 0
                for val, child in top2_with[u]:
                    if child != v:
                        best_down_with = val
                        break

                best_down_without = 0
                for val, child in top2_without[u]:
                    if child != v:
                        best_down_without = val
                        break

                # up_with[v] = price[u] + max(up_with[u], best_down_with)
                up_with[v] = price[u] + max(up_with[u], best_down_with)
                # up_without[v] = price[u] + max(up_without[u], best_down_without)
                up_without[v] = price[u] + max(up_without[u], best_down_without)

            # Now compute answer for node u
            # max path from u = max(down_with[u], up_with[u] + price[u])...
            # Wait, down_with[u] already includes price[u].
            # up_with[u] is the max path going up from u through parent, NOT including u.
            # So total path with leaf = max(down_with[u], up_with[u] + price[u])
            # And path without leaf = max(down_without[u], up_without[u] + price[u])
            # But we want max_path - price[u] = max path excluding one endpoint.
            #
            # Actually: for node u, the longest path from u includes u.
            # diff = longest_path_from_u - price[u]
            # This is the same as removing u from the path... no, we remove the leaf.
            # Hmm, the diff = max_cost_path - min_cost_path = max_path - price[u].
            # max_path includes both endpoints (u and the far node).
            # We want max_path - price[u]. But that's just the max path WITHOUT u.
            # No: max_path = price[u] + ... + price[leaf]. Minus price[u] = path minus root.
            #
            # So the answer for u = max(down_with[u], up_with[u] + price[u]) - price[u]
            # = max(down_with[u] - price[u], up_with[u])

            # But we also should consider: the max path could exclude the endpoint on
            # the other end, giving us max_path - price[far_endpoint].
            # This means for node u: max(path_including_leaf - price[u],
            #                              path_excluding_leaf)
            # = max(path_with - price[u], path_without)

            best_with = max(down_with[u], up_with[u] + price[u])
            best_without = max(down_without[u], up_without[u] + price[u])

            # diff can be: best_with - price[u] (min path = just u, subtract leaf on far end... no)
            # Actually the problem: minCost path from u = price[u] (just the node).
            # maxCost path from u = best_with (longest path including leaf).
            # answer for u = best_with - price[u].
            # But we can also interpret: the path is from u to some node v.
            # maxCost = sum of all prices on path.
            # minCost = min cost path = just price[u] (path of length 1).
            # So diff = maxCost - minCost = best_with - price[u].

            # However, there's another interpretation: remove one endpoint from the max path.
            # The max path with leaf removed = best_without. And best_without might be
            # larger than best_with - price[u] if the leaf has a high price.
            # So answer = max(best_with - price[u], best_without)
            # Wait no, best_without excludes the far endpoint, not u. So:
            # best_without = path from u to parent_of_leaf = best_with - price[leaf].
            # And best_with - price[u] = path from child_of_u to leaf.
            # We want max(best_with - price[u]) over all u (the "remove root" interpretation).
            # But that equals best_without when looking from the leaf's perspective.
            #
            # Let me simplify: answer = max over all u of (max_downward_path_from_u_without_leaf)
            # which = down_without[u] or up-path without endpoint.
            # OR: max over all u of (best_with - price[u]).

            ans = max(ans, best_with - price[u])

            # Also consider: removing the far leaf from the path
            # This equals best_without (for paths going down) or up_without + price[u]
            ans = max(ans, best_without)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxOutput(6, [[0,1],[1,2],[1,3],[3,4],[3,5]], [9,8,7,6,10,5]) == 24
    assert sol.maxOutput(3, [[0,1],[1,2]], [1,1,1]) == 2
    assert sol.maxOutput(1, [], [5]) == 0

    print("all tests passed")
