"""
1027. Longest Arithmetic Subsequence
https://leetcode.com/problems/longest-arithmetic-subsequence/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: DP with hash map per index
- dp[i] = dictionary mapping common difference d -> length of longest
  arithmetic subsequence ending at index i with that difference.
- For each pair (j, i) with j < i:
    d = nums[i] - nums[j]
    dp[i][d] = dp[j].get(d, 1) + 1
- Answer is the maximum across all dp[i] values.

Time:  O(n^2)
Space: O(n^2)   (each index stores at most n-1 differences)
---
"""

from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """Return the length of the longest arithmetic subsequence in nums."""
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 2

        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j].get(d, 1) + 1
                ans = max(ans, dp[i][d])

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestArithSeqLength([3, 6, 9, 12]) == 4
    assert sol.longestArithSeqLength([9, 4, 7, 2, 10]) == 3
    assert sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
    assert sol.longestArithSeqLength([1, 1, 1, 1]) == 4  # diff = 0
    assert sol.longestArithSeqLength([1, 2]) == 2

    print("Solution: all tests passed")
