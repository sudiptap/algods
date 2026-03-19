"""
1458. Max Dot Product of Two Subsequences (Hard)
https://leetcode.com/problems/max-dot-product-of-two-subsequences/

Problem:
    Given two arrays nums1 and nums2, find two subsequences of equal
    length (at least 1) such that their dot product is maximized.

Pattern: 04 - Longest Common Subsequence

Approach:
    1. dp[i][j] = max dot product using nums1[:i] and nums2[:j] with
       at least one pair selected.
    2. Transition: dp[i][j] = max of:
       - nums1[i-1] * nums2[j-1] (start fresh or extend)
       - dp[i-1][j-1] + nums1[i-1] * nums2[j-1] (extend previous)
       - dp[i-1][j] (skip nums1[i-1])
       - dp[i][j-1] (skip nums2[j-1])
    3. Initialize dp with -inf to enforce at least one selection.

Complexity:
    Time:  O(n * m) where n = len(nums1), m = len(nums2)
    Space: O(n * m) for DP table
"""

from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = float('-inf')

        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    product,
                    max(dp[i - 1][j - 1], 0) + product,
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

        return dp[n][m]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.maxDotProduct([2, 1, -2, 5], [3, 0, -6]) == 18, \
        f"Test 1 failed: {sol.maxDotProduct([2, 1, -2, 5], [3, 0, -6])}"

    # Test 2
    assert sol.maxDotProduct([3, -2], [2, -6, 7]) == 21, \
        f"Test 2 failed: {sol.maxDotProduct([3, -2], [2, -6, 7])}"

    # Test 3: all negative
    assert sol.maxDotProduct([-1, -1], [1, 1]) == -1, \
        f"Test 3 failed: {sol.maxDotProduct([-1, -1], [1, 1])}"

    # Test 4: single elements
    assert sol.maxDotProduct([5], [3]) == 15, "Test 4 failed"

    # Test 5
    assert sol.maxDotProduct([-3, -8], [9, 2]) == -6, \
        f"Test 5 failed: {sol.maxDotProduct([-3, -8], [9, 2])}"

    print("All tests passed for 1458. Max Dot Product of Two Subsequences!")


if __name__ == "__main__":
    run_tests()
