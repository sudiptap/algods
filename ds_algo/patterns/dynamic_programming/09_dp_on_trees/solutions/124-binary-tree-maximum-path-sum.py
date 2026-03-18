"""
124. Binary Tree Maximum Path Sum (Hard)
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem:
    A path in a binary tree is a sequence of nodes where each pair of adjacent
    nodes has an edge connecting them. A node can only appear in the path at
    most once. The path does not need to pass through the root.

    The path sum is the sum of the node values in the path.

    Given the root of a binary tree, return the maximum path sum of any
    non-empty path.

Pattern: 09 - DP on Trees

Approach:
    Post-order DFS. At each node we compute the maximum gain we can contribute
    to a path that goes *through* a parent (single branch only). Meanwhile we
    update a global maximum considering the path that *spans* through this node
    using both left and right branches.

    For each node:
        left_gain  = max(dfs(left), 0)   # drop negative branches
        right_gain = max(dfs(right), 0)
        current_path_sum = node.val + left_gain + right_gain  -> update global max
        return node.val + max(left_gain, right_gain)           -> report to parent

Complexity:
    Time:  O(n) - visit every node once
    Space: O(h) - recursion stack, h = height of tree
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path that passes through this node using both branches
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)

            # Return max gain if we continue through one branch only
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum


# ---------- helpers ----------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None = null node)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: [1,2,3] -> 6  (path 2->1->3)
    root = build_tree([1, 2, 3])
    assert sol.maxPathSum(root) == 6, f"Test 1 failed: got {sol.maxPathSum(root)}"

    # Test 2: [-10,9,20,None,None,15,7] -> 42  (path 15->20->7)
    root = build_tree([-10, 9, 20, None, None, 15, 7])
    assert sol.maxPathSum(root) == 42, f"Test 2 failed: got {sol.maxPathSum(root)}"

    # Test 3: single node [-3] -> -3
    root = build_tree([-3])
    assert sol.maxPathSum(root) == -3, f"Test 3 failed: got {sol.maxPathSum(root)}"

    # Test 4: all negative [-1,-2,-3] -> -1
    root = build_tree([-1, -2, -3])
    assert sol.maxPathSum(root) == -1, f"Test 4 failed: got {sol.maxPathSum(root)}"

    # Test 5: single node [5] -> 5
    root = build_tree([5])
    assert sol.maxPathSum(root) == 5, f"Test 5 failed: got {sol.maxPathSum(root)}"

    # Test 6: left-skewed [2,1,None] -> 3
    root = TreeNode(2, TreeNode(1))
    assert sol.maxPathSum(root) == 3, f"Test 6 failed: got {sol.maxPathSum(root)}"

    print("All tests passed for 124. Binary Tree Maximum Path Sum!")


if __name__ == "__main__":
    run_tests()
