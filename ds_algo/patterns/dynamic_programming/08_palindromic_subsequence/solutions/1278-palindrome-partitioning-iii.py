"""
1278. Palindrome Partitioning III (Hard)
https://leetcode.com/problems/palindrome-partitioning-iii/

Problem:
    You are given a string s containing lowercase letters and an integer k.
    You need to change some characters of s to other lowercase letters,
    then divide s into k non-empty disjoint substrings such that each
    substring is a palindrome. Return the minimum number of characters
    that you need to change.

Pattern: 08 - Palindromic Subsequence

Approach:
    1. Precompute cost[i][j] = minimum changes to make s[i..j] a palindrome.
       Use two-pointer: compare s[i] and s[j], if different, increment cost,
       then move inward.
    2. dp[i][k] = minimum changes to partition s[:i] into k palindromes.
       Transition: dp[i][k] = min over all j < i of dp[j][k-1] + cost[j][i-1].
       Base case: dp[i][1] = cost[0][i-1].

Complexity:
    Time:  O(n^2 * k) for the DP transitions + O(n^2) for precomputing costs
    Space: O(n^2) for cost table + O(n * k) for DP table
"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute cost to make s[i..j] a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        # dp[i][p] = min changes to partition s[:i] into p palindromes
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for p in range(1, min(i, k) + 1):
                for j in range(p - 1, i):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])

        return dp[n][k]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: "abc", k=2 -> 1 (change to "aba" + partition "ab|c" won't work,
    # but "a|bc"->change b to c gives "a|cc"=1 change)
    assert sol.palindromePartition("abc", 2) == 1, "Test 1 failed"

    # Test 2: "aabbc", k=3 -> 0 ("aa|bb|c")
    assert sol.palindromePartition("aabbc", 3) == 0, "Test 2 failed"

    # Test 3: "leetcode", k=8 -> 0 (each char is its own palindrome)
    assert sol.palindromePartition("leetcode", 8) == 0, "Test 3 failed"

    # Test 4: single char
    assert sol.palindromePartition("a", 1) == 0, "Test 4 failed"

    # Test 5: already palindrome
    assert sol.palindromePartition("aba", 1) == 0, "Test 5 failed"

    # Test 6: "abcd", k=1 -> need to make whole string palindrome -> 2
    assert sol.palindromePartition("abcd", 1) == 2, "Test 6 failed"

    print("All tests passed for 1278. Palindrome Partitioning III!")


if __name__ == "__main__":
    run_tests()
