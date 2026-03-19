"""
1691. Maximum Height by Stacking Cuboids
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: Sort cuboids, LIS-style with dimension constraints
- Key insight: it's always optimal to orient each cuboid so that the largest
  dimension is the height (we want to maximize total height).
- Sort each cuboid's dimensions, then sort all cuboids.
- Apply LIS-style DP: cuboid j can go on top of cuboid i if all three
  dimensions of j <= corresponding dimensions of i.
- dp[i] = max height ending with cuboid i on top.

Time: O(n^2) where n = number of cuboids
Space: O(n)
---
"""

from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Sort dimensions of each cuboid (smallest to largest)
        for c in cuboids:
            c.sort()

        # Sort cuboids
        cuboids.sort()

        n = len(cuboids)
        # dp[i] = max height with cuboid i on top of stack
        dp = [c[2] for c in cuboids]  # height is the largest dimension

        for i in range(1, n):
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        return max(dp)


# --- Tests ---
def test():
    sol = Solution()

    assert sol.maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]]) == 190
    assert sol.maxHeight([[38, 25, 45], [76, 35, 3]]) == 76
    assert sol.maxHeight([[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]) == 102

    # Single cuboid
    assert sol.maxHeight([[1, 2, 3]]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
