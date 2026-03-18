"""
1092. Shortest Common Supersequence (Hard)
https://leetcode.com/problems/shortest-common-supersequence/

Pattern: 04 - Longest Common Subsequence

Given two strings str1 and str2, return the shortest string that has both
str1 and str2 as subsequences.

Approach:
    1. Build the full LCS DP table.
    2. Backtrack through the table to reconstruct the supersequence:
       - When chars match (part of LCS), include once.
       - Otherwise include the char from the direction we came from
         (the larger dp neighbour) and move in that direction.
    3. Append any remaining characters from either string.

    The result has length  len(str1) + len(str2) - len(LCS).

Time:  O(m * n)
Space: O(m * n)
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """Return the shortest common supersequence of str1 and str2."""
        m, n = len(str1), len(str2)

        # Step 1 – build LCS dp table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2 – backtrack to build the supersequence (in reverse)
        res = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1

        # Remaining chars
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return "".join(reversed(res))


# ───────────────────────── tests ─────────────────────────

def _is_subsequence(s: str, t: str) -> bool:
    it = iter(t)
    return all(c in it for c in s)


def test_example1():
    res = Solution().shortestCommonSupersequence("abac", "cab")
    assert _is_subsequence("abac", res)
    assert _is_subsequence("cab", res)
    assert len(res) == 5  # "cabac"

def test_identical():
    res = Solution().shortestCommonSupersequence("abc", "abc")
    assert res == "abc"

def test_no_overlap():
    res = Solution().shortestCommonSupersequence("ab", "cd")
    assert _is_subsequence("ab", res)
    assert _is_subsequence("cd", res)
    assert len(res) == 4

def test_one_empty_like():
    res = Solution().shortestCommonSupersequence("a", "ab")
    assert _is_subsequence("a", res)
    assert _is_subsequence("ab", res)
    assert len(res) == 2

def test_longer():
    res = Solution().shortestCommonSupersequence("bbbaaaba", "bbababbb")
    assert _is_subsequence("bbbaaaba", res)
    assert _is_subsequence("bbababbb", res)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
