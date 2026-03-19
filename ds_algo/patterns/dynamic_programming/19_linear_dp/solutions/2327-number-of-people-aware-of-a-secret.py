"""
2327. Number of People Aware of a Secret
https://leetcode.com/problems/number-of-people-aware-of-a-secret/

Pattern: 19 - Linear DP

---
APPROACH: dp[i] = number of new people learning the secret on day i
- A person who learns on day i starts sharing from day i+delay to day i+forget-1.
- On day i+forget, they forget.
- dp[i] = sum(dp[j]) for j in [i-forget+1, i-delay] (people who can share on day i).
- Use prefix sums for O(1) range sum.
- Answer = sum(dp[j]) for j in [n-forget+1, n] (people who haven't forgotten by day n).

Time: O(n)  Space: O(n)
---
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        # prefix[i] = sum(dp[1..i])
        prefix = [0] * (n + 2)
        prefix[1] = 1

        for i in range(2, n + 1):
            # People who can share on day i learned on days [i-forget+1, i-delay]
            lo = max(1, i - forget + 1)
            hi = i - delay
            if hi >= lo:
                dp[i] = (prefix[hi] - prefix[lo - 1]) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

        # People who know on day n: learned on days [n-forget+1, n]
        lo = max(1, n - forget + 1)
        ans = (prefix[n] - prefix[lo - 1]) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.peopleAwareOfSecret(6, 2, 4) == 5
    assert sol.peopleAwareOfSecret(4, 1, 3) == 6
    assert sol.peopleAwareOfSecret(1, 1, 2) == 1

    print("all tests passed")
