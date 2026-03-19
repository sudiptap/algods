"""
1735. Count Ways to Make Array With Product
https://leetcode.com/problems/count-ways-to-make-array-with-product/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Prime factorize k, distribute prime factors using stars and bars
- For each query (n, k): factorize k into prime powers p1^e1 * p2^e2 * ...
- For each prime factor with exponent e, distribute e copies among n positions.
- Using stars and bars: C(e + n - 1, n - 1) ways for each prime.
- Total = product of C(ei + n - 1, n - 1) for all primes.
- Precompute combinations using Pascal's triangle or modular inverse.

Time: O(Q * sqrt(k) + precompute) per query
Space: O(max_val) for precomputation
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        # Precompute factorials and inverse factorials
        MAX = 10014 + 14  # n up to 10^4, e up to ~14 (2^14 > 10^4)
        fact = [1] * (MAX + 1)
        for i in range(1, MAX + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (MAX + 1)
        inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
        for i in range(MAX - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        def factorize(k):
            factors = {}
            d = 2
            while d * d <= k:
                while k % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    k //= d
                d += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors

        result = []
        for n, k in queries:
            factors = factorize(k)
            ways = 1
            for p, e in factors.items():
                # Distribute e copies of prime p among n slots: C(e + n - 1, e)
                ways = ways * comb(e + n - 1, e) % MOD
            result.append(ways)

        return result


# --- Tests ---
def test():
    sol = Solution()

    result = sol.waysToFillArray([[2, 6], [5, 1], [73, 660]])
    assert result == [4, 1, 50734910]

    result = sol.waysToFillArray([[1, 1], [2, 2], [3, 4]])
    assert result == [1, 2, 6]

    print("All tests passed!")


if __name__ == "__main__":
    test()
