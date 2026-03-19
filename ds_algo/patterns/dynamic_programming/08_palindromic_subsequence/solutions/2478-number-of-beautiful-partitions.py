"""
2478. Number of Beautiful Partitions
https://leetcode.com/problems/number-of-beautiful-partitions/

Pattern: 08 - Palindromic Subsequence (Partitioning DP)

---
APPROACH: dp[i][j] = ways to partition s[:i] into j parts
- Each part must start with a prime digit and end with a non-prime digit.
- Each part has length >= minLength.
- Prime digits: 2, 3, 5, 7. Non-prime: 1, 4, 6, 8, 9, 0.
- dp[i][j] = sum of dp[m][j-1] for valid split points m.
- Use prefix sums to speed up.

Time: O(n * k)  Space: O(n * k)
---
"""


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        primes = {'2', '3', '5', '7'}

        # First char must be prime, last char must be non-prime
        if s[0] not in primes or s[-1] in primes:
            return 0

        # Valid split points: positions where we can start a new partition
        # A split at position i means s[i] starts a new part, s[i-1] ends previous
        # s[i] must be prime, s[i-1] must be non-prime

        # dp[j][i] = ways to split s[:i] into j parts
        # Use 1D with parts iteration
        # dp[i] = ways to partition s[:i] into current number of parts
        prev = [0] * (n + 1)
        # Base: 0 parts for empty prefix
        prev[0] = 1

        for part in range(1, k + 1):
            cur = [0] * (n + 1)
            prefix = 0
            for i in range(part * minLength, n + 1):
                # Check if position i-minLength is a valid start for prefix sum
                j = i - minLength
                if j >= 0:
                    # j is a valid split point if s[j] is prime (start of new part)
                    # and (j == 0 or s[j-1] is non-prime)
                    if (j == 0 or s[j - 1] not in primes) and (j == 0 or part > 1 or j == 0):
                        if s[j] in primes or j == 0:
                            pass
                    # More carefully:
                    # prev[j] contributes if position j is a valid boundary:
                    # s[j] must be prime (new part starts here)
                    # and j == 0 (first part) or s[j-1] is non-prime (previous part ends)
                    if j == 0:
                        prefix = (prefix + prev[j]) % MOD
                    elif s[j] in primes and s[j - 1] not in primes:
                        prefix = (prefix + prev[j]) % MOD

                # Current position i: s[i-1] must be non-prime (end of part)
                if s[i - 1] not in primes:
                    cur[i] = prefix

            prev = cur

        return prev[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.beautifulPartitions("23542185131", 3, 2) == 3
    assert sol.beautifulPartitions("23542185131", 3, 3) == 1
    assert sol.beautifulPartitions("3312958", 3, 1) == 1
    assert sol.beautifulPartitions("1", 1, 1) == 0

    print("all tests passed")
