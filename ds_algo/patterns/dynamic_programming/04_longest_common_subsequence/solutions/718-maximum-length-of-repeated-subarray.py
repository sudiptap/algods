"""
718. Maximum Length of Repeated Subarray (Medium)

Given two integer arrays nums1 and nums2, return the maximum length of a
subarray that appears in both arrays.

Pattern: Longest Common Subsequence variant (contiguous version)
- dp[i][j] = length of common subarray ending at nums1[i-1] and nums2[j-1].
- If nums1[i-1] == nums2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
- Otherwise: dp[i][j] = 0  (must be contiguous, unlike LCS)
- Answer is the max value in the dp table.

Time:  O(m * n)
Space: O(n) with rolling array optimisation
"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """Return maximum length of a subarray common to both arrays."""
        m, n = len(nums1), len(nums2)
        # Use shorter array for the inner dimension to save space
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m

        dp = [0] * (n + 1)
        result = 0

        for i in range(1, m + 1):
            # Traverse right-to-left so dp[j-1] still holds the previous row value
            for j in range(n, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    result = max(result, dp[j])
                else:
                    dp[j] = 0

        return result


# ----------------- Tests -----------------
def run_tests():
    sol = Solution()

    # Example 1
    assert sol.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3, "Test 1 failed"

    # Example 2
    assert sol.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5, "Test 2 failed"

    # No common subarray
    assert sol.findLength([1, 2, 3], [4, 5, 6]) == 0, "Test 3 failed"

    # Single element match
    assert sol.findLength([1], [1]) == 1, "Test 4 failed"

    # Single element no match
    assert sol.findLength([1], [2]) == 0, "Test 5 failed"

    # Common subarray in the middle
    assert sol.findLength([1, 2, 3, 4, 5], [8, 2, 3, 4, 9]) == 3, "Test 6 failed"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
