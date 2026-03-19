"""
3490. Count Beautiful Numbers
https://leetcode.com/problems/count-beautiful-numbers/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP tracking digit product divisibility.
- A number is beautiful if the product of its digits is divisible by the sum of its digits.
- Count beautiful numbers in range [l, r].
- Digit DP: track (position, tight, sum_of_digits, product_of_digits, started).
- Product can be large but has limited prime factors (only 2, 3, 5, 7 from digits 2-9).
- Compress product representation.

Time: O(d * sum * product_states * 10)  Space: O(d * sum * product_states)
---
"""

from functools import lru_cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count(num):
            if num <= 0:
                return 0
            digits = list(map(int, str(num)))
            n = len(digits)

            @lru_cache(maxsize=None)
            def dp(pos, tight, s, p, started):
                """
                pos: current digit position
                tight: whether we're still bounded by num
                s: sum of digits so far
                p: product of digits so far
                started: have we placed a non-zero digit yet
                """
                if pos == n:
                    if not started:
                        return 0
                    return 1 if p % s == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    if not started and d == 0:
                        res += dp(pos + 1, new_tight, 0, 0, False)
                    else:
                        new_s = s + d
                        new_p = (p if p > 0 else 1) * d if started else d
                        res += dp(pos + 1, new_tight, new_s, new_p, True)

                return res

            result = dp(0, True, 0, 0, False)
            dp.cache_clear()
            return result

        return count(r) - count(l - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.beautifulNumbers(10, 20) == 2
    assert sol.beautifulNumbers(1, 15) == 10

    print("Solution: all tests passed")
