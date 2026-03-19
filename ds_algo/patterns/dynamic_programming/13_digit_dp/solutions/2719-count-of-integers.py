"""
2719. Count of Integers
https://leetcode.com/problems/count-of-integers/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP counting numbers in [num1, num2] whose digit sum is in
[min_sum, max_sum]. count(x) = numbers in [0, x] with valid digit sum.
Answer = count(num2) - count(num1-1). Use tight constraint and track
running digit sum.

Time: O(len * digit_sum * 10)  Space: O(len * digit_sum)
---
"""

MOD = 10**9 + 7


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def count_up_to(s):
            from functools import lru_cache
            n = len(s)

            @lru_cache(maxsize=None)
            def dp(pos, dsum, tight):
                if dsum > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= dsum <= max_sum else 0
                limit = int(s[pos]) if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    res += dp(pos + 1, dsum + d, tight and d == limit)
                return res % MOD

            result = dp(0, 0, True)
            dp.cache_clear()
            return result

        def subtract_one(s):
            digits = list(s)
            i = len(digits) - 1
            while i >= 0 and digits[i] == '0':
                digits[i] = '9'
                i -= 1
            digits[i] = str(int(digits[i]) - 1)
            # Remove leading zeros
            result = ''.join(digits).lstrip('0')
            return result if result else '0'

        ans = (count_up_to(num2) - count_up_to(subtract_one(num1))) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.count("1", "12", 1, 8) == 11
    assert sol.count("1", "5", 1, 5) == 5
    assert sol.count("1", "1", 1, 1) == 1

    print("All tests passed!")
