"""
509. Fibonacci Number (Easy)
https://leetcode.com/problems/fibonacci-number/

Pattern: Fibonacci Pattern

F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.

Approach:
    Iteratively compute fib using two variables (prev, curr).
    O(1) space, O(n) time.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def fib(self, n: int) -> int:
        """Return the n-th Fibonacci number."""
        if n <= 1:
            return n

        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr


# ───────────────────────── tests ─────────────────────────

def test_zero():
    assert Solution().fib(0) == 0

def test_one():
    assert Solution().fib(1) == 1

def test_two():
    assert Solution().fib(2) == 1

def test_three():
    assert Solution().fib(3) == 2

def test_four():
    assert Solution().fib(4) == 3

def test_ten():
    assert Solution().fib(10) == 55

def test_twenty():
    assert Solution().fib(20) == 6765

def test_thirty():
    assert Solution().fib(30) == 832040


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
