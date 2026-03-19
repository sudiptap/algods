"""
847. Shortest Path Visiting All Nodes (Hard)
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

Given an undirected, connected graph of n nodes (0-indexed), return the length
of the shortest path that visits every node. You may start and stop at any node,
revisit nodes, and reuse edges.

Pattern: Bitmask DP / BFS
Approach:
- State: (current_node, visited_mask) where visited_mask is a bitmask of visited nodes.
- BFS from all nodes simultaneously: enqueue (node, 1 << node) for each node.
- First time we reach a state where visited_mask == (1 << n) - 1, return distance.
- Use a set to avoid revisiting the same (node, mask) state.

Time:  O(2^n * n)  — at most 2^n * n states, each processed once.
Space: O(2^n * n)  — for the visited set and queue.
"""

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """Return length of shortest path visiting all nodes.

        Args:
            graph: Adjacency list of an undirected graph, 1 <= n <= 12.

        Returns:
            Minimum number of edges in a path visiting every node.
        """
        n = len(graph)
        if n == 1:
            return 0

        full = (1 << n) - 1
        queue = deque()
        visited = set()

        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))

        while queue:
            node, mask, dist = queue.popleft()
            for nei in graph[node]:
                new_mask = mask | (1 << nei)
                if new_mask == full:
                    return dist + 1
                if (nei, new_mask) not in visited:
                    visited.add((nei, new_mask))
                    queue.append((nei, new_mask, dist + 1))

        return -1  # unreachable for connected graph


# ---------- tests ----------
def test_shortest_path_visiting_all_nodes():
    sol = Solution()

    # Example 1: complete graph on 4 nodes -> 4
    assert sol.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4

    # Example 2: path graph 0-1-2-3 -> 4 (but also 0-1-2-3 visits all)
    assert sol.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4

    # Single node
    assert sol.shortestPathLength([[]]) == 0

    # Two nodes connected
    assert sol.shortestPathLength([[1], [0]]) == 1

    # Path: 0-1-2 -> need 2 edges
    assert sol.shortestPathLength([[1], [0, 2], [1]]) == 2

    # Star: 0 connected to 1,2,3 -> need to go 0->1, 1->0, 0->2, 2->0, 0->3 = 6? No.
    # Actually 1->0->2->0->3 = 4 edges
    assert sol.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4

    print("All tests passed for 847. Shortest Path Visiting All Nodes")


if __name__ == "__main__":
    test_shortest_path_visiting_all_nodes()
