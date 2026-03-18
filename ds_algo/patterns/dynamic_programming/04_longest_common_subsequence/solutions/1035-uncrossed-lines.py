"""
1035. Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/

Pattern: 04 - Longest Common Subsequence

---
APPROACH: LCS (Longest Common Subsequence)
- Drawing uncrossed lines between nums1 and nums2 where values match
  is exactly the Longest Common Subsequence problem.
- dp[i][j] = LCS of nums1[:i] and nums2[:j].
- If nums1[i-1] == nums2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
  Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Time:  O(m * n)
Space: O(m * n), optimizable to O(min(m, n))
---
"""

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """Return max number of uncrossed lines (= LCS length)."""
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2
    assert sol.maxUncrossedLines(
        [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]
    ) == 3
    assert sol.maxUncrossedLines(
        [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]
    ) == 2
    assert sol.maxUncrossedLines([1], [1]) == 1
    assert sol.maxUncrossedLines([1], [2]) == 0

    print("Solution: all tests passed")
