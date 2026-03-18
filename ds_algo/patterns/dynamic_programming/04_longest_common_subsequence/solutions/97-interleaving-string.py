"""
97. Interleaving String
https://leetcode.com/problems/interleaving-string/

Pattern: 04 - Longest Common Subsequence (two-sequence DP)

---
APPROACH: 2D DP → 1D optimized
- dp[i][j] = can s1[:i] and s2[:j] interleave to form s3[:i+j]?
- If s1[i-1] == s3[i+j-1]: dp[i][j] |= dp[i-1][j]  (take from s1)
- If s2[j-1] == s3[i+j-1]: dp[i][j] |= dp[i][j-1]  (take from s2)
- Early exit: if len(s1) + len(s2) != len(s3), return False

1D optimization: only need previous row → O(n) space

Time: O(m*n)  Space: O(n)
---
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)
        dp[0] = True

        # base row: s1 is empty, check if s2[:j] == s3[:j]
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # base column: s2 is empty
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1]) or      # take from s1
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])     # take from s2
                )

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert sol.isInterleave("", "", "") == True
    assert sol.isInterleave("a", "", "a") == True
    assert sol.isInterleave("", "b", "b") == True
    assert sol.isInterleave("a", "b", "ab") == True
    assert sol.isInterleave("a", "b", "ba") == True

    print("all tests passed")
