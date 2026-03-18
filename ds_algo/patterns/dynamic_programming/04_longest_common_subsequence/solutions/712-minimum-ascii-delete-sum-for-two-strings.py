"""
712. Minimum ASCII Delete Sum for Two Strings (Medium)
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Pattern: 04 - Longest Common Subsequence

---
APPROACH: 2D DP similar to edit distance.
- dp[i][j] = minimum ASCII sum of deleted characters to make
  s1[:i] and s2[:j] equal.
- If s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]  (no deletion needed).
- Otherwise: dp[i][j] = min(
      dp[i-1][j] + ord(s1[i-1]),   # delete s1[i-1]
      dp[i][j-1] + ord(s2[j-1]),   # delete s2[j-1]
  )
- Base cases:
  dp[0][0] = 0
  dp[i][0] = sum of ASCII values of s1[:i]  (delete all of s1 prefix)
  dp[0][j] = sum of ASCII values of s2[:j]  (delete all of s2 prefix)

Time:  O(m * n)   where m = len(s1), n = len(s2)
Space: O(m * n)   (can be optimised to O(n))
---
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """Return the minimum ASCII sum of deleted characters to make s1 and s2 equal.

        Args:
            s1: First string.
            s2: Second string.

        Returns:
            Lowest ASCII sum of deleted characters from both strings.
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: delete all characters from one string
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1]),
                    )

        return dp[m][n]


# ---------- Tests ----------
def test_minimum_delete_sum():
    sol = Solution()

    # Example 1: delete "at" from "eat" -> 116+97=213? No.
    # "sea" and "eat": delete 's' (115) and 't' (116) -> 231
    assert sol.minimumDeleteSum("sea", "eat") == 231

    # Example 2
    assert sol.minimumDeleteSum("delete", "leet") == 403

    # Both empty
    assert sol.minimumDeleteSum("", "") == 0

    # One empty: must delete entire other string
    assert sol.minimumDeleteSum("abc", "") == ord('a') + ord('b') + ord('c')
    assert sol.minimumDeleteSum("", "xyz") == ord('x') + ord('y') + ord('z')

    # Identical strings: no deletions needed
    assert sol.minimumDeleteSum("hello", "hello") == 0

    # Completely different single chars
    assert sol.minimumDeleteSum("a", "b") == ord('a') + ord('b')

    print("All tests passed for 712. Minimum ASCII Delete Sum for Two Strings")


if __name__ == "__main__":
    test_minimum_delete_sum()
