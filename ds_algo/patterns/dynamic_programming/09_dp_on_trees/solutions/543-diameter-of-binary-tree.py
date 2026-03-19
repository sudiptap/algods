"""
543. Diameter of Binary Tree (Easy)
https://leetcode.com/problems/diameter-of-binary-tree/

Pattern: DP on Trees

Given the root of a binary tree, return the length of the diameter —
the longest path between any two nodes (measured in edges).
The path may or may not pass through the root.

Approach:
    DFS returning the depth (longest single-arm path) from each node.
    At each node, the path through it = left_depth + right_depth.
    Update a global maximum with this value.
    Return max(left_depth, right_depth) + 1 to parent.

Time:  O(n)
Space: O(h) where h is tree height (recursion stack)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Return the diameter of the binary tree in edges."""
        self.ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.ans


# ───────────────────────── tests ─────────────────────────

def test_example1():
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert Solution().diameterOfBinaryTree(root) == 3

def test_example2():
    root = TreeNode(1, TreeNode(2))
    assert Solution().diameterOfBinaryTree(root) == 1

def test_single_node():
    assert Solution().diameterOfBinaryTree(TreeNode(1)) == 0

def test_none():
    assert Solution().diameterOfBinaryTree(None) == 0

def test_linear():
    # 1 -> 2 -> 3 -> 4
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert Solution().diameterOfBinaryTree(root) == 3

def test_balanced():
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, None, TreeNode(6)))
    assert Solution().diameterOfBinaryTree(root) == 4


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
