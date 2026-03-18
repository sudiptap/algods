"""
300. Longest Increasing Subsequence (Medium)
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Approach 1 - O(n^2) DP:
    dp[i] = length of LIS ending at index i.
    dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i].

Approach 2 - O(n log n) Patience Sorting:
    Maintain a list 'tails' where tails[k] is the smallest tail element
    of all increasing subsequences of length k+1.
    For each num, binary-search for its position in tails.

Time:  O(n log n) for the optimal approach
Space: O(n)
"""

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Return the length of the longest strictly increasing subsequence.

        Uses O(n log n) patience sorting with bisect.

        Args:
            nums: List of integers, 1 <= len(nums) <= 2500.

        Returns:
            Length of the longest increasing subsequence.
        """
        tails: List[int] = []

        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """O(n^2) DP approach for reference.

        Args:
            nums: List of integers.

        Returns:
            Length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# ---------- tests ----------
def test_longest_increasing_subsequence():
    sol = Solution()

    for fn_name in ("lengthOfLIS", "lengthOfLIS_dp"):
        fn = getattr(sol, fn_name)

        # Example 1: [10,9,2,5,3,7,101,18] -> LIS is [2,3,7,101], length 4
        assert fn([10, 9, 2, 5, 3, 7, 101, 18]) == 4

        # Example 2
        assert fn([0, 1, 0, 3, 2, 3]) == 4

        # Example 3: all same -> 1
        assert fn([7, 7, 7, 7, 7, 7, 7]) == 1

        # Single element
        assert fn([10]) == 1

        # Already sorted
        assert fn([1, 2, 3, 4, 5]) == 5

        # Reverse sorted
        assert fn([5, 4, 3, 2, 1]) == 1

        print(f"  {fn_name}: OK")

    print("All tests passed for 300. Longest Increasing Subsequence")


if __name__ == "__main__":
    test_longest_increasing_subsequence()
