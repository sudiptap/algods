"""
894. All Possible Full Binary Trees (Medium)
https://leetcode.com/problems/all-possible-full-binary-trees/

Given an integer n, return a list of all possible full binary trees with n nodes.
Each node has either 0 or 2 children.

Pattern: DP on Trees
Approach:
- A full binary tree has an odd number of nodes. If n is even, return [].
- Memoize on n. For each n, split (n-1) nodes between left and right subtrees.
  Both left and right must be odd (full binary tree requirement).
- Left gets i nodes, right gets (n-1-i) for i = 1, 3, 5, ...
- Recursively build all left and right subtrees and combine.

Time:  O(2^(n/2)) — Catalan-number-like growth.
Space: O(n * 2^(n/2)) — for memoization of all trees.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """Return all possible full binary trees with n nodes.

        Args:
            n: Number of nodes, 1 <= n <= 20.

        Returns:
            List of root nodes of all possible full binary trees.
        """
        memo = {}

        def build(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return [TreeNode(0)]
            if n % 2 == 0:
                return []

            result = []
            for left_count in range(1, n, 2):
                right_count = n - 1 - left_count
                for left in build(left_count):
                    for right in build(right_count):
                        root = TreeNode(0, left, right)
                        result.append(root)

            memo[n] = result
            return result

        return build(n)


def count_nodes(root):
    """Count nodes in a binary tree."""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_full(root):
    """Check if binary tree is full (every node has 0 or 2 children)."""
    if not root:
        return True
    if (root.left is None) != (root.right is None):
        return False
    return is_full(root.left) and is_full(root.right)


# ---------- tests ----------
def test_all_possible_fbt():
    sol = Solution()

    # n=1: single node
    trees = sol.allPossibleFBT(1)
    assert len(trees) == 1
    assert count_nodes(trees[0]) == 1

    # n=2: impossible (even)
    assert sol.allPossibleFBT(2) == []

    # n=3: only one tree (root + 2 leaves)
    trees = sol.allPossibleFBT(3)
    assert len(trees) == 1
    assert all(is_full(t) and count_nodes(t) == 3 for t in trees)

    # n=7: 5 different full binary trees
    trees = sol.allPossibleFBT(7)
    assert len(trees) == 5
    assert all(is_full(t) and count_nodes(t) == 7 for t in trees)

    # n=5: 2 trees
    trees = sol.allPossibleFBT(5)
    assert len(trees) == 2
    assert all(is_full(t) and count_nodes(t) == 5 for t in trees)

    # n=4: even, impossible
    assert sol.allPossibleFBT(4) == []

    print("All tests passed for 894. All Possible Full Binary Trees")


if __name__ == "__main__":
    test_all_possible_fbt()
