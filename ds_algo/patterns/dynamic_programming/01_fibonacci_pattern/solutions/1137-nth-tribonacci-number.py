"""
1137. N-th Tribonacci Number (Easy)
https://leetcode.com/problems/n-th-tribonacci-number/

Pattern: 01 - Fibonacci Pattern

T(0) = 0, T(1) = 1, T(2) = 1.
T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3.

Approach:
    Iteratively compute using three variables (a, b, c).
    Roll forward each step.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        """Return the n-th Tribonacci number."""
        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


# ───────────────────────── tests ─────────────────────────

def test_zero():
    assert Solution().tribonacci(0) == 0

def test_one():
    assert Solution().tribonacci(1) == 1

def test_two():
    assert Solution().tribonacci(2) == 1

def test_four():
    assert Solution().tribonacci(4) == 4

def test_twenty_five():
    assert Solution().tribonacci(25) == 1389537

def test_thirty_seven():
    assert Solution().tribonacci(37) == 2082876103


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
