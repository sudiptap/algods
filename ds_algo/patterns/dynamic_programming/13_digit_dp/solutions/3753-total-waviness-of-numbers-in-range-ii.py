"""
3753. Total Waviness of Numbers in Range II
https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP with direction tracking
- Same as Range I but num2 up to 10^15, so brute force won't work.
- State: (pos, prev_digit, prev_direction, tight, started, count_so_far)
  - prev_direction: 1 = last was up, -1 = last was down, 0 = no direction yet
  - count: waviness accumulated so far
- At each position, try each digit. If it creates a peak/valley relative to
  the previous direction, increment waviness.
- We track (pos, prev_digit, direction, tight, started) and accumulate
  waviness contribution.
- Use f(n) = total waviness of [1..n], answer = f(num2) - f(num1-1).

Time: O(d * 10 * 3 * 2 * 2) with d ≈ 16  Space: O(d * 10 * 3)
---
"""

from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count(n):
            if n <= 0:
                return 0
            s = str(n)
            L = len(s)

            @lru_cache(maxsize=None)
            def dp(pos, prev, direction, tight, started):
                """
                Returns (count_of_numbers, total_waviness) for remaining digits.
                direction: 0=none, 1=prev was up from prev-prev, -1=prev was down
                """
                if pos == L:
                    return (1, 0) if started else (0, 0)

                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wav = 0

                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        c, w = dp(pos + 1, -1, 0, new_tight, False)
                        total_cnt += c
                        total_wav += w
                        continue

                    new_started = True

                    if not started or prev == -1:
                        # First or second digit, no direction yet
                        c, w = dp(pos + 1, d, 0, new_tight, new_started)
                        total_cnt += c
                        total_wav += w
                    else:
                        # We have a previous digit; determine new direction
                        if d > prev:
                            new_dir = 1
                        elif d < prev:
                            new_dir = -1
                        else:
                            new_dir = 0

                        # Check if prev is a peak or valley
                        # prev is a peak if direction was "up" and now "down"
                        # prev is a valley if direction was "down" and now "up"
                        wave_add = 0
                        if direction == 1 and new_dir == -1:
                            wave_add = 1  # prev was a peak
                        elif direction == -1 and new_dir == 1:
                            wave_add = 1  # prev was a valley

                        c, w = dp(pos + 1, d, new_dir if new_dir != 0 else direction, new_tight, new_started)
                        total_cnt += c
                        total_wav += w + wave_add * c

                return (total_cnt, total_wav)

            _, result = dp(0, -1, 0, True, False)
            dp.cache_clear()
            return result

        return count(num2) - count(num1 - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.totalWaviness(120, 130) == 3
    assert sol.totalWaviness(198, 202) == 3
    assert sol.totalWaviness(4848, 4848) == 2
    assert sol.totalWaviness(1, 9) == 0

    # Cross-validate with brute force for small range
    def brute(a, b):
        total = 0
        for x in range(a, b + 1):
            d = [int(c) for c in str(x)]
            for i in range(1, len(d) - 1):
                if d[i] > d[i-1] and d[i] > d[i+1]:
                    total += 1
                elif d[i] < d[i-1] and d[i] < d[i+1]:
                    total += 1
        return total

    for a in range(1, 200):
        for b in range(a, min(a + 50, 1000)):
            assert sol.totalWaviness(a, b) == brute(a, b), f"Failed for ({a},{b})"

    print("all tests passed")
