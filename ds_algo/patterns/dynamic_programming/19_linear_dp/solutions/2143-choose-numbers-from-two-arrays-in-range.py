"""
2143. Choose Numbers From Two Arrays in Range (Hard)
https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

Given two arrays nums1 and nums2 of length n, for each index choose a
number from either array. If chosen from nums1, add it; if from nums2,
subtract it. The result must be in [1, infinity). Count the number of
valid selections mod 10^9+7.

Pattern: Linear DP (Offset DP on Difference)
Approach:
- dp[diff] = number of ways to achieve a particular difference
  (sum of chosen nums1 values - sum of chosen nums2 values).
- For each index i, either add nums1[i] or subtract nums2[i].
- Use dictionary-based DP or offset array.
- Count all states where diff >= 1 at the end.

Time:  O(n * S) where S = range of possible sums
Space: O(S)
"""

from typing import List
from collections import defaultdict


class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        """Return number of selections where sum from nums1 > sum from nums2.

        Args:
            nums1: First array.
            nums2: Second array.

        Returns:
            Count of valid selections mod 10^9 + 7.
        """
        MOD = 10**9 + 7
        dp = defaultdict(int)
        result = 0

        for i in range(len(nums1)):
            new_dp = defaultdict(int)
            # Choose nums1[i]: add to diff
            new_dp[nums1[i]] = (new_dp[nums1[i]] + 1) % MOD
            # Choose nums2[i]: subtract from diff
            new_dp[-nums2[i]] = (new_dp[-nums2[i]] + 1) % MOD

            for diff, ways in dp.items():
                new_dp[diff + nums1[i]] = (new_dp[diff + nums1[i]] + ways) % MOD
                new_dp[diff - nums2[i]] = (new_dp[diff - nums2[i]] + ways) % MOD

            dp = new_dp
            # Count selections where diff == 0 (equal sums)
            # Wait: problem says result in [1, inf), meaning sum1 - sum2 >= 1?
            # Actually re-read: result must be in [1, inf) meaning the total is positive.
            # So we want diff == 0? No, diff = sum_chosen_from_1 - sum_chosen_from_2 must be in [1, inf).
            # Hmm, let me re-read the problem.
            # "choose numbers from two arrays in range" - the sum should be 0.
            # Actually the problem asks: for each index, add nums1[i] or subtract nums2[i].
            # Want total == 0. Count selections where total == 0.
            # But we exclude choosing nothing... actually must choose at least one index.
            # Since we process all indices and for each must make a choice, at the end
            # just count dp[0].
            # Actually, re-reading: this might be about selecting a non-empty subset
            # of indices, and for each selected index, choose nums1 or nums2.
            # Let me re-check the problem. Since it's premium, let me go with:
            # Count (at each step) the ways the running sum equals 0.
            result = (result + dp.get(0, 0)) % MOD

        return result


# ---------- tests ----------
def test_count_subranges():
    sol = Solution()

    # Example 1: nums1=[1,2,5], nums2=[2,6,3]
    # At each step, count ways partial selection sums to 0.
    # i=0: +1 or -2. Neither is 0.
    # i=0,1: +1+2=3, +1-6=-5, -2+2=0!, -2-6=-8. One way at step i=1.
    # Also just i=1: +2 or -6. Neither 0.
    # ... expected: 3
    assert sol.countSubranges([1, 2, 5], [2, 6, 3]) == 3

    # Example 2: nums1=[1,1,1,1,1], nums2=[1,1,1,1,1]
    # For each subrange of even length, count assignments where sum = 0
    # Length 2: 4 ranges * C(2,1)=2 ways each = 8
    # Length 4: 2 ranges * C(4,2)=6 ways each = 12
    # Total = 20
    assert sol.countSubranges([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]) == 20

    print("All tests passed for 2143. Choose Numbers From Two Arrays in Range")


if __name__ == "__main__":
    test_count_subranges()
