"""
2867. Count Valid Paths in a Tree
https://leetcode.com/problems/count-valid-paths-in-a-tree/

Pattern: 09 - DP on Trees (DFS counting paths through prime nodes)

---
APPROACH: A valid path contains exactly one prime node. For each prime node p,
count connected components of non-prime nodes adjacent to p. A path through p
uses nodes from two different components (or just p to one component). Use
Union-Find for non-prime components.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # Sieve of Eratosthenes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Union-Find for non-prime nodes
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]

        # Union non-prime neighbors
        for u, v in edges:
            if not is_prime[u] and not is_prime[v]:
                union(u, v)

        ans = 0
        for p in range(1, n + 1):
            if not is_prime[p]:
                continue
            # For each prime node p, look at connected non-prime components
            component_sizes = []
            for nei in adj[p]:
                if not is_prime[nei]:
                    component_sizes.append(size[find(nei)])

            # Paths: p alone doesn't count (need length >= 1 edge)
            # Path from component to p: sum of sizes
            # Path through p between two components: sum of pairs
            total = 0
            running_sum = 0
            for s in component_sizes:
                ans += s  # paths from this component to p
                ans += running_sum * s  # paths through p between earlier components and this one
                running_sum += s

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countPaths(5, [[1,2],[1,3],[2,4],[2,5]]) == 4
    assert sol.countPaths(6, [[1,2],[1,3],[2,4],[3,5],[3,6]]) == 6

    print("All tests passed!")
