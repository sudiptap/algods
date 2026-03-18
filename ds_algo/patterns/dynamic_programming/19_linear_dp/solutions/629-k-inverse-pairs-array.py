"""
629. K Inverse Pairs Array
https://leetcode.com/problems/k-inverse-pairs-array/

Pattern: 19 - Linear DP

---
APPROACH: DP with prefix sum optimisation
- dp[i][j] = number of arrays of [1..i] with exactly j inverse pairs.
- When inserting element i into an array of [1..i-1], placing it at position p
  (0-indexed from the right) creates exactly p new inverse pairs.
  p ranges from 0 to i-1.
- Naive recurrence: dp[i][j] = sum(dp[i-1][j-p] for p in 0..min(j, i-1))
- With prefix sums: dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]
  (sliding window of width i over previous row).
- Base: dp[0][0] = 1 (empty array, 0 inverse pairs).

Time: O(n * k)   Space: O(k)
---
"""

MOD = 10**9 + 7


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """Return the number of arrays of [1..n] with exactly k inverse pairs, mod 10^9+7."""
        # dp[j] = number of permutations of [1..current_n] with j inverse pairs
        dp = [0] * (k + 1)
        dp[0] = 1  # base: one permutation of [] with 0 inverse pairs

        for i in range(1, n + 1):
            # Build prefix sum of current dp row for sliding window
            new_dp = [0] * (k + 1)
            prefix = [0] * (k + 2)
            for j in range(k + 1):
                prefix[j + 1] = (prefix[j] + dp[j]) % MOD

            for j in range(k + 1):
                # sum of dp[j-p] for p in 0..min(j, i-1)
                # = prefix[j+1] - prefix[max(0, j-i+1)]
                lo = max(0, j - i + 1)
                new_dp[j] = (prefix[j + 1] - prefix[lo]) % MOD

            dp = new_dp

        return dp[k]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.kInversePairs(3, 0) == 1
    assert sol.kInversePairs(3, 1) == 2
    assert sol.kInversePairs(3, 3) == 1    # [3,2,1] only
    assert sol.kInversePairs(3, 4) == 0    # max inverse pairs for n=3 is 3
    assert sol.kInversePairs(1, 0) == 1
    assert sol.kInversePairs(1000, 1000) == 663677020

    print("all tests passed")
