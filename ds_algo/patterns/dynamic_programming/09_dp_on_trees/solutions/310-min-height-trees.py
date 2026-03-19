"""
310. Minimum Height Trees (Medium)
https://leetcode.com/problems/minimum-height-trees/

Pattern: DP on Trees / BFS Leaf Trimming

Given a tree of n nodes labeled 0 to n-1, find all root labels that
minimize the height of the tree (MHTs).

Approach:
    BFS leaf trimming (topological sort style).
    Repeatedly remove all current leaves. The last 1 or 2 remaining
    nodes are the roots of MHTs — they are the "center" of the tree.

    Why it works: the center of the longest path is always an MHT root,
    and trimming leaves layer by layer converges to the center.

Time:  O(n)
Space: O(n)
"""

from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """Return root labels that produce minimum height trees."""
        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque(i for i in range(n) if len(adj[i]) == 1)
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert sorted(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) == [1]

def test_example2():
    assert sorted(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) == [3, 4]

def test_single_node():
    assert Solution().findMinHeightTrees(1, []) == [0]

def test_two_nodes():
    assert sorted(Solution().findMinHeightTrees(2, [[0,1]])) == [0, 1]

def test_line_graph():
    # 0-1-2-3-4 -> center is 2
    assert Solution().findMinHeightTrees(5, [[0,1],[1,2],[2,3],[3,4]]) == [2]

def test_line_even():
    # 0-1-2-3 -> center is 1,2
    assert sorted(Solution().findMinHeightTrees(4, [[0,1],[1,2],[2,3]])) == [1, 2]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
