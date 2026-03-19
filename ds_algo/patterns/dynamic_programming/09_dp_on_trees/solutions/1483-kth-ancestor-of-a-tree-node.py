"""
1483. Kth Ancestor of a Tree Node (Hard)
https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

Problem:
    Implement a class to efficiently find the k-th ancestor of any node
    in a tree with n nodes rooted at node 0.

Pattern: 09 - DP on Trees

Approach:
    1. Binary lifting: precompute up[node][j] = 2^j-th ancestor of node.
    2. up[node][0] = parent[node].
    3. up[node][j] = up[up[node][j-1]][j-1] (2^j = 2^(j-1) + 2^(j-1)).
    4. To find k-th ancestor, decompose k in binary and jump accordingly.

Complexity:
    Time:  O(n log n) preprocessing, O(log k) per query
    Space: O(n log n) for the binary lifting table
"""

from typing import List
import math


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.LOG = max(1, math.ceil(math.log2(n + 1)))
        self.up = [[-1] * (self.LOG + 1) for _ in range(n)]

        for i in range(n):
            self.up[i][0] = parent[i]

        for j in range(1, self.LOG + 1):
            for i in range(n):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG + 1):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node


# ---------- tests ----------
def run_tests():
    # Test 1: tree from problem
    ta = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    assert ta.getKthAncestor(3, 1) == 1, "Test 1a failed"
    assert ta.getKthAncestor(5, 2) == 0, "Test 1b failed"
    assert ta.getKthAncestor(6, 3) == -1, "Test 1c failed"

    # Test 2: root node
    assert ta.getKthAncestor(0, 1) == -1, "Test 2 failed"

    # Test 3: k=0 returns self
    assert ta.getKthAncestor(3, 0) == 3, "Test 3 failed"

    # Test 4: linear chain
    ta2 = TreeAncestor(5, [-1, 0, 1, 2, 3])
    assert ta2.getKthAncestor(4, 4) == 0, "Test 4a failed"
    assert ta2.getKthAncestor(4, 5) == -1, "Test 4b failed"
    assert ta2.getKthAncestor(4, 2) == 2, "Test 4c failed"

    print("All tests passed for 1483. Kth Ancestor of a Tree Node!")


if __name__ == "__main__":
    run_tests()
