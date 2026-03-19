"""
3409. Longest Subsequence With Decreasing Adjacent Difference
https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

Pattern: 05 - LIS variant with dp[val][diff]

---
APPROACH: dp[val][diff] = longest subsequence ending with value val, last adjacent diff = diff
- For each num, for each possible diff d, look at prev values num-d and num+d.
- dp[num][d] = max over suffix_max[prev][d] + 1 (non-increasing: prev diff >= current diff d).
- Maintain suffix_max[v][d] = max(dp[v][d], dp[v][d+1], ...) for efficient lookup.

Time: O(n * max_val)  Space: O(max_val^2)
---
"""

from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        max_val = max(nums)
        # dp[v][d] = length of longest subseq ending at value v with last diff exactly d
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        # suffix_max[v][d] = max of dp[v][d..max_val]
        suffix_max = [[0] * (max_val + 2) for _ in range(max_val + 1)]

        ans = 1

        for num in nums:
            # Process from largest diff to smallest to avoid using updates from same iteration
            for d in range(max_val, -1, -1):
                for prev in (num - d, num + d):
                    if 0 <= prev <= max_val and (prev != num or d == 0):
                        # non-increasing: previous diff >= d, so look at suffix_max[prev][d]
                        val = suffix_max[prev][d] + 1
                        dp[num][d] = max(dp[num][d], val)

            # Rebuild suffix_max for num
            suffix_max[num][max_val + 1] = 0
            for d in range(max_val, -1, -1):
                suffix_max[num][d] = max(dp[num][d], suffix_max[num][d + 1])

            ans = max(ans, suffix_max[num][0])

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestSubsequence([16, 6, 3]) == 3
    assert sol.longestSubsequence([6, 5, 3, 4, 2, 1]) == 4
    assert sol.longestSubsequence([0, 4, 8, 12]) == 4
    assert sol.longestSubsequence([1]) == 1

    print("Solution: all tests passed")
