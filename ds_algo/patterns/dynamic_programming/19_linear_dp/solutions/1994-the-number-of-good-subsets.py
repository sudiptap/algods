"""
1994. The Number of Good Subsets (Hard)
https://leetcode.com/problems/the-number-of-good-subsets/

A good subset has product with each prime factor appearing exactly once.
Return number of non-empty good subsets mod 10^9+7. Elements 1-30.

Pattern: Linear DP (Bitmask on Prime Factors)
Approach:
- Primes up to 30: [2,3,5,7,11,13,17,19,23,29] (10 primes).
- Numbers with repeated prime factors (4,8,9,12,16,18,20,24,25,27,28) are excluded.
- For valid numbers, represent prime factorization as a bitmask.
- dp[mask] = number of subsets whose product has prime factors = mask.
- For each valid number with factor mask m, for each existing dp state s
  where s & m == 0: dp[s | m] += dp[s] * count[number].
- 1s can be included or not: multiply answer by 2^count[1].
- Answer = sum(dp[mask] for mask > 0) * 2^count[1].

Time:  O(30 * 2^10)
Space: O(2^10)
"""

from typing import List
from collections import Counter


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        """Return number of good subsets mod 10^9+7.

        Args:
            nums: Array of integers 1-30.

        Returns:
            Count of good subsets.
        """
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_idx = {p: i for i, p in enumerate(primes)}

        def get_mask(n):
            mask = 0
            for i, p in enumerate(primes):
                if n % p == 0:
                    n //= p
                    if n % p == 0:
                        return -1  # repeated prime factor
                    mask |= (1 << i)
            return mask

        cnt = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in range(2, 31):
            if cnt[num] == 0:
                continue
            mask = get_mask(num)
            if mask == -1:
                continue
            # Iterate dp in reverse to avoid using same number twice
            # But we have cnt[num] copies; each copy is a separate choice
            # Since product must have each prime once, we can use at most 1
            # copy of each number. But multiple copies means cnt[num] choices.
            for s in range(len(dp) - 1, -1, -1):
                if dp[s] and (s & mask) == 0:
                    dp[s | mask] = (dp[s | mask] + dp[s] * cnt[num]) % MOD

        # Sum all non-zero masks, multiply by 2^count[1]
        total = sum(dp[1:]) % MOD
        total = total * pow(2, cnt[1], MOD) % MOD
        return total


# ---------- tests ----------
def test_good_subsets():
    sol = Solution()

    # Example 1: [1,2,3,4] -> good subsets: {2},{3},{2,3},{1,2},{1,3},{1,2,3} = 6
    assert sol.numberOfGoodSubsets([1, 2, 3, 4]) == 6

    # Example 2: [4,2,3,15] -> {2},{3},{15},{2,3},{2,15},{3,15}...
    # 15=3*5. {2},{3},{15},{2,15},{3,5->not present}
    # Actually: 2(mask=01), 3(mask=10), 15(mask=0110)=3*5
    # {2}=1, {3}=1, {15}=1, {2,3}=1, {2,15}=1 -> 5
    assert sol.numberOfGoodSubsets([4, 2, 3, 15]) == 5

    # All 1s
    assert sol.numberOfGoodSubsets([1, 1, 1]) == 0

    # Single prime
    assert sol.numberOfGoodSubsets([2]) == 1

    print("All tests passed for 1994. The Number of Good Subsets")


if __name__ == "__main__":
    test_good_subsets()
