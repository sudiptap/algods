"""
1981. Minimize the Difference Between Target and Chosen Elements (Medium)
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

Given an m x n matrix mat, choose one element from each row. Minimize
|sum_of_chosen - target|.

Pattern: 0/1 Knapsack (Bitset DP)
Approach:
- Track all reachable sums using a set (or bitset).
- For each row, expand reachable sums by adding each possible element.
- After processing all rows, find the reachable sum closest to target.
- Optimization: prune sums that are too large (above target + max possible
  reduction from remaining rows).

Time:  O(m * n * S) where S = range of reachable sums
Space: O(S)
"""

from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """Return minimum |sum - target| choosing one element per row.

        Args:
            mat: m x n integer matrix.
            target: Target sum.

        Returns:
            Minimum absolute difference.
        """
        possible = {0}

        for row in mat:
            new_possible = set()
            for s in possible:
                for val in row:
                    new_possible.add(s + val)
            possible = new_possible

            # Pruning: keep only sums <= target + some buffer,
            # but we must keep at least the minimum sum >= target
            # and all sums <= target
            min_above = float('inf')
            pruned = set()
            for s in possible:
                if s <= target:
                    pruned.add(s)
                else:
                    if s < min_above:
                        min_above = s
                    pruned.add(s)
            # Keep sums below target and the smallest sum above target
            final = set()
            for s in pruned:
                if s <= target or s == min_above:
                    final.add(s)
            possible = final

        return min(abs(s - target) for s in possible)


# ---------- tests ----------
def test_minimize_difference():
    sol = Solution()

    # Example 1
    assert sol.minimizeTheDifference([[1,2,3],[4,5,6],[7,8,9]], 13) == 0

    # Example 2
    assert sol.minimizeTheDifference([[1],[2],[3]], 100) == 94

    # Example 3
    assert sol.minimizeTheDifference([[1,2,9,8,7]], 6) == 1

    # Single element
    assert sol.minimizeTheDifference([[5]], 5) == 0

    # Target is 0
    assert sol.minimizeTheDifference([[1,2],[3,4]], 0) == 4

    print("All tests passed for 1981. Minimize the Difference Between Target and Chosen Elements")


if __name__ == "__main__":
    test_minimize_difference()
