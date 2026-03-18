"""
95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

Pattern: 09 - DP on Trees (recursive tree generation)

Related: #96 (Unique BSTs — just count, uses Catalan numbers)

---
APPROACH: Recursive with memoization
- For range [lo, hi], pick each value i as root
- Left subtrees = all BSTs from [lo, i-1]
- Right subtrees = all BSTs from [i+1, hi]
- Combine every left with every right → one tree per combination
- Memoize on (lo, hi)

Base: lo > hi → [None] (empty subtree)

The number of trees = Catalan(n), which grows as O(4^n / n^(3/2))

Time: O(n * Catalan(n))  Space: O(n * Catalan(n)) for all trees
---
"""

from typing import List, Optional
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        @lru_cache(maxsize=None)
        def build(lo: int, hi: int) -> tuple:
            if lo > hi:
                return (None,)

            trees = []
            for root_val in range(lo, hi + 1):
                left_trees = build(lo, root_val - 1)
                right_trees = build(root_val + 1, hi)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val, left, right)
                        trees.append(root)

            return tuple(trees)

        return list(build(1, n))


def tree_to_list(root):
    """Serialize tree to level-order list for testing."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # n=3: should produce 5 trees (Catalan(3) = 5)
    trees_3 = sol.generateTrees(3)
    assert len(trees_3) == 5

    # n=1: single node
    trees_1 = sol.generateTrees(1)
    assert len(trees_1) == 1
    assert trees_1[0].val == 1

    # n=2: Catalan(2) = 2
    trees_2 = sol.generateTrees(2)
    assert len(trees_2) == 2

    # n=4: Catalan(4) = 14
    trees_4 = sol.generateTrees(4)
    assert len(trees_4) == 14

    # verify all trees for n=3 contain nodes {1,2,3}
    for t in trees_3:
        vals = set()
        def collect(node):
            if node:
                vals.add(node.val)
                collect(node.left)
                collect(node.right)
        collect(t)
        assert vals == {1, 2, 3}

    print("all tests passed")
