"""
72. Edit Distance (Levenshtein Distance)
https://leetcode.com/problems/edit-distance/

Pattern: 04 - Longest Common Subsequence (two-sequence alignment — THE classic)

---
APPROACH: 2D DP
- dp[i][j] = min operations to convert word1[:i] → word2[:j]
- If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]  (no-op)
- Else: dp[i][j] = 1 + min(
      dp[i-1][j-1],  # replace
      dp[i-1][j],    # delete from word1
      dp[i][j-1]     # insert into word1
  )
- Base: dp[i][0] = i (delete all), dp[0][j] = j (insert all)

Time: O(m*n)  Space: O(m*n), optimizable to O(n)
---
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # replace
                        dp[i - 1][j],       # delete
                        dp[i][j - 1]        # insert
                    )

        return dp[m][n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
    assert sol.minDistance("", "") == 0
    assert sol.minDistance("abc", "") == 3
    assert sol.minDistance("", "abc") == 3
    assert sol.minDistance("abc", "abc") == 0

    print("all tests passed")
