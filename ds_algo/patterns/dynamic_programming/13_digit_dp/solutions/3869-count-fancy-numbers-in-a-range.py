"""
3869. Count Fancy Numbers in a Range
https://leetcode.com/problems/count-fancy-numbers-in-a-range/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP with digit frequency tracking
- "Good" number: digits are strictly increasing or strictly decreasing.
  Single-digit numbers are good.
- "Fancy" number: the number itself is good, OR the digit sum is good.
- Count fancy numbers in [l, r].
- f(n) = count of fancy in [1, n]. Answer = f(r) - f(l-1).
- For each number, check if it's good (strictly mono digits) OR its
  digit sum is good.
- Digit sum is at most 9*16 = 144, which is a 3-digit number.
  Check if 144's digits are strictly monotone: 1,4,4 -> no.
- A number with digit sum s is "fancy" if s is good. s is good if
  s's digits are strictly increasing or decreasing. For s <= 144:
  good sums include all single digit (1-9), and two-digit strictly
  increasing (12,13,...,19,23,...,89) and strictly decreasing (10,21,...,98).

- Digit DP state: (pos, tight, started, is_increasing, is_decreasing,
  last_digit, digit_sum)
  Track whether the number itself is good (mono) and the digit sum.

Time: O(d * 10 * 2 * 2 * 2 * 10 * S) where S = max digit sum
Space: O(d * 10 * 2 * 2 * S)
---
"""

from functools import lru_cache


def is_good(x):
    """Check if x's digits are strictly increasing or strictly decreasing."""
    if x < 10:
        return True
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    digits.reverse()
    inc = all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))
    dec = all(digits[i] > digits[i + 1] for i in range(len(digits) - 1))
    return inc or dec


class Solution:
    def countFancyNumbers(self, l: int, r: int) -> int:
        def count(n):
            if n <= 0:
                return 0
            s = str(n)
            L = len(s)

            @lru_cache(maxsize=None)
            def dp(pos, tight, started, last, mono_inc, mono_dec, dsum):
                """
                Returns count of fancy numbers.
                mono_inc: whether all digits so far are strictly increasing
                mono_dec: whether all digits so far are strictly decreasing
                last: last digit placed (-1 if none)
                dsum: sum of digits so far
                """
                if pos == L:
                    if not started:
                        return 0
                    # Number is fancy if good (mono) or digit sum is good
                    num_is_good = mono_inc or mono_dec
                    sum_is_good = is_good(dsum) if dsum > 0 else False
                    return 1 if (num_is_good or sum_is_good) else 0

                limit = int(s[pos]) if tight else 9
                result = 0

                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        result += dp(pos + 1, new_tight, False, -1, True, True, 0)
                    else:
                        if not started or last == -1:
                            # First digit
                            result += dp(pos + 1, new_tight, True, d, True, True, d)
                        else:
                            new_inc = mono_inc and (d > last)
                            new_dec = mono_dec and (d < last)
                            result += dp(pos + 1, new_tight, True, d, new_inc, new_dec, dsum + d)

                return result

            ans = dp(0, True, False, -1, True, True, 0)
            dp.cache_clear()
            return ans

        return count(r) - count(l - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countFancyNumbers(8, 10) == 3
    assert sol.countFancyNumbers(1, 9) == 9  # all single digits are good

    # Cross-validate with brute force
    def brute(l, r):
        cnt = 0
        for x in range(l, r + 1):
            digits = [int(c) for c in str(x)]
            inc = all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))
            dec = all(digits[i] > digits[i + 1] for i in range(len(digits) - 1))
            num_good = inc or dec
            s = sum(digits)
            s_digits = [int(c) for c in str(s)]
            s_inc = all(s_digits[i] < s_digits[i + 1] for i in range(len(s_digits) - 1))
            s_dec = all(s_digits[i] > s_digits[i + 1] for i in range(len(s_digits) - 1))
            sum_good = s_inc or s_dec
            if num_good or sum_good:
                cnt += 1
        return cnt

    for l in range(1, 100):
        for r in range(l, min(l + 20, 200)):
            assert sol.countFancyNumbers(l, r) == brute(l, r), \
                f"Failed for ({l},{r}): got {sol.countFancyNumbers(l,r)}, expected {brute(l,r)}"

    print("all tests passed")
