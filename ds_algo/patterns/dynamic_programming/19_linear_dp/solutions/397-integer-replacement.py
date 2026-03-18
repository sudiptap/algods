"""
397. Integer Replacement (Medium)

Given a positive integer n, return the minimum number of operations to
reduce it to 1. Operations:
    - If n is even : n -> n / 2
    - If n is odd  : n -> n + 1  OR  n -> n - 1

Approach - Greedy with bit manipulation:
    Even: always halve.
    Odd:  look at the lowest two bits.
        - If (n & 3) == 3 and n != 3: prefer n + 1
          (makes the last two bits 00, enabling two halvings).
        - Otherwise: prefer n - 1.
    Special case: n == 3 -> prefer n - 1 (3 -> 2 -> 1 = 2 steps,
                  vs 3 -> 4 -> 2 -> 1 = 3 steps).

    Time : O(log n)
    Space: O(1)

Also shown: memoized recursion variant.

Example:
    8 -> 4 -> 2 -> 1  =>  3 operations
    7 -> 8 -> 4 -> 2 -> 1  =>  4 operations
"""

from functools import lru_cache


class Solution:
    def integerReplacement(self, n: int) -> int:
        """Greedy bit-manipulation: O(log n) time, O(1) space."""
        ops = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n == 3 or (n & 3) == 1:
                n -= 1
            else:
                n += 1
            ops += 1
        return ops

    def integerReplacementMemo(self, n: int) -> int:
        """Memoized recursion variant: O(log n) time and space."""
        @lru_cache(maxsize=None)
        def dp(x: int) -> int:
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + dp(x // 2)
            return 1 + min(dp(x + 1), dp(x - 1))

        return dp(n)


# ---- Tests ----
def test():
    sol = Solution()

    # Greedy tests
    assert sol.integerReplacement(8) == 3
    assert sol.integerReplacement(7) == 4
    assert sol.integerReplacement(1) == 0
    assert sol.integerReplacement(2) == 1
    assert sol.integerReplacement(3) == 2
    assert sol.integerReplacement(4) == 2
    assert sol.integerReplacement(15) == 5  # 15->16->8->4->2->1
    assert sol.integerReplacement(65535) == 17
    assert sol.integerReplacement(100000000) == 31

    # Memo tests - cross-check with greedy
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 42, 100, 1000, 65535]:
        assert sol.integerReplacement(n) == sol.integerReplacementMemo(n), \
            f"Mismatch at n={n}"

    print("All tests passed!")


if __name__ == "__main__":
    test()
