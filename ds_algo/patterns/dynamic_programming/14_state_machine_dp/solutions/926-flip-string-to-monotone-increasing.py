"""
926. Flip String to Monotone Increasing
https://leetcode.com/problems/flip-string-to-monotone-increasing/

Pattern: 14 - State Machine DP

---
APPROACH: Greedy / State Machine
- Track ones_count (number of '1's seen so far) and flips (min flips needed).
- When we see a '1': ones_count += 1 (no flip needed).
- When we see a '0' after some '1's: we can either flip this '0' to '1' (flips + 1)
  or flip all previous '1's (ones_count). Take the minimum.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Return the minimum number of flips to make s monotone increasing."""
        ones_count = 0
        flips = 0

        for ch in s:
            if ch == '1':
                ones_count += 1
            else:
                # '0' encountered: flip it, or flip all preceding 1s
                flips = min(flips + 1, ones_count)

        return flips


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minFlipsMonoIncr("00110") == 1
    assert sol.minFlipsMonoIncr("010110") == 2
    assert sol.minFlipsMonoIncr("00011000") == 2
    assert sol.minFlipsMonoIncr("0") == 0
    assert sol.minFlipsMonoIncr("1") == 0
    assert sol.minFlipsMonoIncr("111") == 0
    assert sol.minFlipsMonoIncr("000") == 0
    assert sol.minFlipsMonoIncr("10") == 1

    print("all tests passed")
