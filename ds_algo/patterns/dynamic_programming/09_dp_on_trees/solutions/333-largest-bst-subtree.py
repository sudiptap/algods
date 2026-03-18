"""
333. Largest BST Subtree (Medium)

Given the root of a binary tree, find the largest subtree which is also a
Binary Search Tree (BST), where the largest means subtree has the largest
number of nodes.

Approach:
    Post-order traversal. Each node returns a tuple:
        (is_bst, size, min_val, max_val)
    If both children are BSTs and the current node's value fits within the
    valid range (left_max < node.val < right_min), combine into a larger BST.
    Otherwise, propagate the largest BST size found so far.

Time:  O(n) - visit each node once
Space: O(h) - recursion stack, h = height of tree
"""

import math
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """Return the size of the largest BST subtree in the binary tree."""
        self.max_size = 0

        def postorder(node: Optional[TreeNode]) -> Tuple[bool, int, int, int]:
            """Return (is_bst, size, min_val, max_val) for subtree rooted at node."""
            if not node:
                return (True, 0, math.inf, -math.inf)

            l_bst, l_size, l_min, l_max = postorder(node.left)
            r_bst, r_size, r_min, r_max = postorder(node.right)

            if l_bst and r_bst and l_max < node.val < r_min:
                size = l_size + 1 + r_size
                self.max_size = max(self.max_size, size)
                return (True, size, min(l_min, node.val), max(r_max, node.val))

            return (False, 0, 0, 0)

        postorder(root)
        return self.max_size


# ---------- Tests ----------

def build(vals, i=0):
    """Build tree from level-order list (None = null)."""
    if i >= len(vals) or vals[i] is None:
        return None
    node = TreeNode(vals[i])
    node.left = build(vals, 2 * i + 1)
    node.right = build(vals, 2 * i + 2)
    return node


def test():
    s = Solution()

    # Example 1: [10,5,15,1,8,null,7]
    #        10
    #       /  \
    #      5   15
    #     / \    \
    #    1   8    7
    # Largest BST is the subtree rooted at 5 (nodes: 1,5,8), size=3
    root = build([10, 5, 15, 1, 8, None, 7])
    assert s.largestBSTSubtree(root) == 3, f"Expected 3, got {s.largestBSTSubtree(root)}"

    # Example 2: single node
    root = TreeNode(1)
    assert s.largestBSTSubtree(root) == 1

    # Example 3: empty tree
    assert s.largestBSTSubtree(None) == 0

    # Example 4: entire tree is BST
    #     4
    #    / \
    #   2   6
    #  / \
    # 1   3
    root = build([4, 2, 6, 1, 3])
    assert s.largestBSTSubtree(root) == 5

    # Example 5: no subtree larger than 1
    #    1
    #   / \
    #  1   1
    root = build([1, 1, 1])
    assert s.largestBSTSubtree(root) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
