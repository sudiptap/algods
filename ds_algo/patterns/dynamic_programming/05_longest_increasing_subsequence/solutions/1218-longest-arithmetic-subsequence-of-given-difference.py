"""
1218. Longest Arithmetic Subsequence of Given Difference (Medium)
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

Given an integer array arr and an integer difference, return the length of the
longest subsequence in arr which is an arithmetic sequence with the common
difference equal to difference. A subsequence does not need to be contiguous.

Pattern: LIS variant with HashMap
- dp[num] = length of longest arithmetic subsequence ending at num.
- For each num in arr: dp[num] = dp[num - difference] + 1.
- Answer: max(dp.values()).

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """Return length of longest arithmetic subsequence with given difference.

        Args:
            arr: Array of integers.
            difference: Required common difference between consecutive elements.

        Returns:
            Length of the longest valid subsequence.
        """
        dp = {}
        result = 1

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            if dp[num] > result:
                result = dp[num]

        return result


# ---------- tests ----------
def test_longest_subsequence():
    sol = Solution()

    # Example 1: [1,2,3,4] with diff=1 -> length 4
    assert sol.longestSubsequence([1, 2, 3, 4], 1) == 4

    # Example 2: [1,3,5,7] with diff=1 -> each alone, length 1
    assert sol.longestSubsequence([1, 3, 5, 7], 1) == 1

    # Example 3: [1,5,7,8,5,3,4,2,1] with diff=-2 -> [7,5,3,1] length 4
    assert sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4

    # diff=0: longest run of same value
    assert sol.longestSubsequence([3, 3, 3, 2, 3], 0) == 4

    # Single element
    assert sol.longestSubsequence([10], 5) == 1

    # Negative difference
    assert sol.longestSubsequence([5, 3, 1, -1], -2) == 4

    print("All tests passed for 1218. Longest Arithmetic Subsequence of Given Difference")


if __name__ == "__main__":
    test_longest_subsequence()
