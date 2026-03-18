"""
313. Super Ugly Number (Medium)
https://leetcode.com/problems/super-ugly-number/

A super ugly number is a positive integer whose prime factors are in the given
list of primes. Given an integer n and a list of primes, return the nth super
ugly number. 1 is by convention a super ugly number.

Pattern: Linear DP (multi-pointer, generalization of Ugly Number II #264)
- Maintain one pointer per prime, all starting at index 0.
- dp[i] = ith super ugly number. dp[0] = 1.
- At each step, dp[i] = min(dp[ptr[j]] * primes[j]) over all j.
- Advance all pointers whose candidate equals dp[i] (avoids duplicates).

Time:  O(n * k) where k = len(primes)
Space: O(n + k)
"""

from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """Return the nth super ugly number.

        Args:
            n: Which super ugly number to return, 1-indexed.
            primes: Sorted list of prime factors allowed.

        Returns:
            The nth super ugly number.
        """
        k = len(primes)
        dp = [0] * n
        dp[0] = 1
        ptrs = [0] * k  # one pointer per prime

        for i in range(1, n):
            # Compute candidate for each prime
            candidates = [dp[ptrs[j]] * primes[j] for j in range(k)]
            dp[i] = min(candidates)
            # Advance all pointers that produced the minimum (skip duplicates)
            for j in range(k):
                if candidates[j] == dp[i]:
                    ptrs[j] += 1

        return dp[n - 1]


# ---------- tests ----------
def test_super_ugly_number():
    sol = Solution()

    # Example 1
    assert sol.nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32

    # First super ugly number is always 1
    assert sol.nthSuperUglyNumber(1, [2, 3, 5]) == 1

    # Classic ugly numbers (primes = [2,3,5]), 10th = 12
    assert sol.nthSuperUglyNumber(10, [2, 3, 5]) == 12

    # Single prime [2]: powers of 2
    assert sol.nthSuperUglyNumber(5, [2]) == 16  # 1,2,4,8,16

    # Two primes [2,3]: sequence 1, 2, 3, 4, 6, 8 -> 6th is 8
    assert sol.nthSuperUglyNumber(6, [2, 3]) == 8

    print("All tests passed for 313. Super Ugly Number")


if __name__ == "__main__":
    test_super_ugly_number()
