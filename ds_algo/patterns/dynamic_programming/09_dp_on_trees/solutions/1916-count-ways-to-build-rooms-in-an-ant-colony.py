"""
1916. Count Ways to Build Rooms in an Ant Colony (Hard)
https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

Given a tree rooted at 0 with prevRoom[i] = parent of room i, count
the number of valid build orders (topological orderings) mod 10^9+7.

Pattern: DP on Trees
Approach:
- For a rooted tree, the number of valid topological orderings is:
  n! / product(subtree_size[v] for all v)
- Compute subtree sizes via DFS.
- Use modular arithmetic with precomputed factorials and inverse factorials.

Time:  O(n)
Space: O(n)
"""

from typing import List
import sys


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        """Return number of valid room build orders mod 10^9+7.

        Args:
            prevRoom: Parent array where prevRoom[i] is parent of room i.

        Returns:
            Count of valid build orders mod 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(prevRoom)

        # Build adjacency list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[prevRoom[i]].append(i)

        # Compute subtree sizes iteratively (avoid recursion limit)
        subtree_size = [1] * n
        order = []
        stack = [0]
        visited = [False] * n
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            order.append(node)
            for c in children[node]:
                stack.append(c)

        # Process in reverse order (leaves first)
        for node in reversed(order):
            for c in children[node]:
                subtree_size[node] += subtree_size[c]

        # Precompute factorials and inverse factorials
        max_n = n + 1
        fact = [1] * max_n
        for i in range(1, max_n):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * max_n
        inv_fact[max_n - 1] = pow(fact[max_n - 1], MOD - 2, MOD)
        for i in range(max_n - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        # Result = n! / product(subtree_size[v])
        result = fact[n]
        for v in range(n):
            result = result * inv_fact[subtree_size[v]] % MOD

        return result


# ---------- tests ----------
def test_ways_to_build_rooms():
    sol = Solution()

    # Example 1: [-1,0,1] -> only one order: 0,1,2
    assert sol.waysToBuildRooms([-1, 0, 1]) == 1

    # Example 2: [-1,0,0,1,2] -> 6 valid orders
    assert sol.waysToBuildRooms([-1, 0, 0, 1, 2]) == 6

    # Single room
    assert sol.waysToBuildRooms([-1]) == 1

    # Star graph: [-1,0,0,0] -> 3! = 6 (any order of 1,2,3 after 0)
    assert sol.waysToBuildRooms([-1, 0, 0, 0]) == 6

    print("All tests passed for 1916. Count Ways to Build Rooms in an Ant Colony")


if __name__ == "__main__":
    test_ways_to_build_rooms()
