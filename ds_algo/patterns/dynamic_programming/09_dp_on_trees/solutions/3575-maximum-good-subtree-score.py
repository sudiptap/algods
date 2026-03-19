"""
3575. Maximum Good Subtree Score
https://leetcode.com/problems/maximum-good-subtree-score/

Pattern: 09 - DP on Trees

---
APPROACH: Bitmask DP on subtree digit sets
- A "good" subtree is one where all node values have distinct digits.
- Track which digits are used via bitmask (10 bits for digits 0-9).
- dp[node][mask] = max sum of values from a subset of subtree nodes,
  where mask represents the set of digits used, and no digit repeats.
- For each node, merge children's DP tables, then optionally include
  the node itself.

Time: O(n * 2^10 * 2^10) worst case, but pruned  Space: O(n * 2^10)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(300000)
MOD = 10**9 + 7


class Solution:
    def maxScore(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def digit_mask(val):
            mask = 0
            if val == 0:
                return 1  # digit 0
            while val > 0:
                d = val % 10
                if mask & (1 << d):
                    return -1  # repeated digit in same number
                mask |= (1 << d)
                val //= 10
            return mask

        masks = [digit_mask(v) for v in values]

        def dfs(v, parent):
            # Returns dict: mask -> max_sum
            # Start with empty selection
            dp = {0: 0}

            # Optionally include this node (if its digits don't repeat internally)
            vm = masks[v]
            if vm != -1:
                dp[vm] = values[v]

            for u in adj[v]:
                if u == parent:
                    continue
                child_dp = dfs(u, v)

                # Merge: for each combo of current dp and child dp where masks don't overlap
                new_dp = {}
                for m1, s1 in dp.items():
                    if m1 not in new_dp or new_dp[m1] < s1:
                        new_dp[m1] = s1
                    for m2, s2 in child_dp.items():
                        if m1 & m2 == 0:
                            combined = m1 | m2
                            total = s1 + s2
                            if combined not in new_dp or new_dp[combined] < total:
                                new_dp[combined] = total
                dp = new_dp

            return dp

        result = dfs(0, -1)
        ans = max(result.values()) if result else 0
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple: single node
    assert sol.maxScore(1, [], [123]) == 123

    # Two nodes, no digit overlap
    res = sol.maxScore(2, [[0, 1]], [12, 34])
    assert res == 46, f"Got {res}"

    # Two nodes with digit overlap
    res = sol.maxScore(2, [[0, 1]], [12, 23])
    assert res == 23, f"Got {res}"  # can't use both, pick max

    print("All tests passed!")
