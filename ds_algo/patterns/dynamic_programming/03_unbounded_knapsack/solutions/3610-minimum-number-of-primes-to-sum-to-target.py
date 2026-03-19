"""
3610. Minimum Number of Primes to Sum to Target
https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

Pattern: 03 - Unbounded Knapsack

---
APPROACH: Sieve + coin change (unbounded knapsack)
- Generate all primes up to target using Sieve of Eratosthenes.
- Treat primes as coin denominations.
- Find minimum number of primes that sum to target (coins can be reused).
- Classic unbounded knapsack / coin change.

Time: O(target * sqrt(target))  Space: O(target)
---
"""


class Solution:
    def minPrimes(self, target: int) -> int:
        if target < 2:
            return -1

        # Sieve of Eratosthenes
        is_prime = [True] * (target + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(target**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, target + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(2, target + 1) if is_prime[i]]

        # Coin change
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for i in range(1, target + 1):
            for p in primes:
                if p > i:
                    break
                if dp[i - p] + 1 < dp[i]:
                    dp[i] = dp[i - p] + 1

        return dp[target] if dp[target] != float('inf') else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minPrimes(5) == 1  # 5 itself
    assert sol.minPrimes(4) == 2  # 2+2
    assert sol.minPrimes(10) == 2  # 5+5 or 3+7
    assert sol.minPrimes(1) == -1
    assert sol.minPrimes(2) == 1
    assert sol.minPrimes(9) == 2  # 2+7

    print("All tests passed!")
