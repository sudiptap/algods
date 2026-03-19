"""
1879. Minimum XOR Sum of Two Arrays (Hard)
https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

Given two integer arrays nums1 and nums2 of length n, rearrange nums2
to minimize the XOR sum: sum of nums1[i] XOR nums2[perm[i]].

Pattern: Bitmask DP
Approach:
- dp[mask] = minimum XOR sum when assigning the elements of nums2
  indicated by set bits in mask to the first popcount(mask) elements
  of nums1.
- pos = popcount(mask). For each bit j set in mask, try assigning
  nums2[j] to nums1[pos-1], add (nums1[pos-1] ^ nums2[j]) + dp[mask ^ (1<<j)].
- Base: dp[0] = 0.
- Answer: dp[(1<<n)-1].

Time:  O(2^n * n)
Space: O(2^n)
"""

from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """Return minimum XOR sum after optimally rearranging nums2.

        Args:
            nums1: First array.
            nums2: Second array.

        Returns:
            Minimum possible XOR sum.
        """
        n = len(nums1)
        full = 1 << n
        dp = [float('inf')] * full
        dp[0] = 0

        for mask in range(1, full):
            pos = bin(mask).count('1') - 1  # 0-indexed position in nums1
            for j in range(n):
                if mask & (1 << j):
                    dp[mask] = min(dp[mask],
                                   dp[mask ^ (1 << j)] + (nums1[pos] ^ nums2[j]))

        return dp[full - 1]


# ---------- tests ----------
def test_minimum_xor_sum():
    sol = Solution()

    # Example 1: [1,2] [2,3] -> (1^3)+(2^2)=2+0=2
    assert sol.minimumXORSum([1, 2], [2, 3]) == 2

    # Example 2: [1,0,3] [5,3,4] -> (1^4)+(0^5)+(3^3)=5+5+0=10 or better
    assert sol.minimumXORSum([1, 0, 3], [5, 3, 4]) == 8

    # Single element
    assert sol.minimumXORSum([5], [3]) == 6

    # Identical arrays
    assert sol.minimumXORSum([1, 2, 3], [1, 2, 3]) == 0

    print("All tests passed for 1879. Minimum XOR Sum of Two Arrays")


if __name__ == "__main__":
    test_minimum_xor_sum()
