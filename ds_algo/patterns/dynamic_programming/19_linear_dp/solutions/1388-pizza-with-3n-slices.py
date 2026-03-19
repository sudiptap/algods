"""
1388. Pizza With 3n Slices (Hard)
https://leetcode.com/problems/pizza-with-3n-slices/

Problem:
    Given a circular pizza with 3n slices, you pick a slice, then Alice
    and Bob pick adjacent slices. Repeat n times. Maximize the sum of
    your slices. Equivalently: pick n non-adjacent elements from a
    circular array of 3n elements to maximize their sum.

Pattern: 19 - Linear DP

Approach:
    1. Reduce to: pick exactly n non-adjacent elements from circular array
       of size 3n to maximize sum.
    2. Like House Robber II: solve for linear array [0..3n-2] and [1..3n-1],
       take the max.
    3. For linear version: dp[i][j] = max sum picking j elements from first
       i elements, with constraint no two adjacent.

Complexity:
    Time:  O(n^2) where n = len(slices)/3
    Space: O(n^2) for DP table, reducible to O(n)
"""

from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def solve(arr):
            m = len(arr)
            n = len(slices) // 3
            # dp[i][j] = max sum picking j elements from first i, no two adjacent
            INF = float('-inf')
            dp = [[INF] * (n + 1) for _ in range(m + 1)]
            dp[0][0] = 0
            for i in range(1, m + 1):
                dp[i][0] = 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    # Don't pick i-th
                    dp[i][j] = dp[i - 1][j]
                    # Pick i-th (can't pick (i-1)-th)
                    if i >= 2 and dp[i - 2][j - 1] != INF:
                        dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + arr[i - 1])
                    elif i == 1:
                        dp[i][j] = max(dp[i][j], arr[0] if j == 1 else INF)

            return dp[m][n]

        # Circular: exclude first or exclude last
        return max(solve(slices[1:]), solve(slices[:-1]))


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10, f"Test 1 failed: {sol.maxSizeSlices([1, 2, 3, 4, 5, 6])}"

    # Test 2
    assert sol.maxSizeSlices([8, 9, 8, 6, 1, 1]) == 16, f"Test 2 failed: {sol.maxSizeSlices([8, 9, 8, 6, 1, 1])}"

    # Test 3: minimum size
    assert sol.maxSizeSlices([1, 2, 3]) == 3, f"Test 3 failed"

    # Test 4
    assert sol.maxSizeSlices([4, 1, 2, 5, 8, 3, 1, 9, 7]) == 21, f"Test 4 failed: {sol.maxSizeSlices([4, 1, 2, 5, 8, 3, 1, 9, 7])}"

    print("All tests passed for 1388. Pizza With 3n Slices!")


if __name__ == "__main__":
    run_tests()
