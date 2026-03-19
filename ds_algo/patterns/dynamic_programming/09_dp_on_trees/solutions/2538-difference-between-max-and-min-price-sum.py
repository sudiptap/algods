"""
2538. Difference Between Maximum and Min Price Sum
https://leetcode.com/problems/difference-between-maximum-and-min-price-sum/

Pattern: 09 - DP on Trees

---
APPROACH: Rerooting DP
- For each node as root, maxCost = max path sum from root to any node in subtree.
  minCost = price[root] (just the root itself).
- So answer = max over all roots r of (maxPathSum(r) - price[r]).
- This equals: find the longest path (by price sum) in the tree, then the answer
  is that path's total sum minus the minimum endpoint price.
- Equivalently: for every path in the tree, the score = sum - min(endpoint1, endpoint2).
- Implementation: for each node, track the two longest downward paths. The best path
  through a node = longest + second_longest + price[node]. For the answer, subtract
  the leaf price from one end.

Simpler approach: DFS computing for each node:
  - max path sum WITH leaf (path from node to some descendant, all nodes included)
  - max path sum WITHOUT leaf (same path but exclude the leaf at the end)
- The answer for node as root = max(down_without[child] + price[node]) over children,
  meaning the longest path from root but without the far leaf.

Time: O(n)  Space: O(n)
---
"""

from typing import List
import sys
sys.setrecursionlimit(300000)


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0

        def dfs(u, parent):
            """Returns (with_leaf, without_leaf) for paths starting at u going down.
            with_leaf = max path sum from u to some descendant (includes all nodes)
            without_leaf = same but exclude the leaf endpoint"""
            nonlocal ans

            with_leaf = price[u]  # just u itself (u is a leaf)
            without_leaf = 0       # path of just u, but excluding the leaf (u) = 0

            for v in adj[u]:
                if v == parent:
                    continue
                child_with, child_without = dfs(v, u)

                # Combine: path through u using one child's path and current best from another
                # The "answer" for paths through u:
                # Option 1: one side has leaf removed: with_leaf (old) + child_without + price[u]?
                # No. Let me think again.
                # A path through u uses at most 2 branches. For the answer, we remove
                # one endpoint (leaf) from the path.
                # Score = path_sum - one_leaf_price
                # = (branch1_with_leaf + branch2_with_leaf - price[u]) - min_leaf_of_either_branch
                # = branch1_without + branch2_with - price[u] + price[u]  (if we remove leaf of branch1)
                # Wait, let me be more careful:
                # branch1 contributes: with_leaf1 = price[u->...->leaf1], includes u
                # Actually with_leaf already includes price[u].
                # path sum through u = with_leaf (from one side, includes u) + child_with (other side, includes child but NOT u)
                # Hmm, the child's with_leaf includes child but not u.
                # So: path through u = with_leaf_from_one_branch + child_with_from_other (the child's subtree, not including u) + price[u]?
                # No. with_leaf already includes price[u]. child_with includes price[child] to some leaf.
                # So total path = with_leaf + child_with - price[u]? No that doesn't make sense either.

                # Let me redefine clearly:
                # with_leaf[u] = max sum of a path from u downward to some leaf, including u and the leaf
                # without_leaf[u] = max sum of a path from u downward, including u but NOT the leaf at the end

                # For the answer: considering u as the "bend" point of a path:
                # path uses two branches from u: total = branch_a + branch_b - price[u] (u counted once)
                # To compute diff for this path: total - min(leaf_a, leaf_b)
                # If we remove leaf from branch_a: score = without_leaf_a + child_b_with_leaf
                # Wait: without_leaf from branch_a (which includes u) + child_b's with_leaf
                # But u is counted in without_leaf_a already. So:
                # path without one leaf = without_leaf_a + (child_with from branch_b)
                # where child_with = with_leaf of child - ... no.
                #
                # Let me define:
                # dw[u] = max (path sum from u to descendant, EXCLUDING the leaf) = price[u] + max(dw[child])
                # dl[u] = max (path sum from u to descendant, INCLUDING leaf) = price[u] + max(dl[child])
                # For a leaf node: dl = price[leaf], dw = 0
                #
                # For a path through u using two branches (children c1, c2):
                # Remove leaf from c1's side: score = dw_c1_side + dl_c2_side (both include price[u])
                #   = (price[u] + dw[c1]) + dl[c2]  -- but price[u] counted once, should be:
                #   Nope. dw[u] from c1's direction = price[u] + dw[c1]? Or dw[c1] includes price[c1]...
                #
                # Let me redefine from child perspective:
                # cdl[c] = max path sum from c downward including leaf = dl[c] (includes c)
                # cdw[c] = max path sum from c downward excluding leaf = dw[c] (includes c, excludes far leaf)
                #
                # For path through u using children c1 and c2 (and removing one leaf):
                # Score option A (remove leaf of c1 side):
                #   = cdw[c1] + price[u] + cdl[c2]
                # Score option B (remove leaf of c2 side):
                #   = cdl[c1] + price[u] + cdw[c2]
                #
                # For path using just one child (u is one endpoint, leaf is other):
                # Score = cdw[c] + price[u]  (remove leaf) or cdl[c] (remove u... = cdl[c] - 0 = cdl[c])
                # Wait removing u means score = cdl[c] (the path is u to leaf, remove u endpoint)
                # Actually: diff = path_sum - min_endpoint. If u is endpoint:
                # Score = total_path - price[u] (if price[u] is the min) = cdl[c]
                # Or score = total_path - leaf_price = cdw[c] + price[u]

                # Update answer: combine current best from u's side with new child
                # ans = max(ans, old_with_leaf_from_u * child_without + ...)
                ans = max(ans, with_leaf + child_without)  # remove leaf from child's side
                ans = max(ans, without_leaf + child_with)   # remove leaf from u's current best side

                # Update u's values
                with_leaf = max(with_leaf, child_with + price[u])
                without_leaf = max(without_leaf, child_without + price[u])

            # Also consider u as an endpoint: the path is just u to some descendant
            # Score = with_leaf - price[u] (remove u as leaf) -> this = child_with
            # Or score = without_leaf (remove the descendant leaf)
            # These are already captured above since we track without_leaf

            # Single-branch answer: path from u downward
            # Removing the leaf: without_leaf (already tracked)
            # Removing u: with_leaf - price[u] = max child_with
            ans = max(ans, without_leaf)  # path from u, remove far leaf
            ans = max(ans, with_leaf - price[u])  # path from u, remove u itself

            return with_leaf, without_leaf

        dfs(0, -1)
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxOutput(6, [[0,1],[1,2],[1,3],[3,4],[3,5]], [9,8,7,6,10,5]) == 24
    assert sol.maxOutput(3, [[0,1],[1,2]], [1,1,1]) == 2
    assert sol.maxOutput(1, [], [5]) == 0

    print("all tests passed")
