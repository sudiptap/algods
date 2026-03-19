"""
3725. Count Ways to Choose Coprime Integers from Rows
https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

Pattern: 11 - Bitmask DP

---
APPROACH: DP on bitmask of prime factors
- Choose one integer per row such that GCD of all chosen = 1.
- Values up to 150, so primes up to 150: there are 35 such primes.
  But bitmask of 35 is too large.
- Use Mobius function + inclusion-exclusion:
  For each divisor d, count ways where d divides all chosen values.
  Then apply Mobius inversion: answer = sum over d of mu(d) * f(d)
  where f(d) = product over rows of (count of elements divisible by d).

Time: O(D * m * n) where D = max value = 150
Space: O(D)
---
"""

from typing import List


class Solution:
    def countWays(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 150

        # Compute Mobius function for values 1..MAX_VAL
        mu = [0] * (MAX_VAL + 1)
        mu[1] = 1
        primes = []
        is_prime = [True] * (MAX_VAL + 1)

        for i in range(2, MAX_VAL + 1):
            if is_prime[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > MAX_VAL:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]

        m = len(mat)

        # For each d with mu(d) != 0, compute product of counts
        ans = 0
        for d in range(1, MAX_VAL + 1):
            if mu[d] == 0:
                continue

            product = 1
            for row in mat:
                cnt = sum(1 for v in row if v % d == 0)
                product = product * cnt % MOD
                if product == 0:
                    break

            ans = (ans + mu[d] * product) % MOD

        return ans % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countWays([[1, 2], [3, 4]]) == 3   # (1,3),(1,4),(2,3)
    assert sol.countWays([[2, 2], [2, 2]]) == 0
    assert sol.countWays([[1], [1]]) == 1
    assert sol.countWays([[6, 10, 15], [7, 11, 13]]) == 9  # all coprime to any

    print("all tests passed")
