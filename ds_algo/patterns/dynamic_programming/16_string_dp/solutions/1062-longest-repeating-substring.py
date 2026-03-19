"""
1062. Longest Repeating Substring (Medium)

Pattern: 16_string_dp
- Find the longest substring that occurs at least twice.

Approach:
- DP approach: dp[i][j] = length of longest common suffix of s[0..i-1] and s[0..j-1]
  where we only consider i != j to find repeating (not same position).
- dp[i][j] = dp[i-1][j-1] + 1 if s[i-1] == s[j-1] and i != j, else 0.
- Answer is max over all dp[i][j].
- Alternative: binary search on length + rolling hash for O(n log n), but
  the DP approach is simpler and O(n^2).

Complexity:
- Time:  O(n^2)
- Space: O(n^2), can be optimized to O(n)
"""


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ans = 0

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: "abcd" -> 0 (no repeating substring)
    assert sol.longestRepeatingSubstring("abcd") == 0

    # Example 2: "abbaba" -> 2 ("ab" or "ba" repeats)
    assert sol.longestRepeatingSubstring("abbaba") == 2

    # Example 3: "aabcaabdaab" -> 3 ("aab" repeats)
    assert sol.longestRepeatingSubstring("aabcaabdaab") == 3

    # Single char repeated
    assert sol.longestRepeatingSubstring("aaaa") == 3

    # Two chars
    assert sol.longestRepeatingSubstring("ab") == 0

    # "aa"
    assert sol.longestRepeatingSubstring("aa") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
