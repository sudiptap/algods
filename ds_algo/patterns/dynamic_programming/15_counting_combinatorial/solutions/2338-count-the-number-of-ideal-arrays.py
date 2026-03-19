"""
2338. Count the Number of Ideal Arrays
https://leetcode.com/problems/count-the-number-of-ideal-arrays/

Pattern: 15 - Counting/Combinatorial

---
APPROACH: Prime factorization + stars and bars
- An ideal array has arr[i] | arr[i+1] for each i. Last element <= maxValue.
- The "shape" of the array is determined by the sequence of distinct values
  (each divides the next). For a sequence of length k, we can distribute
  it into n positions using stars-and-bars: C(n-1, k-1).
- Count distinct divisor chains ending at each value v <= maxValue using
  prime factorization: if v = p1^a1 * p2^a2 * ..., the chain length minus 1
  equals sum of exponents. The number of chains with that product = product
  of C(n-1, exponents distributed across n slots).
- For each value v, factorize, get exponents e1, e2, ..., and the contribution
  is product of C(n-1+ei-1, ei) ... no, it's product of C(n-1, ei) using
  stars and bars for distributing each prime's exponents across n-1 "gaps".

Actually: for each prime p with exponent e in v, we need to place e
multiplications by p across n-1 transitions. This is C(n-1, e) ... no,
it's C(n-1+e-1, e) = C(n+e-2, e) if we allow repeated positions...

Correct formula: for a chain of k distinct values in n slots, we pick which
k slots hold distinct values: C(n-1, k-1). For value v with prime factorization
p1^a1 * ... * pm^am, the number of distinct increasing chains ending at v
is product of ways to split each exponent. A chain of length k means k-1
multiplications total, where for prime pi we do ai multiplications. The number
of orderings is multinomial. But actually each chain gives a unique sequence
of distinct values, so we use:

For value v = p1^a1 * p2^a2 * ..., the number of ways to form an ideal
array of length n ending at v is: product over each prime pi of C(n-1, ai).

This comes from: each prime's exponent increases ai times across n-1 gaps,
choosing which gaps.

Wait, C(n-1, ai) only works if ai <= n-1. And each prime's gaps are chosen
independently. The total is product of C(n-1, ai) for each prime factor.

Time: O(maxValue * log(maxValue) + maxValue * num_primes)  Space: O(maxValue)
---
"""

from math import comb


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # Precompute smallest prime factor
        spf = list(range(maxValue + 1))
        for i in range(2, int(maxValue**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Precompute C(n-1, k) for small k (max exponent ~ 14 for 2^14 = 16384)
        max_exp = 14
        c = [0] * (max_exp + 1)
        for k in range(max_exp + 1):
            c[k] = comb(n - 1 + k, k)  # C(n-1+k, k) = stars and bars

        # Wait, let me reconsider. For a prime with exponent e in value v,
        # we need to distribute e "increment steps" across n-1 gaps between
        # n positions. This is C(n-1+e-1, e) = C(n+e-2, e).
        # No: the distinct values form an increasing chain. If chain length is L,
        # we choose L positions out of n (with order preserved): C(n-1, L-1).
        # But chain structure and position selection are interleaved.
        #
        # The standard result: for ideal array of length n with last element v
        # having prime factorization p1^a1 * ... * pm^am:
        # Count = product of C(n-1+ai-1, ai) ... no.
        #
        # Actually it's C(n-1, ai) because we're choosing which of n-1 transitions
        # to "use" for each prime independently, but each transition can handle
        # multiple primes simultaneously.
        #
        # No wait. Let me think again. Stars and bars: distributing ai identical
        # balls into n-1 gaps (each gap can get 0 or more) = C(n-1+ai-1, ai) = C(n+ai-2, ai).
        # But that allows a gap to have multiplied by p^2 in one step.
        # Since arr[i] | arr[i+1], that's fine - we CAN multiply by p^2 in one step.
        # So each prime's exponent is distributed among n-1 transitions independently.
        # = C(n-1+ai-1, ai) = C(n+ai-2, ai)

        # Recompute c
        c = [0] * (max_exp + 1)
        for k in range(max_exp + 1):
            c[k] = comb(n - 1 + k, k) % MOD  # C(n-1+k, k)

        ans = 0
        for v in range(1, maxValue + 1):
            # Factorize v
            ways = 1
            tmp = v
            while tmp > 1:
                p = spf[tmp]
                e = 0
                while tmp % p == 0:
                    tmp //= p
                    e += 1
                ways = (ways * c[e]) % MOD
            ans = (ans + ways) % MOD

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.idealArrays(2, 5) == 10
    assert sol.idealArrays(5, 3) == 11
    assert sol.idealArrays(1, 1) == 1

    print("all tests passed")
