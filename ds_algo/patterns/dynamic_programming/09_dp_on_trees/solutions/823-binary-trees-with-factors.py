"""
823. Binary Trees With Factors
https://leetcode.com/problems/binary-trees-with-factors/

Pattern: 09 - DP on Trees

---
APPROACH: Sort and for each root, try all factor pairs as children
- Sort the array. For each value v as root, try all pairs (a, b)
  where a * b = v and both a, b are in the array.
- dp[v] = 1 (just the node) + sum(dp[a] * dp[b]) for all valid pairs.
- For each v, iterate over elements a < v and check if v/a is also in set.
- If a != v/a, multiply by 2 (left/right swap).

Time: O(n^2)  Space: O(n)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        val_set = set(arr)
        dp = {}

        for v in arr:
            dp[v] = 1  # just the leaf
            for a in arr:
                if a >= v:
                    break
                if v % a == 0:
                    b = v // a
                    if b in val_set:
                        dp[v] = (dp[v] + dp[a] * dp[b]) % MOD

        return sum(dp.values()) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numFactoredBinaryTrees([2, 4]) == 3
    # Trees: [2], [4], [4 with children 2,2]
    assert sol.numFactoredBinaryTrees([2, 4, 5, 10]) == 7
    assert sol.numFactoredBinaryTrees([2]) == 1
    assert sol.numFactoredBinaryTrees([2, 4, 8, 16]) == 23

    print("all tests passed")
