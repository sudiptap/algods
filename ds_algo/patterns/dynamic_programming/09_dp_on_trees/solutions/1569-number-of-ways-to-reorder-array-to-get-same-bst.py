"""
1569. Number of Ways to Reorder Array to Get Same BST
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

Pattern: 09 - DP on Trees

---
APPROACH: Combinatorics on BST structure (recursive)
- Root is always first element. Elements < root go to left subtree,
  elements > root go to right subtree.
- The relative order within left and right subtrees matters, but the
  interleaving between left and right can be chosen freely.
- Number of interleavings = C(left_size + right_size, left_size)
- Multiply by recursive results for left and right subtrees.
- Answer = total ways - 1 (exclude the original ordering).

Time: O(n^2) for the recursion and combination computation
Space: O(n^2) for Pascal's triangle
---
"""

from typing import List
from math import comb

MOD = 10**9 + 7


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def count(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            # C(len(left)+len(right), len(left)) * count(left) * count(right)
            return comb(len(left) + len(right), len(left)) % MOD * count(left) % MOD * count(right) % MOD

        return (count(nums) - 1) % MOD


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.numOfWays([2, 1, 3]) == 1

    # Example 2
    assert sol.numOfWays([3, 4, 5, 1, 2]) == 5

    # Example 3
    assert sol.numOfWays([1, 2, 3]) == 0  # Only one way to build this BST

    # Single element
    assert sol.numOfWays([1]) == 0

    # Two elements
    assert sol.numOfWays([2, 1]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
