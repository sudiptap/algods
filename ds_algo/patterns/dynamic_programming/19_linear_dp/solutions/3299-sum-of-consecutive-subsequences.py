"""
3299. Sum of Consecutive Subsequences (Hard)

Pattern: 19_linear_dp
- Find the sum of all subsequences where consecutive elements differ by exactly 1
  (ascending or descending). Return sum mod 10^9+7.

Approach:
- For ascending subsequences ending at nums[i] with value v:
  count_asc[v] += (1 + count_asc[v-1]), sum_asc[v] += (v + sum_asc[v-1] + v * count_asc[v-1])
  Simplified: each element can start a new subsequence or extend one ending with v-1.
- Similarly for descending (extend subsequences ending with v+1).
- But single-element subsequences are counted in both, so subtract sum of single elements.
- Contribution-based: for each value v at index i, it can extend subsequences ending at v-1
  (for ascending) and v+1 (for descending).

Complexity:
- Time:  O(n)
- Space: O(n)
"""

from typing import List
from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        # count[v] = number of consecutive subsequences ending with value v
        # total_sum[v] = sum of all elements in those subsequences

        # Ascending: each subseq has elements with values increasing by 1
        asc_count = defaultdict(int)
        asc_sum = defaultdict(int)
        total = 0

        for v in nums:
            prev_c = asc_count[v - 1]
            prev_s = asc_sum[v - 1]
            # New subsequences ending at v: prev_c extensions + 1 new single
            new_c = (prev_c + 1) % MOD
            new_s = (prev_s + v * new_c) % MOD
            asc_count[v] = (asc_count[v] + new_c) % MOD
            asc_sum[v] = (asc_sum[v] + new_s) % MOD
            total = (total + new_s) % MOD

        # Descending: values decrease by 1
        desc_count = defaultdict(int)
        desc_sum = defaultdict(int)

        for v in nums:
            prev_c = desc_count[v + 1]
            prev_s = desc_sum[v + 1]
            new_c = (prev_c + 1) % MOD
            new_s = (prev_s + v * new_c) % MOD
            desc_count[v] = (desc_count[v] + new_c) % MOD
            desc_sum[v] = (desc_sum[v] + new_s) % MOD
            total = (total + new_s) % MOD

        # Single-element subsequences counted twice, subtract once
        for v in nums:
            total = (total - v) % MOD

        return total % MOD


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [1,2] -> [1],[2],[1,2] sums = 1+2+3 = 6
    assert sol.getSum([1, 2]) == 6

    # Example 2
    assert sol.getSum([1, 4, 2, 3]) == 31

    print("All tests passed!")


if __name__ == "__main__":
    test()
