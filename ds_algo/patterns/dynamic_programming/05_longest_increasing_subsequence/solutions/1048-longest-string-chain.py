"""
1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: DP with hash map
- Sort words by length.
- dp[word] = length of longest chain ending at word.
- For each word, try removing each character to form a predecessor.
  If predecessor exists in dp, dp[word] = max(dp[word], dp[pred] + 1).
- Answer is max(dp.values()).

Time:  O(n * L^2)  where L = max word length (up to 16), n = number of words
       (for each word, we generate L predecessors, each costing O(L) to build)
Space: O(n * L)    (hash map storing all words)
---
"""

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """Return the length of the longest possible word chain."""
        words.sort(key=len)
        dp = {}

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)

        return max(dp.values())


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert sol.longestStrChain(
        ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    ) == 5
    assert sol.longestStrChain(["abcd", "dbqca"]) == 1
    assert sol.longestStrChain(["a"]) == 1

    print("Solution: all tests passed")
