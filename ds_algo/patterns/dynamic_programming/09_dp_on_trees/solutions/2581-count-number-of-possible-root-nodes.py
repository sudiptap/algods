"""
2581. Count Number of Possible Root Nodes
https://leetcode.com/problems/count-number-of-possible-root-nodes/

Pattern: 09 - DP on Trees

---
APPROACH: Rerooting DP counting nodes matching guesses
- Root at node 0. For each guess [u, v] meaning "u is parent of v",
  check if it's correct when rooted at 0.
- Count correct guesses for root=0.
- Rerooting: when we move root from u to v (edge u-v):
  - If guess [u, v] exists: loses 1 correct (u no longer parent of v)
  - If guess [v, u] exists: gains 1 correct (v now parent of u)
- DFS to count for all roots.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        guess_set = set()
        for u, v in guesses:
            guess_set.add((u, v))

        # Root at 0, count correct guesses
        parent = [-1] * n
        order = []
        visited = [False] * n
        stack = [0]
        visited[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)

        correct = 0
        for v in range(1, n):
            if (parent[v], v) in guess_set:
                correct += 1

        # Rerooting DFS
        ans = 0
        count = [0] * n
        count[0] = correct

        if count[0] >= k:
            ans += 1

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                # Reroot from u to v
                count[v] = count[u]
                if (u, v) in guess_set:
                    count[v] -= 1  # u is no longer parent of v
                if (v, u) in guess_set:
                    count[v] += 1  # v is now parent of u
                if count[v] >= k:
                    ans += 1

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.rootCount([[0,1],[1,2],[1,3],[4,2]], [[1,3],[0,1],[1,0],[2,4]], 3) == 3
    assert sol.rootCount([[0,1],[1,2],[2,3],[3,4]], [[1,0],[3,4],[2,1],[3,2]], 1) == 5

    print("all tests passed")
