"""
650. 2 Keys Keyboard (Medium)
https://leetcode.com/problems/2-keys-keyboard/

Initially a notepad has one character 'A'. You can perform two operations:
  - Copy All: copy all characters on the notepad.
  - Paste: paste the last copied characters.
Given n, return the minimum number of operations to get exactly n 'A's.

Approach - Prime Factorization:
    The minimum operations for n equals the sum of its prime factors.
    If n = p1 * p2 * ... * pk, answer = p1 + p2 + ... + pk.

    Intuition: to produce p copies from 1 copy, you need 1 Copy All +
    (p-1) Pastes = p operations. Chaining factors is optimal because
    dp[n] = dp[n/p] + p for the smallest prime factor p of n.

Time:  O(sqrt(n)) for prime factorization
Space: O(1)
"""


class Solution:
    def minSteps(self, n: int) -> int:
        """Return the minimum operations to get n 'A's on the notepad.

        Decomposes n into prime factors and sums them. Each prime factor p
        contributes exactly p operations (1 copy + p-1 pastes).

        Args:
            n: Target number of 'A's, 1 <= n <= 1000.

        Returns:
            Minimum number of Copy All and Paste operations.
        """
        if n == 1:
            return 0

        steps = 0
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                steps += divisor
                n //= divisor
            divisor += 1

        return steps

    def minSteps_dp(self, n: int) -> int:
        """Bottom-up DP approach for reference.

        dp[i] = min operations to get i 'A's.
        For each i, try all divisors: dp[i] = min(dp[i/d] + d).

        Args:
            n: Target number of 'A's.

        Returns:
            Minimum number of operations.
        """
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = i  # Worst case: all pastes from a single 'A'
            d = 2
            while d * d <= i:
                if i % d == 0:
                    dp[i] = min(dp[i], dp[d] + i // d, dp[i // d] + d)
                d += 1

        return dp[n]


# --- Tests ---

def test_example1():
    sol = Solution()
    assert sol.minSteps(3) == 3  # Copy All, Paste, Paste

def test_example2():
    sol = Solution()
    assert sol.minSteps(1) == 0  # Already have one 'A'

def test_prime():
    sol = Solution()
    assert sol.minSteps(7) == 7  # Prime: must paste 7 times from 1

def test_power_of_two():
    sol = Solution()
    assert sol.minSteps(8) == 6  # 2+2+2 = 6

def test_composite():
    sol = Solution()
    assert sol.minSteps(12) == 7  # 12 = 2*2*3 -> 2+2+3 = 7

def test_large():
    sol = Solution()
    assert sol.minSteps(100) == 14  # 100 = 2*2*5*5 -> 2+2+5+5 = 14

def test_dp_matches_factorization():
    sol = Solution()
    for n in range(1, 101):
        assert sol.minSteps(n) == sol.minSteps_dp(n), f"Mismatch at n={n}"


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_prime()
    test_power_of_two()
    test_composite()
    test_large()
    test_dp_matches_factorization()
    print("All tests passed!")
