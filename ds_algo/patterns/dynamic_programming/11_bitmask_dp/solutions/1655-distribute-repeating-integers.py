"""
1655. Distribute Repeating Integers
https://leetcode.com/problems/distribute-repeating-integers/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP on customer satisfaction
- Count frequency of each distinct value in nums.
- dp[mask] = can we satisfy the set of customers indicated by mask?
- For each frequency count, try to assign it to a subset of remaining customers.
- Precompute the total quantity needed for each subset of customers.
- Iterate over frequencies, and for each mask, try all submasks.

Time: O(freq_count * 3^m) where m = number of customers (at most 10)
Space: O(2^m)
---
"""

from typing import List
from collections import Counter


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counts = list(Counter(nums).values())
        m = len(quantity)
        full = (1 << m) - 1

        # Precompute total quantity for each subset
        subset_sum = [0] * (full + 1)
        for mask in range(1, full + 1):
            # Find lowest set bit
            lsb = mask & (-mask)
            j = lsb.bit_length() - 1
            subset_sum[mask] = subset_sum[mask ^ lsb] + quantity[j]

        # dp[mask] = True if customers in mask can be satisfied
        dp = [False] * (full + 1)
        dp[0] = True

        for cnt in counts:
            # Process in reverse to avoid using same count twice
            # Actually, each count is used once, so iterate from full to 0
            for mask in range(full, 0, -1):
                if dp[mask]:
                    continue
                # Try all submasks of complement
                # We need to find submask s of mask such that dp[mask ^ s] is True
                # and subset_sum[s] <= cnt
                sub = mask
                while sub > 0:
                    if subset_sum[sub] <= cnt and dp[mask ^ sub]:
                        dp[mask] = True
                        break
                    sub = (sub - 1) & mask

        return dp[full]


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.canDistribute([1, 2, 3, 4], [2]) == False

    # Example 2
    assert sol.canDistribute([1, 2, 3, 3], [2]) == True

    # Example 3
    assert sol.canDistribute([1, 1, 2, 2], [2, 2]) == True

    # More complex
    assert sol.canDistribute([1, 1, 1, 1, 1], [2, 3]) == True
    assert sol.canDistribute([1, 1, 2, 2, 3, 3], [2, 2, 2]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test()
