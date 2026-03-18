"""
2320. Count Number of Ways to Place Houses
https://leetcode.com/problems/count-number-of-ways-to-place-houses/

Pattern: 01 - Fibonacci Pattern

---
APPROACH: Each side of the street is independent.
For one side with n plots, the number of valid arrangements (no two
adjacent houses) follows the Fibonacci recurrence:
  f(1) = 2 (place or skip), f(2) = 3
  f(i) = f(i-1) + f(i-2)
This gives f(n) = fib(n+2) arrangements per side.
Since the two sides are independent, answer = f(n)^2 mod 10^9+7.

Time: O(n)  Space: O(1)
---
"""

MOD = 10**9 + 7


class Solution:
    def countHousePlacements(self, n: int) -> int:
        """Return the number of valid house placement configs mod 10^9+7."""
        # f(i) = ways to arrange one side of length i
        # f(1) = 2, f(2) = 3, f(i) = f(i-1) + f(i-2)
        if n == 1:
            return 4  # 2^2

        prev2, prev1 = 2, 3
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, (prev2 + prev1) % MOD

        return (prev1 * prev1) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: n=1 -> 4 (each side: house or empty = 2, 2*2=4)
    assert sol.countHousePlacements(1) == 4
    # Example 2: n=2 -> 9 (each side: 3 ways, 3*3=9)
    assert sol.countHousePlacements(2) == 9
    # n=3: each side has 5 ways (fib pattern), 5*5=25
    assert sol.countHousePlacements(3) == 25
    # n=4: each side has 8 ways, 8*8=64
    assert sol.countHousePlacements(4) == 64
    # Large n should not overflow (mod applied)
    assert sol.countHousePlacements(1000) > 0

    print("all tests passed")
