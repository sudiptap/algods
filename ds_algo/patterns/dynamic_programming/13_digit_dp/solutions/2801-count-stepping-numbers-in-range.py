"""
2801. Count Stepping Numbers in Range
https://leetcode.com/problems/count-stepping-numbers-in-range/

Pattern: 13 - Digit DP (tracking last digit)

---
APPROACH: Digit DP with states: position, last digit, tight constraint,
and whether we've started (to handle leading zeros). A stepping number has
|adjacent digits| = 1.

Time: O(len * 10)  Space: O(len * 10)
---
"""

MOD = 10**9 + 7


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        def count_up_to(s):
            from functools import lru_cache
            n = len(s)

            @lru_cache(maxsize=None)
            def dp(pos, last, tight, started):
                if pos == n:
                    return 1 if started else 0
                limit = int(s[pos]) if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    if not started and d == 0:
                        res += dp(pos + 1, -1, tight and d == limit, False)
                    elif not started:
                        res += dp(pos + 1, d, tight and d == limit, True)
                    elif abs(d - last) == 1:
                        res += dp(pos + 1, d, tight and d == limit, True)
                return res % MOD

            result = dp(0, -1, True, False)
            dp.cache_clear()
            return result

        def subtract_one(s):
            digits = list(s)
            i = len(digits) - 1
            while i >= 0 and digits[i] == '0':
                digits[i] = '9'
                i -= 1
            digits[i] = str(int(digits[i]) - 1)
            result = ''.join(digits).lstrip('0')
            return result if result else '0'

        ans = (count_up_to(high) - count_up_to(subtract_one(low))) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countSteppingNumbers("1", "11") == 10
    assert sol.countSteppingNumbers("90", "101") == 2

    print("All tests passed!")
