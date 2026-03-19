"""
1373. Maximum Sum BST in Binary Tree (Hard)
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

Problem:
    Given a binary tree, find the maximum sum of all keys of any sub-tree
    which is also a Binary Search Tree (BST).

Pattern: 09 - DP on Trees

Approach:
    1. Post-order traversal returning (is_bst, subtree_sum, min_val, max_val).
    2. A node's subtree is a BST if:
       - Left and right subtrees are BSTs.
       - node.val > left's max and node.val < right's min.
    3. If BST, compute sum = left_sum + right_sum + node.val, update global max.
    4. If not BST, propagate "not BST" upward.

Complexity:
    Time:  O(n) - visit each node once
    Space: O(h) for recursion stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            """Returns (is_bst, sum, min_val, max_val)."""
            if not node:
                return (True, 0, float('inf'), float('-inf'))

            l_bst, l_sum, l_min, l_max = dfs(node.left)
            r_bst, r_sum, r_min, r_max = dfs(node.right)

            if l_bst and r_bst and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                self.ans = max(self.ans, total)
                return (True, total, min(l_min, node.val), max(r_max, node.val))

            return (False, 0, 0, 0)

        dfs(root)
        return self.ans


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6] -> 20
    root = TreeNode(1)
    root.left = TreeNode(4, TreeNode(2), TreeNode(4))
    root.right = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
    assert sol.maxSumBST(root) == 20, f"Test 1 failed: {sol.maxSumBST(root)}"

    # Test 2: [4,3,null,1,2] -> whole tree is BST, sum=4+3+1+2=10
    root = TreeNode(4, TreeNode(3, TreeNode(1, None, TreeNode(2))))
    assert sol.maxSumBST(root) == 10, f"Test 2 failed: {sol.maxSumBST(root)}"

    # Test 3: single node
    root = TreeNode(5)
    assert sol.maxSumBST(root) == 5, "Test 3 failed"

    # Test 4: all negative, answer is 0 (empty BST)
    root = TreeNode(-4, TreeNode(-2), TreeNode(-5))
    assert sol.maxSumBST(root) == 0, f"Test 4 failed: {sol.maxSumBST(root)}"

    # Test 5: [-4, -2, -5] is BST? -2 < -4? No. So not BST at root.
    # -2 alone: sum=-2. -5 alone: sum=-5. All negative -> answer 0.

    print("All tests passed for 1373. Maximum Sum BST in Binary Tree!")


if __name__ == "__main__":
    run_tests()
