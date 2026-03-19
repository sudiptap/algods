"""
2003. Smallest Missing Genetic Value in Each Subtree (Hard)
https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

Given a tree where each node has a unique genetic value, for each node
find the smallest positive integer not in its subtree.

Pattern: DP on Trees
Approach:
- All nodes except those on the path from node-with-value-1 to root
  have answer 1 (since value 1 is not in their subtree).
- Find node with value 1, DFS up to root. For each ancestor on this
  path, DFS into other subtrees to collect values, then increment
  the missing counter.
- Track seen values in a set; advance missing from 1 upward.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        """Return smallest missing genetic value for each subtree.

        Args:
            parents: Parent array (parents[0] = -1 for root).
            nums: Genetic values (all distinct, 1-indexed values).

        Returns:
            Array of smallest missing values per subtree.
        """
        n = len(parents)
        ans = [1] * n

        # Find node with value 1
        if 1 not in nums:
            return ans

        node1 = nums.index(1)

        # Build children list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        # Walk from node1 to root, collecting all subtree values
        seen = set()
        missing = 1

        # DFS helper to collect all values in subtree
        def collect(node):
            stack = [node]
            while stack:
                u = stack.pop()
                if u in visited:
                    continue
                visited.add(u)
                seen.add(nums[u])
                for c in children[u]:
                    if c not in visited:
                        stack.append(c)

        visited = set()
        cur = node1
        while cur != -1:
            collect(cur)
            while missing in seen:
                missing += 1
            ans[cur] = missing
            cur = parents[cur]

        return ans


# ---------- tests ----------
def test_smallest_missing():
    sol = Solution()

    # Example 1
    assert sol.smallestMissingValueSubtree(
        [-1, 0, 0, 2], [1, 2, 3, 4]
    ) == [5, 1, 1, 1]

    # Example 2
    assert sol.smallestMissingValueSubtree(
        [-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3]
    ) == [7, 1, 1, 4, 2, 1]

    # Example 3
    assert sol.smallestMissingValueSubtree(
        [-1, 2, 3, 0, 2, 4, 1], [2, 3, 4, 5, 6, 7, 8]
    ) == [1, 1, 1, 1, 1, 1, 1]

    print("All tests passed for 2003. Smallest Missing Genetic Value in Each Subtree")


if __name__ == "__main__":
    test_smallest_missing()
