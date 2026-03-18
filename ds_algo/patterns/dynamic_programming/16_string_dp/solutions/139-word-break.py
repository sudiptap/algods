"""
139. Word Break
https://leetcode.com/problems/word-break/

Pattern: 16 - String DP

---
APPROACH: Bottom-up DP
- dp[i] = True if s[:i] can be segmented into dictionary words
- Base: dp[0] = True (empty string)
- Transition: dp[i] = True if there exists some j < i such that
  dp[j] is True AND s[j:i] is in wordDict
- Optimization: only check j values where i - j <= max word length

Time: O(n^2 * m) where n = len(s), m = avg word length for string comparison
      With set lookup and max_len optimization, effectively O(n * L) where L = max word length
Space: O(n + W) where W = total chars in wordDict
---
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(w) for w in wordDict) if wordDict else 0
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True  # empty string

        for i in range(1, n + 1):
            # Only check substrings up to max word length
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # no need to check further

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True

    # Example 2
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True

    # Example 3
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    # Single word match
    assert sol.wordBreak("hello", ["hello"]) is True

    # No match
    assert sol.wordBreak("hello", ["world"]) is False

    # Overlapping words
    assert sol.wordBreak("cars", ["car", "ca", "rs"]) is True

    # Empty string
    assert sol.wordBreak("", ["a"]) is True

    # Tricky: prefix trap
    assert sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]) is True  # 4+3

    # Tricky: cannot segment
    assert sol.wordBreak("aaaaaaa", ["aaaa", "aa"]) is False  # 7 can't be made from 4s and 2s

    print("Solution: all tests passed")
