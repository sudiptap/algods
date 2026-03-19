"""
3336. Find Number of Subsequences With Equal GCD (Hard)

Pattern: 15_counting_combinatorial
- Split nums into two non-empty subsequences seq1, seq2 (partition is not required,
  but every element goes to exactly one). Count splits where gcd(seq1) == gcd(seq2).

Approach:
- dp[g1][g2] = number of ways to assign elements seen so far such that
  GCD of elements in group1 is g1 and GCD of elements in group2 is g2.
- g1=0 or g2=0 means that group is empty (gcd with 0 = identity).
- For each num, either put it in group1 (g1 = gcd(g1, num)) or group2.
- Answer: sum of dp[g][g] for all g >= 1.

Complexity:
- Time:  O(n * M^2) where M = max(nums), with GCD pruning much faster in practice
- Space: O(M^2)
"""

from typing import List
from math import gcd

MOD = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mx = max(nums)

        # dp[g1][g2] - use dict for sparsity
        dp = {}
        dp[(0, 0)] = 1

        for num in nums:
            new_dp = {}
            for (g1, g2), cnt in dp.items():
                # Option 1: put num in group1
                ng1 = gcd(g1, num)
                key1 = (ng1, g2)
                new_dp[key1] = (new_dp.get(key1, 0) + cnt) % MOD

                # Option 2: put num in group2
                ng2 = gcd(g2, num)
                key2 = (g1, ng2)
                new_dp[key2] = (new_dp.get(key2, 0) + cnt) % MOD
            dp = new_dp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 >= 1:
                ans = (ans + cnt) % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.subsequencePairCount([1, 2, 3, 4]) == 6

    # Example 2
    assert sol.subsequencePairCount([10, 20, 30]) == 2

    # Example 3
    assert sol.subsequencePairCount([1, 1, 1, 1]) == 14

    print("All tests passed!")


if __name__ == "__main__":
    test()
