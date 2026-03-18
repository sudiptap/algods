"""
140. Word Break II
https://leetcode.com/problems/word-break-ii/

Pattern: 16 - String DP

---
APPROACH: Backtracking with Memoization (Top-down DP)
- For each position, try every word in the dictionary that matches the current prefix
- Recursively solve the remaining suffix
- Memoize results: memo[start] = list of all sentences formable from s[start:]
- Pre-check with word break feasibility (optional but avoids TLE on adversarial inputs)

Time: O(n * 2^n) worst case — exponentially many valid segmentations possible
      In practice much better due to memoization and dictionary constraints
Space: O(n * 2^n) for storing all sentences in memo
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        max_len = max(len(w) for w in wordDict) if wordDict else 0

        @lru_cache(maxsize=None)
        def backtrack(start: int) -> List[tuple]:
            if start == len(s):
                return [()]  # one valid decomposition: empty

            results = []
            for end in range(start + 1, min(start + max_len, len(s)) + 1):
                word = s[start:end]
                if word in word_set:
                    for rest in backtrack(end):
                        results.append((word,) + rest)
            return results

        return [" ".join(words) for words in backtrack(0)]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    result = sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    assert sorted(result) == sorted(["cats and dog", "cat sand dog"]), f"Got {result}"

    # Example 2
    result = sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
    expected = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    assert sorted(result) == sorted(expected), f"Got {result}"

    # Example 3
    result = sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert result == [], f"Got {result}"

    # Single word
    result = sol.wordBreak("hello", ["hello"])
    assert result == ["hello"]

    # Multiple ways to split
    result = sol.wordBreak("aaa", ["a", "aa", "aaa"])
    expected = ["a a a", "a aa", "aa a", "aaa"]
    assert sorted(result) == sorted(expected), f"Got {result}"

    print("Solution: all tests passed")
