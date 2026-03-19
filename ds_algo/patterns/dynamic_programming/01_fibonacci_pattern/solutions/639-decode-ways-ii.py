"""
639. Decode Ways II
https://leetcode.com/problems/decode-ways-ii/

Pattern: 01 - Fibonacci Pattern

---
APPROACH: Linear DP extending Decode Ways (#91) with '*' wildcard
- '*' can represent digits 1-9.
- dp[i] = number of ways to decode s[:i]
- Single digit contributions:
  - digit 1-9 -> dp[i-1]
  - '*' -> 9 * dp[i-1]  (represents 1-9)
  - '0' -> 0
- Two digit contributions (s[i-1], s[i]):
  - Both known: if 10 <= val <= 26 -> dp[i-2]
  - First '*', second known d:
    - d <= 6: 2 ways (1d, 2d) -> 2 * dp[i-2]
    - d >= 7: 1 way (1d only) -> dp[i-2]
  - First known, second '*':
    - first == '1': '*' = 1-9 -> 9 * dp[i-2]
    - first == '2': '*' = 1-6 -> 6 * dp[i-2]
    - else: 0
  - Both '*': 1x(1-9) + 2x(1-6) = 15 -> 15 * dp[i-2]

Time: O(n)  Space: O(1)
---
"""

MOD = 10**9 + 7


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        # dp[i-2], dp[i-1]
        prev2 = 1  # empty string
        if s[0] == '*':
            prev1 = 9
        elif s[0] == '0':
            prev1 = 0
        else:
            prev1 = 1

        for i in range(1, len(s)):
            curr = 0
            c, p = s[i], s[i - 1]

            # Single digit contribution
            if c == '*':
                curr += 9 * prev1
            elif c != '0':
                curr += prev1

            # Two digit contribution
            if p == '*' and c == '*':
                curr += 15 * prev2  # 11-19 (9) + 21-26 (6)
            elif p == '*':
                # p is *, c is known digit
                if c <= '6':
                    curr += 2 * prev2  # 1c or 2c
                else:
                    curr += prev2      # only 1c
            elif c == '*':
                # p is known, c is *
                if p == '1':
                    curr += 9 * prev2  # 11-19
                elif p == '2':
                    curr += 6 * prev2  # 21-26
                # else: 0
            else:
                # both known
                two = int(p + c)
                if 10 <= two <= 26:
                    curr += prev2

            curr %= MOD
            prev2, prev1 = prev1, curr

        return prev1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numDecodings("*") == 9
    assert sol.numDecodings("1*") == 18   # 1+[1-9] as single=9, 1[1-9] as two=9 -> 18
    assert sol.numDecodings("2*") == 15   # 2+[1-9]=9, 2[1-6]=6 -> 15
    assert sol.numDecodings("**") == 96   # 9*9 + 15 = 96
    assert sol.numDecodings("*1") == 11   # single: 9*1, two: 11 or 21 = 2 -> 11
    assert sol.numDecodings("0") == 0
    assert sol.numDecodings("10") == 1
    assert sol.numDecodings("12") == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("*0") == 2    # only 10 or 20

    print("all tests passed")
