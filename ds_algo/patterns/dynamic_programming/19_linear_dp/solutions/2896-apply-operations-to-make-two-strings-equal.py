"""
2896. Apply Operations to Make Two Strings Equal
https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

Pattern: 19 - Linear DP (DP on positions where strings differ)

---
APPROACH: Find positions where s1[i] != s2[i]. If count is odd, return -1.
We can pair adjacent diffs (cost = pos[i+1] - pos[i]) or pair any two diffs
with cost x each. dp[i] = min cost to fix first i differing positions.

Time: O(m) where m = number of differing positions  Space: O(m)
---
"""

from functools import lru_cache


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        m = len(diffs)
        if m % 2 == 1:
            return -1
        if m == 0:
            return 0

        @lru_cache(maxsize=None)
        def dp(i):
            if i >= m:
                return 0
            if i == m - 1:
                return float('inf')  # shouldn't happen since m is even
            # Option 1: pair diffs[i] with diffs[i+1] using adjacent flips
            # Option 2: pair diffs[i] with some later diff using cost x
            # We model option 2 as: pair diffs[i] with diffs[i+1] at cost x,
            # but that's not right. Use the standard pairing DP:
            # Either pair i with i+1 (adjacent cost), or skip i to pair with someone later (cost x/2 each)
            res = dp(i + 2) + min(diffs[i + 1] - diffs[i], x)
            if i + 2 <= m:
                res = min(res, dp(i + 1) + x / 2)  # defer pairing i
            return res

        # Actually, cleaner DP: dp[i] = min cost to handle diffs[i:]
        # But the x/2 trick: each "remote pair" costs x total, split as x/2 per element
        dp_arr = [0] * (m + 1)
        for i in range(m - 2, -1, -2):
            # Must pair them all. dp[i] processes pairs.
            pass

        # Cleaner approach: dp[i] = min cost for first i diffs
        dp2 = [float('inf')] * (m + 1)
        dp2[0] = 0
        for i in range(1, m + 1):
            # Use cost x to pair with any previous (amortized x per pair)
            dp2[i] = dp2[i - 1] + x / 2
            if i >= 2:
                dp2[i] = min(dp2[i], dp2[i - 2] + diffs[i - 1] - diffs[i - 2])

        return int(dp2[m])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperations("1100011000", "0101001010", 2) == 4
    assert sol.minOperations("10110", "00011", 4) == -1

    print("All tests passed!")
