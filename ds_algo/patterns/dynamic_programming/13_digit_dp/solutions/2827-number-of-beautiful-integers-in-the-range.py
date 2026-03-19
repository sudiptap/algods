"""
2827. Number of Beautiful Integers in the Range
https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

Pattern: 13 - Digit DP (tracking even/odd digit counts and remainder)

---
APPROACH: Digit DP with states: position, count_even - count_odd (balance),
current number mod k, tight constraint, and started flag. A number is
beautiful if #even_digits == #odd_digits and number % k == 0.

Time: O(len * 2*len * k * 10)  Space: O(len * 2*len * k)
---
"""

from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_up_to(num):
            s = str(num)
            n = len(s)

            @lru_cache(maxsize=None)
            def dp(pos, balance, rem, tight, started):
                # balance = #even - #odd so far
                if pos == n:
                    return 1 if started and balance == 0 and rem == 0 else 0
                limit = int(s[pos]) if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    if not started and d == 0:
                        res += dp(pos + 1, 0, 0, new_tight, False)
                    else:
                        new_balance = balance + (1 if d % 2 == 0 else -1)
                        new_rem = (rem * 10 + d) % k
                        res += dp(pos + 1, new_balance, new_rem, new_tight, True)
                return res

            result = dp(0, 0, 0, True, False)
            dp.cache_clear()
            return result

        return count_up_to(high) - count_up_to(low - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfBeautifulIntegers(10, 20, 3) == 2  # 12, 18
    assert sol.numberOfBeautifulIntegers(1, 10, 1) == 1   # 10
    assert sol.numberOfBeautifulIntegers(5, 5, 2) == 0

    print("All tests passed!")
