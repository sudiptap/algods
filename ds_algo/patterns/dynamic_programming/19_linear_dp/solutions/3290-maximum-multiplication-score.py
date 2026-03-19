"""
3290. Maximum Multiplication Score (Medium)

Pattern: 19_linear_dp
- Given arrays a (size 4) and b (size n), choose 4 indices i0<i1<i2<i3 from b.
  Maximize a[0]*b[i0] + a[1]*b[i1] + a[2]*b[i2] + a[3]*b[i3].

Approach:
- dp[j] = max score after matching first j elements of a, scanning through b left to right.
- For each b[i], update dp[j] = max(dp[j], dp[j-1] + a[j-1]*b[i]) for j=4..1 (reverse).

Complexity:
- Time:  O(4 * n) = O(n)
- Space: O(1) (only 5 dp values)
"""

from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        INF = float('-inf')
        dp = [0] + [INF] * 4  # dp[j] = best score matching first j of a

        for val in b:
            for j in range(4, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + a[j - 1] * val)

        return dp[4]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxScore([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7]) == 26

    # Example 2
    assert sol.maxScore([-1, 4, 5, -2], [-5, -1, -3, -2, -4]) == -1

    # All positive
    assert sol.maxScore([1, 1, 1, 1], [1, 2, 3, 4]) == 10

    print("All tests passed!")


if __name__ == "__main__":
    test()
