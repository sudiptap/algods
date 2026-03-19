"""
2376. Count Special Integers
https://leetcode.com/problems/count-special-integers/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP counting numbers with all distinct digits
- Process digits of n from most significant to least.
- Track: position, tight (is current prefix == n's prefix), mask of used digits,
  started (have we placed a nonzero digit yet).
- If not tight, remaining positions can use any unused digit.

Time: O(10 * 2^10 * digits)  Space: O(2^10 * digits)
---
"""

from functools import lru_cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        L = len(s)

        @lru_cache(maxsize=None)
        def dp(pos, mask, tight, started):
            if pos == L:
                return 1 if started else 0

            limit = int(s[pos]) if tight else 9
            res = 0

            if not started:
                # Option: skip this digit (leading zero)
                res += dp(pos + 1, mask, False, False)
                # Place a nonzero digit
                for d in range(1, limit + 1):
                    if mask & (1 << d):
                        continue
                    res += dp(pos + 1, mask | (1 << d), tight and (d == limit), True)
            else:
                for d in range(0, limit + 1):
                    if mask & (1 << d):
                        continue
                    res += dp(pos + 1, mask | (1 << d), tight and (d == limit), True)

            return res

        return dp(0, 0, True, False)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countSpecialNumbers(20) == 19
    assert sol.countSpecialNumbers(5) == 5
    assert sol.countSpecialNumbers(135) == 110
    assert sol.countSpecialNumbers(1) == 1

    print("all tests passed")
