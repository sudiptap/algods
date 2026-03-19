"""
788. Rotated Digits
https://leetcode.com/problems/rotated-digits/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP counting valid rotated numbers up to n
- Valid digits: 0,1,2,5,6,8,9. Invalid: 3,4,7.
- A number is "good" if it's valid AND contains at least one of {2,5,6,9}
  (digits that actually change when rotated).
- Digit DP: for each digit position, track (tight constraint, has_diff).
- has_diff = whether we've seen a digit from {2,5,6,9}.
- Count numbers that are valid and have has_diff = True.

Time: O(d) where d = number of digits in n  Space: O(d)
---
"""

from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        valid = {0, 1, 2, 5, 6, 8, 9}
        diff = {2, 5, 6, 9}

        @lru_cache(maxsize=None)
        def dp(pos, tight, has_diff, started):
            if pos == len(digits):
                return 1 if started and has_diff else 0

            limit = digits[pos] if tight else 9
            count = 0

            for d in range(0, limit + 1):
                if d not in valid:
                    continue
                new_started = started or d > 0
                new_tight = tight and (d == limit)
                new_diff = has_diff or (d in diff and new_started)
                count += dp(pos + 1, new_tight, new_diff, new_started)

            return count

        return dp(0, True, False, False)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.rotatedDigits(10) == 4    # 2, 5, 6, 9
    assert sol.rotatedDigits(1) == 0
    assert sol.rotatedDigits(2) == 1     # just 2
    assert sol.rotatedDigits(100) == 40
    assert sol.rotatedDigits(857) == 247

    print("all tests passed")
