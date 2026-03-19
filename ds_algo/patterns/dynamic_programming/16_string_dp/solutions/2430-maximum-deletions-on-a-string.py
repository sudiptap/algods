"""
2430. Maximum Deletions on a String
https://leetcode.com/problems/maximum-deletions-on-a-string/

Pattern: 16 - String DP

---
APPROACH: dp[i] = max deletions from s[i:], using LCP for prefix matching
- dp[i] = max number of operations starting from index i.
- For each i, try deleting prefix s[i:i+l] where s[i:i+l] == s[i+l:i+2l].
  Then dp[i] = max(dp[i], dp[i+l] + 1).
- Use LCP (Longest Common Prefix) array: lcp[i][j] = length of longest common
  prefix of s[i:] and s[j:]. Compute bottom-up.
- If no valid deletion found, dp[i] = 1 (delete entire remaining string).

Time: O(n^2)  Space: O(n^2)
---
"""


class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)

        # Precompute LCP
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        dp = [1] * n  # worst case: delete whole suffix

        for i in range(n - 1, -1, -1):
            for l in range(1, (n - i) // 2 + 1):
                # Check if s[i:i+l] == s[i+l:i+2l]
                if lcp[i][i + l] >= l:
                    dp[i] = max(dp[i], dp[i + l] + 1)

        return dp[0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.deleteString("abcabcdabc") == 2
    assert sol.deleteString("aaabaab") == 4
    assert sol.deleteString("aaaaa") == 5
    assert sol.deleteString("a") == 1
    assert sol.deleteString("ab") == 1

    print("all tests passed")
