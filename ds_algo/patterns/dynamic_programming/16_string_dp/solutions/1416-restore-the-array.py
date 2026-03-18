"""
1416. Restore The Array (Hard)
https://leetcode.com/problems/restore-the-array/

Pattern: String DP

Given a string s of digits and an integer k, find the number of ways to
partition s into a sequence of integers in [1, k] with no leading zeros.
Return the answer modulo 10^9 + 7.

Approach:
    dp[i] = number of ways to decode s[:i].
    dp[0] = 1 (empty prefix = one way).

    For each position i, try all ending positions j (j > i) such that
    s[i:j] forms a valid number in [1, k]:
      - s[i] != '0'  (no leading zeros)
      - int(s[i:j]) <= k
    Then dp[j] += dp[i].

    We break early when the number exceeds k.

Time:  O(n * log k)  — inner loop runs at most O(log10(k)) digits.
Space: O(n)
"""

MOD = 10**9 + 7


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """Return the number of ways to partition s into numbers in [1, k]."""
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            if s[i] == '0':
                continue  # no leading zeros
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                dp[j + 1] = (dp[j + 1] + dp[i]) % MOD

        return dp[n]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().numberOfArrays("1000", 10000) == 1

def test_example2():
    assert Solution().numberOfArrays("1000", 10) == 0

def test_example3():
    assert Solution().numberOfArrays("1317", 2000) == 8

def test_single_digit():
    assert Solution().numberOfArrays("5", 10) == 1

def test_leading_zeros():
    assert Solution().numberOfArrays("10", 10) == 1

def test_all_ones():
    assert Solution().numberOfArrays("111", 11) == 3  # [1,1,1], [1,11], [11,1]

def test_large_k():
    assert Solution().numberOfArrays("12345", 100000) == 16


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
