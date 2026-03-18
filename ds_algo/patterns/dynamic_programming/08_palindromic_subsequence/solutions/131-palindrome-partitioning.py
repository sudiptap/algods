"""
131. Palindrome Partitioning (Medium)
https://leetcode.com/problems/palindrome-partitioning/

Problem:
    Given a string s, partition s such that every substring of the partition
    is a palindrome. Return all possible palindrome partitionings of s.

Pattern: 08 - Palindromic Subsequence

Approach:
    1. Pre-compute a DP table where dp[i][j] is True if s[i..j] is a
       palindrome. Fill bottom-up: single chars are palindromes, two chars
       match if equal, longer substrings check endpoints + inner substring.
    2. Backtrack: starting from index 0, try every end index. If the
       substring is a palindrome (O(1) lookup), include it and recurse on
       the remainder.

Complexity:
    Time:  O(n * 2^n) - in the worst case (e.g. "aaa") we generate
           exponentially many partitions, each taking O(n) to copy.
    Space: O(n^2) for the DP table + O(n) recursion depth
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # Pre-compute palindrome lookup table
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        result: List[List[str]] = []
        path: List[str] = []

        def backtrack(start: int) -> None:
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: "aab" -> [["a","a","b"],["aa","b"]]
    result = sol.partition("aab")
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert sorted(result) == sorted(expected), f"Test 1 failed: got {result}"

    # Test 2: "a" -> [["a"]]
    result = sol.partition("a")
    assert result == [["a"]], f"Test 2 failed: got {result}"

    # Test 3: "aaa" -> [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]
    result = sol.partition("aaa")
    expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    assert sorted(result) == sorted(expected), f"Test 3 failed: got {result}"

    # Test 4: "ab" -> [["a","b"]]
    result = sol.partition("ab")
    assert result == [["a", "b"]], f"Test 4 failed: got {result}"

    # Test 5: "aba" -> [["a","b","a"],["aba"]]
    result = sol.partition("aba")
    expected = [["a", "b", "a"], ["aba"]]
    assert sorted(result) == sorted(expected), f"Test 5 failed: got {result}"

    # Test 6: empty-ish single char
    result = sol.partition("z")
    assert result == [["z"]], f"Test 6 failed: got {result}"

    print("All tests passed for 131. Palindrome Partitioning!")


if __name__ == "__main__":
    run_tests()
