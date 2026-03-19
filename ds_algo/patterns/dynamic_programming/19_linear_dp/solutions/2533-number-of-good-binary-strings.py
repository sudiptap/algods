"""
2533. Number of Good Binary Strings
https://leetcode.com/problems/number-of-good-binary-strings/

Pattern: 19 - Linear DP

---
APPROACH: DP like climbing stairs with steps of zeroGroup and oneGroup length
- dp[i] = number of good binary strings of length i.
- dp[0] = 1 (empty string).
- dp[i] += dp[i - zeroGroup] (append zeroGroup zeros)
- dp[i] += dp[i - oneGroup] (append oneGroup ones)
- Answer: sum(dp[minLength..maxLength])

Time: O(maxLength)  Space: O(maxLength)
---
"""


class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (maxLength + 1)
        dp[0] = 1

        for i in range(1, maxLength + 1):
            if i >= zeroGroup:
                dp[i] = (dp[i] + dp[i - zeroGroup]) % MOD
            if i >= oneGroup:
                dp[i] = (dp[i] + dp[i - oneGroup]) % MOD

        return sum(dp[minLength:maxLength + 1]) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.goodBinaryStrings(2, 3, 1, 2) == 5
    assert sol.goodBinaryStrings(4, 4, 4, 3) == 1
    assert sol.goodBinaryStrings(1, 1, 1, 1) == 2

    print("all tests passed")
