"""
2247. Maximum Cost of Trip With K Highways
https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

Pattern: 11 - Bitmask DP

---
APPROACH: dp[mask][node] = max cost visiting nodes in mask ending at node
- mask is a bitmask of visited cities, node is the current city.
- Transition: for each neighbor v of node not in mask,
  dp[mask | (1<<v)][v] = max(dp[mask | (1<<v)][v], dp[mask][node] + cost(node,v))
- Start: dp[1<<i][i] = 0 for all i
- Answer: max over all dp[mask][node] where popcount(mask) == k+1

Time: O(2^n * n^2)  Space: O(2^n * n)
---
"""

from typing import List


class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in highways:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # dp[mask][node]
        dp = [[-1] * n for _ in range(1 << n)]

        # Initialize: start at each node
        for i in range(n):
            dp[1 << i][i] = 0

        ans = -1
        target_bits = k + 1

        for mask in range(1 << n):
            for u in range(n):
                if dp[mask][u] < 0:
                    continue
                if bin(mask).count('1') == target_bits:
                    ans = max(ans, dp[mask][u])
                    continue
                for v, w in adj[u]:
                    if mask & (1 << v):
                        continue
                    nmask = mask | (1 << v)
                    if dp[nmask][v] < dp[mask][u] + w:
                        dp[nmask][v] = dp[mask][u] + w

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumCost(5, [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], 3) == 17
    assert sol.maximumCost(4, [[0,1,3],[2,3,2]], 2) == -1
    assert sol.maximumCost(2, [[0,1,5]], 1) == 5
    assert sol.maximumCost(3, [[0,1,2],[1,2,3]], 2) == 5

    print("all tests passed")
