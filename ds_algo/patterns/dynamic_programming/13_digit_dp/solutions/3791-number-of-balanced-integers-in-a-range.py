"""
3791. Number of Balanced Integers in a Range
https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP tracking odd/even position digit sums
- Balanced: at least 2 digits AND sum of digits at odd positions ==
  sum at even positions (leftmost digit is position 1).
- f(n) = count of balanced integers in [1, n]. Answer = f(high) - f(low-1).
- State: (pos, diff, tight, started, num_digits_so_far)
  - diff = sum_odd_pos - sum_even_pos
  - Need to track how many real digits placed (to know parity of next position).

Time: O(d^2 * D * 10)  Space: O(d^2 * D)
where d = digits of n (~16), D = max possible diff (~9*8=72 per side)
---
"""

from functools import lru_cache


class Solution:
    def countBalancedIntegers(self, low: int, high: int) -> int:
        def count(n):
            if n <= 0:
                return 0
            s = str(n)
            L = len(s)

            @lru_cache(maxsize=None)
            def dp(pos, diff, tight, started, placed):
                """
                pos: current position in string
                diff: sum_odd - sum_even (shifted by 150 to avoid negative keys)
                tight: whether constrained by upper bound
                started: whether we've placed a non-zero digit
                placed: number of digits placed so far
                """
                if pos == L:
                    if not started:
                        return 0
                    if placed < 2:
                        return 0
                    return 1 if diff == 0 else 0

                limit = int(s[pos]) if tight else 9
                result = 0

                for d in range(0, limit + 1):
                    new_tight = tight and d == limit

                    if not started and d == 0:
                        result += dp(pos + 1, 0, new_tight, False, 0)
                    else:
                        new_placed = placed + 1
                        # Position new_placed: 1-indexed. Odd or even?
                        # We don't know total digits yet, so track placed count.
                        # Position within the number is new_placed.
                        # Odd position (1, 3, 5, ...): add d to odd sum
                        # Even position (2, 4, 6, ...): add d to even sum
                        if new_placed % 2 == 1:  # odd position
                            new_diff = diff + d
                        else:  # even position
                            new_diff = diff - d

                        result += dp(pos + 1, new_diff, new_tight, True, new_placed)

                return result

            ans = dp(0, 0, True, False, 0)
            dp.cache_clear()
            return ans

        return count(high) - count(low - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countBalancedIntegers(1, 100) == 9  # 11,22,...,99
    assert sol.countBalancedIntegers(120, 129) == 1  # only 121
    assert sol.countBalancedIntegers(1234, 1234) == 0

    # Cross-validate
    def brute(lo, hi):
        cnt = 0
        for x in range(lo, hi + 1):
            d = [int(c) for c in str(x)]
            if len(d) < 2:
                continue
            odd_sum = sum(d[i] for i in range(0, len(d), 2))
            even_sum = sum(d[i] for i in range(1, len(d), 2))
            if odd_sum == even_sum:
                cnt += 1
        return cnt

    for lo in [1, 10, 50, 100]:
        for hi in [lo + 50, lo + 200]:
            assert sol.countBalancedIntegers(lo, hi) == brute(lo, hi), \
                f"Failed for ({lo},{hi}): got {sol.countBalancedIntegers(lo,hi)}, expected {brute(lo,hi)}"

    print("all tests passed")
