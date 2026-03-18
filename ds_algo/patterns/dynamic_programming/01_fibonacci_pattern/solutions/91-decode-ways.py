"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/

Pattern: 01 - Fibonacci (like climbing stairs but with validity constraints)

---
APPROACH: Linear DP with O(1) space
- dp[i] = number of ways to decode s[:i]
- Single digit: if s[i-1] != '0', dp[i] += dp[i-1]
- Two digits:   if 10 <= int(s[i-2:i]) <= 26, dp[i] += dp[i-2]
- Like climbing stairs where you can take 1 or 2 steps,
  but some steps are blocked (leading zeros, values > 26)

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            curr = 0

            # single digit: s[i] can stand alone if not '0'
            if s[i] != '0':
                curr += prev1

            # two digits: s[i-1:i+1] must be in [10, 26]
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numDecodings("12") == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("06") == 0
    assert sol.numDecodings("0") == 0
    assert sol.numDecodings("1") == 1
    assert sol.numDecodings("10") == 1
    assert sol.numDecodings("27") == 1
    assert sol.numDecodings("11106") == 2
    assert sol.numDecodings("111") == 3  # 1,1,1 or 11,1 or 1,11

    print("all tests passed")
