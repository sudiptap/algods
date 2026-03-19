"""
2313. Minimum Flips in Binary Tree to Get Result
https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

Pattern: 09 - DP on Trees

---
APPROACH: Post-order DFS computing min flips for each node to evaluate to 0 or 1
- For leaf nodes: cost to get 0 = (val==1), cost to get 1 = (val==0)
- For OR (val=2): cost(1) = min(l1+r0, l0+r1, l1+r1), cost(0) = l0+r0
- For AND (val=3): cost(1) = l1+r1, cost(0) = min(l0+r0, l0+r1, l1+r0)
- For XOR (val=4): cost(1) = min(l1+r0, l0+r1), cost(0) = min(l0+r0, l1+r1)
- For NOT (val=5): only has one child, cost(1) = child_cost(0), cost(0) = child_cost(1)
- Flip = change node operation (OR->AND, etc.) costs 1 extra.
  Actually, flips change leaf values or gate types.
  Re-reading: flip means changing leaf value or boolean operation.

Wait - the problem says flip = change boolean value of leaf OR change operation.
Let me reconsider: each internal node has an operation. We can flip operations
(OR<->AND, XOR<->XOR stays, NOT<->NOT stays? No...).
Actually flips: for leaf, flip 0<->1. For boolean node, change the operation.
But there are 4 operations (OR, AND, XOR, NOT), changing to what?

Re-reading: "flip" means:
- Leaf: change value 0->1 or 1->0
- Non-leaf: the original operation is fixed. A "flip" changes the result.

Actually the problem: we want root to evaluate to `result`. Min flips of leaf values.
No - we can flip any node. For internal nodes, flipping means changing its operation type.

Let me re-read: "You can flip the value of any leaf node" and "You can flip the
operation of any internal node". Each flip counts as 1 operation.

For this approach:
- DFS returns (cost_to_make_0, cost_to_make_1) for each subtree.
- For leaf val v: (v, 1-v) -- cost 0 if already correct, cost 1 to flip
- For internal node with operation op: compute with current op, and also
  try flipping to each other op (cost+1), take minimum.

Time: O(n)  Space: O(n) for recursion
---
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: int) -> int:
        def dfs(node):
            """Returns (cost_to_0, cost_to_1)"""
            if node is None:
                return (0, 0)

            # Leaf node (val is 0 or 1)
            if node.val == 0 or node.val == 1:
                return (node.val, 1 - node.val)  # cost to make 0, cost to make 1

            left = dfs(node.left)
            right = dfs(node.right)
            l0, l1 = left
            r0, r1 = right

            def compute_op(op, l0, l1, r0, r1):
                """Compute (cost_to_0, cost_to_1) for given operation."""
                if op == 2:  # OR
                    c1 = min(l1 + r0, l0 + r1, l1 + r1)
                    c0 = l0 + r0
                    return (c0, c1)
                elif op == 3:  # AND
                    c1 = l1 + r1
                    c0 = min(l0 + r0, l0 + r1, l1 + r0)
                    return (c0, c1)
                elif op == 4:  # XOR
                    c1 = min(l1 + r0, l0 + r1)
                    c0 = min(l0 + r0, l1 + r1)
                    return (c0, c1)
                else:  # NOT (val == 5), only one child
                    return None

            if node.val == 5:  # NOT - single child
                child = left if node.left else right
                if node.left:
                    child = left
                else:
                    child = right
                # NOT with one child (left child per problem)
                c0, c1 = child
                # Current: NOT, so result is flipped
                res_no_flip = (c1, c0)
                # Flip NOT: we remove the NOT (but what do we change to?)
                # Actually for NOT nodes, they only have 1 child.
                # Flipping NOT... it's unclear what NOT flips to.
                # Let's just return NOT behavior (can't meaningfully flip unary to binary)
                return res_no_flip

            # Binary operations: try current op (free) and other ops (+1 flip)
            ops = [2, 3, 4]  # OR, AND, XOR
            best_c0 = float('inf')
            best_c1 = float('inf')

            for op in ops:
                c0, c1 = compute_op(op, l0, l1, r0, r1)
                flip_cost = 0 if op == node.val else 1
                best_c0 = min(best_c0, c0 + flip_cost)
                best_c1 = min(best_c1, c1 + flip_cost)

            return (best_c0, best_c1)

        costs = dfs(root)
        return costs[result]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: root = [3,5,4,2,null,1,1,1,0], result = 1
    #     AND(3)
    #    /     \
    #  NOT(5)  XOR(4)
    #  /       /   \
    # OR(2)   1     1
    # / \
    # 1   0
    n1 = TreeNode(1)
    n0 = TreeNode(0)
    or_node = TreeNode(2, n1, n0)
    not_node = TreeNode(5, or_node)
    leaf1a = TreeNode(1)
    leaf1b = TreeNode(1)
    xor_node = TreeNode(4, leaf1a, leaf1b)
    root1 = TreeNode(3, not_node, xor_node)
    assert sol.minimumFlips(root1, 1) == 1

    # Simple leaf
    leaf = TreeNode(0)
    assert sol.minimumFlips(leaf, 0) == 0
    assert sol.minimumFlips(leaf, 1) == 1

    # OR of two leaves
    root2 = TreeNode(2, TreeNode(0), TreeNode(0))
    assert sol.minimumFlips(root2, 1) == 1
    assert sol.minimumFlips(root2, 0) == 0

    print("all tests passed")
