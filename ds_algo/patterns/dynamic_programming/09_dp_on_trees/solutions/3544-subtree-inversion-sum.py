"""
3544. Subtree Inversion Sum
https://leetcode.com/problems/subtree-inversion-sum/

Pattern: 09 - DP on Trees

---
APPROACH: Rerooting DP with inversion tracking
- Each node can be "inverted" which negates all values in its subtree (but
  nested inversions cancel). We want to maximize the total sum.
- For each node, decide whether to invert its subtree or not.
- Key constraint: inversions at distance < k from each other conflict.
- dp[node][last_inv_dist] but distance tracking is complex.
- Use tree DP: dp[v][d] = max sum of subtree(v) where d is the distance
  from v to the nearest inverted ancestor (0 means v itself is inverted,
  inf/k means no recent inversion).
- If d >= k, we can choose to invert at v (d becomes 0) or not.
- If d < k, we cannot invert at v, d increments by 1 going to children.

Time: O(n * k)  Space: O(n * k)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(300000)


class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], vals: List[int], k: int) -> int:
        n = len(vals)
        if n == 0:
            return 0

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dp[v][d] = max sum from subtree of v, where d is distance to nearest
        # inverted ancestor. d = k means "no inversion within distance k" (free to invert).
        # d in [0, k]: 0 means parent (or self) was inverted at distance 0 from here.
        # We track d from 1..k where k means "free". 0 means "this node is inverted".
        # Actually let's track: d = distance from nearest inverted ancestor above v.
        # If d >= k, v can choose to invert or not.
        # If v inverts, children see distance 1 from inversion.
        # If v doesn't invert, children see distance d+1 (capped at k).

        INF = float('-inf')

        def dfs(v, parent):
            # Returns dict: d -> max_sum for subtree rooted at v
            # d is the distance from nearest inverted ancestor TO v
            # Result: for each possible d_in (distance from ancestor), return best sum

            child_results = []
            for u in adj[v]:
                if u != parent:
                    child_results.append(dfs(u, v))

            # For a given ancestor distance d_in to v:
            # Option 1: don't invert v. val contribution = vals[v] if even number of
            #   inversions above (tracked by parity). Children see d_in+1 (capped at k).
            # Option 2: invert v (only if d_in >= k). Children see distance 1.

            # Let's simplify: track (distance_to_nearest_inversion, parity_of_inversions)
            # This gets complex. Let me reconsider.

            # Alternative simpler model:
            # dp[v][d] where d = min(distance to nearest inverted ancestor, k)
            # parity is determined by how many inversions are on the path.
            # But we need parity to know the sign of vals[v].

            # Let's track dp[v][(d, parity)] = max sum of subtree
            # d in {0,1,...,k}, parity in {0,1}
            # If d >= k: can invert (parity flips, children get d=1)
            #            or not (children get d=min(d+1,k))
            # If d < k: cannot invert, children get d+1

            # Base: leaf node
            # dp[v][(d,p)] = vals[v] * (1 if p==0 else -1)

            # For internal node, combine children results
            # Each child independently

            # dp[v][(d_in, p_in)]:
            #   sign = 1 if p_in == 0 else -1
            #   Option A (no invert): contribution = vals[v]*sign
            #     for each child c: add dp[c][(min(d_in+1,k), p_in)]
            #   Option B (invert, only if d_in >= k): contribution = vals[v]*(-sign)
            #     for each child c: add dp[c][(1, 1-p_in)]

            result = {}

            for d_in in range(k + 1):
                for p_in in range(2):
                    sign = 1 if p_in == 0 else -1
                    d_child_no = min(d_in + 1, k)

                    # Option A: don't invert
                    val_a = vals[v] * sign
                    for cr in child_results:
                        val_a += cr.get((d_child_no, p_in), INF)

                    best = val_a

                    # Option B: invert (only if d_in >= k)
                    if d_in >= k:
                        val_b = vals[v] * (-sign)
                        for cr in child_results:
                            val_b += cr.get((1, 1 - p_in), INF)
                        best = max(best, val_b)

                    result[(d_in, p_in)] = best

            return result

        res = dfs(0, -1)
        # Root has no inverted ancestor: d=k (free), parity=0
        return res[(k, 0)]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.subtreeInversionSum([[0, 1], [0, 2]], [3, -1, 2], 2) == 6
    # Example 2
    assert sol.subtreeInversionSum([[0, 1], [1, 2], [2, 3], [3, 4]], [1, -2, 3, -4, 5], 2) == 9
    # Example 3
    assert sol.subtreeInversionSum([], [5], 1) == 5

    print("All tests passed!")
