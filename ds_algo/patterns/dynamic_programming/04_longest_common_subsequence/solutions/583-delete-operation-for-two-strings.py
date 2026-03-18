"""
583. Delete Operation for Two Strings
https://leetcode.com/problems/delete-operation-for-two-strings/

Pattern: 04 - Longest Common Subsequence

---
APPROACH: LCS then derive answer
- Find the length of the Longest Common Subsequence of word1 and word2.
- Characters NOT in the LCS must be deleted from both strings.
- answer = len(word1) + len(word2) - 2 * LCS

Time: O(m * n)   Space: O(m * n), optimizable to O(n)
---
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of delete steps to make word1 and word2 the same."""
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs = dp[m][n]
        return m + n - 2 * lcs


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minDistance("sea", "eat") == 2
    assert sol.minDistance("leetcode", "etco") == 4
    assert sol.minDistance("", "") == 0
    assert sol.minDistance("abc", "") == 3
    assert sol.minDistance("abc", "abc") == 0
    assert sol.minDistance("abc", "def") == 6

    print("all tests passed")
