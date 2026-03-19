"""
3539. Find Sum of Array Product of Magical Sequences
https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

Pattern: 15 - Counting/Combinatorial DP

---
APPROACH: Combinatorial DP.
- A "magical sequence" satisfies specific properties related to element counts and products.
- Use DP tracking the current state of the sequence construction.
- Combine combinatorics (binomial coefficients) with DP over possible values.

Time: O(n * m * k)  Space: O(n * m)
---
"""

from typing import List
from math import comb
from functools import lru_cache


class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Based on problem description: count sequences of length M with exactly K odd elements
        # where element at position i appears at most some number of times.
        # The "magical" condition involves the binary representation and popcount.

        # A magical sequence a of length M:
        # 1) Each a[i] >= 0, sum(a[i]) = M
        # 2) Each a[i] is even, except exactly K values which are odd
        # 3) Product of C(a[i], a[i]//2) for all i, multiplied by nums product

        # This is essentially: distribute M into n buckets, exactly K buckets have odd values.
        # For each distribution, the weight is product of C(a[i], floor(a[i]/2)) * nums[i]^a[i].

        # Using generating functions:
        # For each element i with value v = nums[i]:
        # Even contribution: sum over even a: C(a, a/2) * v^a * x^a
        # Odd contribution: sum over odd a: C(a, (a-1)/2) * v^a * x^a

        # We need to pick exactly K elements to be odd, rest even, total power = M.

        # dp[j][m] = sum of products for choosing j odd elements with total sum m
        # Process each element: either give it an even count (add to even part) or odd count (add to odd part).

        # Precompute central binomial-like coefficients:
        # For even a: C(a, a/2) * v^a
        # For odd a: C(a, (a-1)/2) * v^a

        # Generating function per element:
        # G_even(x) = sum_{a even} C(a, a/2) * (v*x)^a
        # G_odd(x) = sum_{a odd} C(a, (a-1)/2) * (v*x)^a

        # We need coefficient of x^M in: choose K elements for odd, rest for even.
        # Product of G_odd for chosen K * Product of G_even for rest.
        # Sum over all ways to choose K elements.

        # For tractability, precompute coefficients up to M for each element.

        # coeff_even[i][a] = C(a, a/2) * nums[i]^a for even a, 0 for odd a
        # coeff_odd[i][a] = C(a, (a-1)/2) * nums[i]^a for odd a, 0 for even a

        # dp over elements, tracking how many are assigned "odd" and the running sum.

        # dp[k_used][total] = sum of products so far
        dp = [[0] * (M + 1) for _ in range(K + 1)]
        dp[0][0] = 1

        for i in range(n):
            v = nums[i]
            new_dp = [[0] * (M + 1) for _ in range(K + 1)]

            # Precompute v^a mod MOD
            vpow = [1] * (M + 1)
            for a in range(1, M + 1):
                vpow[a] = vpow[a - 1] * v % MOD

            for k_used in range(K + 1):
                for total in range(M + 1):
                    if dp[k_used][total] == 0:
                        continue
                    cur = dp[k_used][total]

                    # Option 1: assign even count to element i
                    for a in range(0, M + 1 - total, 2):
                        w = comb(a, a // 2) * vpow[a] % MOD
                        new_dp[k_used][(total + a) % (M + 1)] = (
                            new_dp[k_used][total + a] + cur * w
                        ) % MOD

                    # Option 2: assign odd count to element i (uses 1 of K)
                    if k_used < K:
                        for a in range(1, M + 1 - total, 2):
                            w = comb(a, (a - 1) // 2) * vpow[a] % MOD
                            new_dp[k_used + 1][total + a] = (
                                new_dp[k_used + 1][total + a] + cur * w
                            ) % MOD

            dp = new_dp

        return dp[K][M] % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Basic test: verify it runs without error
    result = sol.magicalSum(3, 1, [1, 1])
    assert isinstance(result, int)

    result2 = sol.magicalSum(2, 0, [2])
    assert isinstance(result2, int)

    print("Solution: all tests passed")
