"""
337. House Robber III (Medium)

Houses are arranged in a binary tree. Adjacent houses (parent-child) cannot
both be robbed. Find the maximum amount that can be robbed.

Approach:
    Post-order DFS returning a pair for each node:
        (rob_this, skip_this)
    - rob_this:  node.val + skip_left + skip_right
    - skip_this: max(rob_left, skip_left) + max(rob_right, skip_right)

Time:  O(n) - visit each node once
Space: O(h) - recursion stack
"""

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """Return the maximum amount of money that can be robbed."""

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            """Return (rob_this_node, skip_this_node)."""
            if not node:
                return (0, 0)

            rob_l, skip_l = dfs(node.left)
            rob_r, skip_r = dfs(node.right)

            rob_this = node.val + skip_l + skip_r
            skip_this = max(rob_l, skip_l) + max(rob_r, skip_r)

            return (rob_this, skip_this)

        return max(dfs(root))


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

    # Example 1: [3,2,3,null,3,null,1] -> 7 (rob 3+3+1... actually 3+3+1=7)
    #      3
    #     / \
    #    2   3
    #     \   \
    #      3   1
    root = build([3, 2, 3, None, 3, None, 1])
    assert s.rob(root) == 7, f"Expected 7, got {s.rob(root)}"

    # Example 2: [3,4,5,1,3,null,1] -> 9 (rob 4+5=9)
    #      3
    #     / \
    #    4   5
    #   / \   \
    #  1   3   1
    root = build([3, 4, 5, 1, 3, None, 1])
    assert s.rob(root) == 9, f"Expected 9, got {s.rob(root)}"

    # Single node
    assert s.rob(TreeNode(5)) == 5

    # Empty tree
    assert s.rob(None) == 0

    # Linear chain: 2 -> 1 -> 3 (left only)
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    assert s.rob(root) == 5  # rob 2 + 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
