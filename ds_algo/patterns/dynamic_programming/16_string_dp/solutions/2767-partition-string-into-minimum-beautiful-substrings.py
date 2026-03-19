"""
2767. Partition String Into Minimum Beautiful Substrings
https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

Pattern: 16 - String DP (dp[i] = min partitions for s[:i])

---
APPROACH: Precompute all powers of 5 in binary. dp[i] = minimum partitions
for s[0:i]. For each position, check all substrings ending at i that form
a power of 5 (no leading zeros).

Time: O(n^2)  Space: O(n)
---
"""


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # Powers of 5 up to 2^15
        powers = set()
        p = 1
        while p <= (1 << 15):
            powers.add(bin(p)[2:])
            p *= 5

        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                if s[j] == '0':
                    continue
                sub = s[j:i]
                if sub in powers:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumBeautifulSubstrings("1011") == 2
    assert sol.minimumBeautifulSubstrings("111") == 3
    assert sol.minimumBeautifulSubstrings("0") == -1

    print("All tests passed!")
