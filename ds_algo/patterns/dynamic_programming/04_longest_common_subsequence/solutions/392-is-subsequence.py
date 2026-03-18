"""
392. Is Subsequence (Easy)

Given two strings s and t, return true if s is a subsequence of t.

A subsequence is formed by deleting some (or no) characters from t
without changing the relative order of the remaining characters.

Approach 1 - Two Pointers (primary):
    Walk pointer i through s and pointer j through t.
    Whenever s[i] == t[j], advance i. Always advance j.
    If i reaches len(s), every character of s was matched in order.
    Time : O(|t|)
    Space: O(1)

Approach 2 - DP / Precomputed index (follow-up for many s queries):
    Precompute next[j][c] = next index in t where char c appears at or after j.
    Then each query is answered in O(|s|) after O(26 * |t|) preprocessing.

Example:
    s = "abc", t = "ahbgdc" -> True
    s = "axc", t = "ahbgdc" -> False
"""

from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Two-pointer scan: O(|t|) time, O(1) space."""
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)

    def isSubsequenceDP(self, s: str, t: str) -> bool:
        """Follow-up: precompute next-occurrence table for many s queries.

        Preprocessing: O(26 * |t|)
        Each query  : O(|s|)
        """
        n = len(t)
        # nxt[j][c] = earliest index >= j in t where character c appears (-1 if none)
        nxt = [[0] * 26 for _ in range(n + 1)]
        for c in range(26):
            nxt[n][c] = -1
        for j in range(n - 1, -1, -1):
            for c in range(26):
                nxt[j][c] = nxt[j + 1][c]
            nxt[j][ord(t[j]) - ord('a')] = j

        j = 0
        for ch in s:
            if j >= n or nxt[j][ord(ch) - ord('a')] == -1:
                return False
            j = nxt[j][ord(ch) - ord('a')] + 1
        return True


# ---- Tests ----
def test():
    sol = Solution()
    # Two-pointer tests
    assert sol.isSubsequence("abc", "ahbgdc") is True
    assert sol.isSubsequence("axc", "ahbgdc") is False
    assert sol.isSubsequence("", "ahbgdc") is True
    assert sol.isSubsequence("abc", "") is False
    assert sol.isSubsequence("", "") is True
    assert sol.isSubsequence("a", "a") is True
    assert sol.isSubsequence("b", "a") is False
    assert sol.isSubsequence("ace", "abcde") is True

    # DP follow-up tests (same cases)
    assert sol.isSubsequenceDP("abc", "ahbgdc") is True
    assert sol.isSubsequenceDP("axc", "ahbgdc") is False
    assert sol.isSubsequenceDP("", "ahbgdc") is True
    assert sol.isSubsequenceDP("abc", "") is False
    assert sol.isSubsequenceDP("", "") is True
    assert sol.isSubsequenceDP("a", "a") is True
    assert sol.isSubsequenceDP("b", "a") is False
    assert sol.isSubsequenceDP("ace", "abcde") is True

    print("All tests passed!")


if __name__ == "__main__":
    test()
