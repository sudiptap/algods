"""
3704. Count No-Zero Pairs That Sum to N
https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

Pattern: 15 - Counting / Combinatorial (Digit DP)

---
APPROACH: Digit DP from LSD
- Count ordered pairs (a, b) of positive integers with a+b=n,
  where neither a nor b contains the digit 0.
- Process from least significant digit. At each position, choose
  da (digit of a) and db (digit of b) both in 1..9 such that
  da + db + carry_in ≡ n_digit (mod 10).
- Track carry and how many digit positions we've processed.
- The key insight: both a and b have exactly as many digits as needed
  (no leading zeros). A number like 15 has digits [5,1] from LSD.
  We process all positions and the carry must be 0 at the end.
  The pair is valid as long as every digit of both numbers is 1-9.
  But a and b may have different lengths than n. To handle this:
  numbers shorter than n have implicit 0s in higher positions, but
  those aren't "digits" of the number. So we track whether a/b are
  still "alive" (haven't ended yet) - meaning they contribute 1-9,
  or have ended (contribute 0 from here on).

Time: O(d * 2 * 81) ≈ O(d * 162)  Space: O(d * 2)
where d = number of digits of n (≤ 16 for n ≤ 10^15)
---
"""

from functools import lru_cache


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = []
        tmp = n
        while tmp:
            digits.append(tmp % 10)
            tmp //= 10
        m = len(digits)

        # We need to count pairs (a, b) with a+b=n, no zero digits in either.
        # From LSD, each digit position must satisfy:
        #   da + db + carry_in = digits[pos] + 10 * carry_out
        # da, db are in {1..9} IF that digit position is part of the number,
        # or 0 if the number has already ended (fewer digits).
        #
        # Key: a number "ends" at the highest non-zero digit. Once ended,
        # all higher positions contribute 0. The number must have at least
        # one digit (the units digit), so it's always alive at pos=0.
        #
        # Enumerate from LSD. State: (pos, carry).
        # At each position, try all valid (da, db) combos.
        # da can be 0 (a ended before this position) or 1-9 (a has a digit here).
        # But if da=0 at this position, a must also have da=0 at all higher positions.
        # Similarly for db.
        # So we need to track whether a and b are still active.
        # State: (pos, carry, a_active, b_active)
        # At pos=0, both are active (both have at least one digit since both >= 1).

        @lru_cache(maxsize=None)
        def dp(pos, carry, a_active, b_active):
            if pos == m:
                # Must have zero carry, and both a and b must have been
                # at least 1 digit (guaranteed since both start active at pos 0)
                return 1 if carry == 0 else 0

            target = digits[pos]
            count = 0

            # Determine ranges for da and db
            # If active: digit is 1-9 (this IS a digit of the number)
            #   But the number might end here (this is the MSB), meaning
            #   at the next position da=0. We handle that by transitioning
            #   a_active to False at next position.
            #   OR the number continues, a_active stays True.
            # If not active: da=0, stays not active.
            if a_active:
                da_vals = range(1, 10)
            else:
                da_vals = [0]

            if b_active:
                db_vals = range(1, 10)
            else:
                db_vals = [0]

            for da in da_vals:
                for db in db_vals:
                    s = da + db + carry
                    if s % 10 != target:
                        continue
                    new_carry = s // 10

                    # Decide if a and b stay active at next position
                    if a_active and b_active:
                        # a can stay active or end, b can stay active or end
                        # But if pos+1 == m, both must end (no more digits of n)
                        # Actually at pos+1 == m, dp returns based on carry only
                        for na in ([True, False] if pos + 1 < m else [False]):
                            for nb in ([True, False] if pos + 1 < m else [False]):
                                count += dp(pos + 1, new_carry, na, nb)
                    elif a_active:
                        for na in ([True, False] if pos + 1 < m else [False]):
                            count += dp(pos + 1, new_carry, na, False)
                    elif b_active:
                        for nb in ([True, False] if pos + 1 < m else [False]):
                            count += dp(pos + 1, new_carry, False, nb)
                    else:
                        count += dp(pos + 1, new_carry, False, False)

            return count

        result = dp(0, 0, True, True)
        dp.cache_clear()
        return result


# Brute force for verification
def brute_force(n):
    def has_zero(x):
        while x > 0:
            if x % 10 == 0:
                return True
            x //= 10
        return False

    count = 0
    for a in range(1, n):
        b = n - a
        if b > 0 and not has_zero(a) and not has_zero(b):
            count += 1
    return count


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Verify against brute force for small values
    for n in range(2, 50):
        expected = brute_force(n)
        got = sol.countNoZeroPairs(n)
        assert got == expected, f"n={n}: expected {expected}, got {got}"

    # Known examples
    assert sol.countNoZeroPairs(2) == 1
    assert sol.countNoZeroPairs(3) == 2
    assert sol.countNoZeroPairs(11) == 8

    print("all tests passed")
