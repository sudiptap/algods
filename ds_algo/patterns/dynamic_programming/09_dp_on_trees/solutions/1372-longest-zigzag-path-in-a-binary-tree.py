"""
1372. Longest ZigZag Path in a Binary Tree (Medium)
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

Problem:
    A ZigZag path alternates between going left and right. Given a binary
    tree, return the length of the longest ZigZag path (number of edges).

Pattern: 09 - DP on Trees

Approach:
    1. DFS returning (left_zigzag, right_zigzag) for each node.
       - left_zigzag = length of longest zigzag starting from this node going left.
       - right_zigzag = similarly going right.
    2. If node has left child, node's left_zigzag = 1 + child's right_zigzag.
    3. If node has right child, node's right_zigzag = 1 + child's left_zigzag.
    4. Track global maximum during traversal.

Complexity:
    Time:  O(n) - visit each node once
    Space: O(h) for recursion stack, h = height of tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            """Returns (left_zigzag_len, right_zigzag_len)."""
            if not node:
                return (-1, -1)

            left_l, left_r = dfs(node.left)
            right_l, right_r = dfs(node.right)

            # Going left from current node then zigzag right
            cur_left = 1 + left_r if node.left else 0
            # Going right from current node then zigzag left
            cur_right = 1 + right_l if node.right else 0

            self.ans = max(self.ans, cur_left, cur_right)
            return (cur_left, cur_right)

        dfs(root)
        return self.ans


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: [1,null,1,1,1,null,null,1,1,null,1] -> 3
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.left = TreeNode(1)
    root.right.right.right = TreeNode(1)
    root.right.right.left.right = TreeNode(1)
    assert sol.longestZigZag(root) == 3, f"Test 1 failed: {sol.longestZigZag(root)}"

    # Test 2: single node
    assert sol.longestZigZag(TreeNode(1)) == 0, "Test 2 failed"

    # Test 3: straight line left
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert sol.longestZigZag(root) == 1, f"Test 3 failed: {sol.longestZigZag(root)}"

    # Test 4: perfect zigzag left-right-left
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(4)
    assert sol.longestZigZag(root) == 3, f"Test 4 failed: {sol.longestZigZag(root)}"

    # Test 5: None
    assert sol.longestZigZag(None) == 0, "Test 5 failed"

    print("All tests passed for 1372. Longest ZigZag Path in a Binary Tree!")


if __name__ == "__main__":
    run_tests()
