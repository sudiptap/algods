"""
3519. Count Numbers with Non-Decreasing Digits
https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP tracking last digit placed.
- Count numbers in [l, r] (given as strings) with non-decreasing digits.
- dp(pos, tight, last_digit, started) = count of valid numbers.
- Each digit must be >= last_digit placed.

Time: O(d * 10 * 10)  Space: O(d * 10)
---
"""

from functools import lru_cache


class Solution:
    def countNumbers(self, l: str, r: str) -> int:
        MOD = 10**9 + 7

        def count(num_str):
            digits = list(map(int, num_str))
            n = len(digits)

            @lru_cache(maxsize=None)
            def dp(pos, tight, last, started):
                if pos == n:
                    return 1 if started else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    if not started and d == 0:
                        res += dp(pos + 1, tight and (d == limit), 0, False)
                    elif d >= last:
                        res += dp(pos + 1, tight and (d == limit), d, True)
                    # else: d < last, skip (not non-decreasing)
                res %= MOD
                return res

            result = dp(0, True, 0, False)
            dp.cache_clear()
            return result

        def subtract_one(s):
            digits = list(s)
            i = len(digits) - 1
            while i >= 0 and digits[i] == '0':
                digits[i] = '9'
                i -= 1
            if i < 0:
                return "0"
            digits[i] = str(int(digits[i]) - 1)
            result = ''.join(digits).lstrip('0')
            return result if result else "0"

        return (count(r) - count(subtract_one(l)) + MOD) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countNumbers("1", "100") == 54  # Non-decreasing numbers 1-100
    assert sol.countNumbers("1", "9") == 9
    assert sol.countNumbers("11", "11") == 1
    assert sol.countNumbers("10", "10") == 0  # 10 has decreasing digits (1 > 0)

    print("Solution: all tests passed")
