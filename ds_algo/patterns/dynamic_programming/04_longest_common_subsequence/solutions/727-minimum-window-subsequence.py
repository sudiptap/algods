"""
727. Minimum Window Subsequence
https://leetcode.com/problems/minimum-window-subsequence/

Pattern: 04 - Longest Common Subsequence

---
APPROACH: DP where dp[i][j] = starting index in s1 for the shortest window
          ending at s1[i-1] that contains s2[:j] as a subsequence.
- dp[i][0] = i for all i (empty s2 matched trivially).
- If s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
- Else: dp[i][j] = dp[i-1][j]  (skip s1[i-1])
- We want min (i - dp[i][m]) where m = len(s2), dp[i][m] != -1.
- Optimize space: only need previous row (rolling over i).

Time: O(|s1| * |s2|)  Space: O(|s2|)
---
"""


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)

        # dp[j] = earliest start index in s1 such that s2[:j] is a subsequence
        #         ending at the current position in s1.
        # We process s1 char by char.
        # -1 means not achievable.

        # dp[0] = current i (empty pattern always starts here)
        # Update backwards to avoid overwriting needed values.

        dp = [-1] * (m + 1)
        dp[0] = 0  # empty pattern can start at index 0

        best_start = -1
        best_len = float('inf')

        for i in range(n):
            # Update dp in reverse order to use values from previous iteration
            for j in range(m, 0, -1):
                if s1[i] == s2[j - 1]:
                    dp[j] = dp[j - 1]
                # else dp[j] stays (carried from previous i, representing dp[i-1][j])
            dp[0] = i + 1  # for next char, empty pattern starts at i+1 (earliest possible start)

            # Check if full s2 matched
            if dp[m] != -1:
                length = i + 1 - dp[m]
                if length < best_len:
                    best_len = length
                    best_start = dp[m]

        return s1[best_start:best_start + best_len] if best_start != -1 else ""


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minWindow("abcdebdde", "bde") == "bcde"
    assert sol.minWindow("jmeqksfrsdcmsiwvaovztaqenrat", "u") == ""
    assert sol.minWindow("abcde", "ace") == "abcde"
    assert sol.minWindow("aaa", "a") == "a"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("ab", "b") == "b"
    assert sol.minWindow("abab", "ab") == "ab"

    print("all tests passed")
