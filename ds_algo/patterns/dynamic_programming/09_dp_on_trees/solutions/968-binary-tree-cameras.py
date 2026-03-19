"""
968. Binary Tree Cameras (Hard)
https://leetcode.com/problems/binary-tree-cameras/

Given a binary tree, install the minimum number of cameras on nodes so that
every node is monitored. A camera monitors its parent, itself, and children.

Pattern: DP on Trees
Approach:
- Post-order DFS with 3 states per node:
  0 = NOT_COVERED: node needs coverage from parent.
  1 = HAS_CAMERA: node has a camera.
  2 = COVERED: node is covered (by a child's camera) but has no camera.
- Null nodes return COVERED (they don't need cameras).
- If any child is NOT_COVERED, current node MUST have a camera.
- If any child HAS_CAMERA, current node is COVERED.
- Otherwise, current node is NOT_COVERED (needs parent to cover it).
- After DFS, if root is NOT_COVERED, add one more camera.

Time:  O(n) — visit each node once.
Space: O(h) — recursion stack, h = height.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


NOT_COVERED, HAS_CAMERA, COVERED = 0, 1, 2


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """Return minimum cameras to cover all nodes.

        Args:
            root: Root of binary tree.

        Returns:
            Minimum number of cameras.
        """
        self.cameras = 0

        def dfs(node):
            if not node:
                return COVERED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == NOT_COVERED or right == NOT_COVERED:
                self.cameras += 1
                return HAS_CAMERA

            if left == HAS_CAMERA or right == HAS_CAMERA:
                return COVERED

            return NOT_COVERED

        if dfs(root) == NOT_COVERED:
            self.cameras += 1

        return self.cameras


# ---------- tests ----------
def test_min_camera_cover():
    sol = Solution()

    # Example 1: [0,0,null,0,0] -> 1 camera at node 1 covers all
    root = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))
    assert sol.minCameraCover(root) == 1

    # Example 2: [0,0,null,0,null,0,null,null,0] -> 2 cameras
    root = TreeNode(0,
        TreeNode(0,
            TreeNode(0,
                TreeNode(0, None, TreeNode(0)))))
    assert sol.minCameraCover(root) == 2

    # Single node: needs 1 camera
    assert sol.minCameraCover(TreeNode(0)) == 1

    # Two nodes: 1 camera on either covers both
    assert sol.minCameraCover(TreeNode(0, TreeNode(0))) == 1

    # Three nodes in a line: camera on middle covers all
    assert sol.minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0)))) == 1

    # Perfect tree of 3: root + 2 children -> camera on root
    assert sol.minCameraCover(TreeNode(0, TreeNode(0), TreeNode(0))) == 1

    print("All tests passed for 968. Binary Tree Cameras")


if __name__ == "__main__":
    test_min_camera_cover()
