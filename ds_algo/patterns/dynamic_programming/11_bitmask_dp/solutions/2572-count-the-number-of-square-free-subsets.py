"""
2572. Count the Number of Square-Free Subsets
https://leetcode.com/problems/count-the-number-of-square-free-subsets/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP on prime factor masks
- Primes up to 30: [2,3,5,7,11,13,17,19,23,29] (10 primes).
- Each number's prime factorization is a bitmask. If any prime appears >= 2 times
  in a number, that number is not square-free (skip it).
- dp[mask] = number of subsets where the product's prime factors match mask.
- For each number, if its prime mask doesn't overlap with current mask, we can add it.

Time: O(n * 2^10)  Space: O(2^10)
---
"""

from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_mask(x):
            """Return prime factor bitmask, or -1 if not square-free."""
            mask = 0
            for i, p in enumerate(primes):
                if x % p == 0:
                    x //= p
                    if x % p == 0:
                        return -1  # p^2 divides original number
                    mask |= (1 << i)
            return mask

        dp = [0] * (1 << 10)
        dp[0] = 1  # empty subset

        for num in nums:
            if num == 1:
                # 1 can be added to any subset without affecting square-freeness
                # doubles the count (include or exclude this 1)
                # Handle specially to avoid issues
                pass
            mask = get_mask(num)
            if mask == -1:
                continue
            if num == 1:
                # 1 has mask 0, can pair with anything
                for m in range(len(dp) - 1, -1, -1):
                    dp[m] = (dp[m] + dp[m]) % MOD
                continue
            # Standard knapsack
            for m in range((1 << 10) - 1, -1, -1):
                if m & mask == mask:
                    dp[m] = (dp[m] + dp[m ^ mask]) % MOD

        return (sum(dp) - 1) % MOD  # subtract empty subset


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.squareFreeSubsets([3, 4, 4, 5]) == 3
    assert sol.squareFreeSubsets([1]) == 1
    assert sol.squareFreeSubsets([26, 6, 4, 27]) == 2  # {26}, {6}; 4=2^2 and 27=3^3 invalid

    print("all tests passed")
