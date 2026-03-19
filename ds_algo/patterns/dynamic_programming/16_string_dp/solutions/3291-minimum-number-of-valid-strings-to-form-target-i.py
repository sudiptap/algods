"""
3291. Minimum Number of Valid Strings to Form Target I (Medium)

Pattern: 16_string_dp
- Given words array and target string, find minimum number of strings to concatenate
  to form target, where each string must be a prefix of some word in words.

Approach:
- Build a Trie from all words.
- dp[i] = minimum number of strings to form target[0..i-1].
- For each position i, walk the Trie matching target[i..] and update dp[i + matched_len].

Complexity:
- Time:  O(n * L) where n = len(target), L = max word length
- Space: O(sum of word lengths + n)
"""

from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        # Build trie
        trie = {}
        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]

        n = len(target)
        INF = float('inf')
        dp = [0] + [INF] * n

        for i in range(n):
            if dp[i] == INF:
                continue
            node = trie
            j = i
            while j < n and target[j] in node:
                node = node[target[j]]
                j += 1
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != INF else -1


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.minValidStrings(["abc", "aaaaa", "bcdef"], "aabcdabc") == 3

    # Example 2
    assert sol.minValidStrings(["abababab", "ab"], "ababaababa") == 2

    # Example 3
    assert sol.minValidStrings(["abcdef"], "xyz") == -1

    # Single char
    assert sol.minValidStrings(["a"], "a") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
