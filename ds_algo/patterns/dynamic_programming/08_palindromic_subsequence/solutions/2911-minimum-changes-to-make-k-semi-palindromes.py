"""
2911. Minimum Changes to Make K Semi-palindromes
https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

Pattern: 08 - Palindromic Subsequence (Precompute semi-palindrome costs, DP partition)

---
APPROACH: Precompute cost[i][j] = min changes to make s[i:j+1] a semi-palindrome.
A semi-palindrome of length L can use any divisor d of L (1 <= d < L). For each d,
check d interleaved subsequences and count mismatches. Then DP partition into k parts.

Time: O(n^3 + n^2 * k)  Space: O(n^2)
---
"""


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute semi-palindrome cost for substring s[i:j+1]
        def semi_cost(i, j):
            length = j - i + 1
            if length <= 1:
                return 0
            best = float('inf')
            # Try each valid period d (divisor of length, 1 <= d < length)
            for d in range(1, length):
                if length % d != 0:
                    continue
                changes = 0
                for start in range(d):
                    # Check subsequence: s[i+start], s[i+start+d], s[i+start+2d], ...
                    seq = []
                    for pos in range(i + start, j + 1, d):
                        seq.append(s[pos])
                    # Count changes to make this subsequence a palindrome
                    l, r = 0, len(seq) - 1
                    while l < r:
                        if seq[l] != seq[r]:
                            changes += 1
                        l += 1
                        r -= 1
                best = min(best, changes)
            return best

        # Precompute all costs
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = semi_cost(i, j)

        # DP: dp[p][i] = min cost to partition s[0:i+1] into p semi-palindromes
        INF = float('inf')
        dp = [[INF] * n for _ in range(k + 1)]

        for i in range(n):
            dp[1][i] = cost[0][i]

        for p in range(2, k + 1):
            for i in range(p - 1, n):
                for j in range(p - 2, i):
                    if dp[p - 1][j] < INF:
                        dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j + 1][i])

        return dp[k][n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumChanges("abcac", 2) == 1
    assert sol.minimumChanges("abcdef", 2) == 2
    assert sol.minimumChanges("aabbaa", 3) == 0

    print("All tests passed!")
