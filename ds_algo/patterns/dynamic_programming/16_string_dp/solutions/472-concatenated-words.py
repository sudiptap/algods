"""
472. Concatenated Words (Hard)

Pattern: 16_string_dp
- Sort words by length. For each word, check if it can be formed by concatenating
  shorter words already in our dictionary (same logic as LeetCode 139 Word Break).

Approach:
- Sort words by length so that all potential component words are processed first.
- Maintain a set of known words.
- For each word, run a Word-Break-style DP:
    dp[i] = True if word[:i] can be segmented into words from the set.
- If dp[len(word)] is True, the word is a concatenated word.
- Add the word to the set regardless (it may be a component for longer words).

Complexity:
- Time:  O(N * L^2) where N = number of words, L = max word length
         (for each word we do an O(L^2) DP with substring checks)
- Space: O(N * L) for the word set
"""

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set()
        words.sort(key=len)
        result = []

        for word in words:
            if not word:
                continue
            if self._can_form(word, word_set):
                result.append(word)
            word_set.add(word)

        return result

    def _can_form(self, word: str, word_set: set) -> bool:
        if not word_set:
            return False
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    words1 = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
              "hippopotamuses", "rat", "ratcatdogcat"]
    result1 = sol.findAllConcatenatedWordsInADict(words1)
    assert set(result1) == {"catsdogcats", "dogcatsdog", "ratcatdogcat"}

    # Example 2
    words2 = ["cat", "dog", "catdog"]
    result2 = sol.findAllConcatenatedWordsInADict(words2)
    assert result2 == ["catdog"]

    # No concatenated words
    words3 = ["a", "b", "c"]
    result3 = sol.findAllConcatenatedWordsInADict(words3)
    assert result3 == []

    # Single character concatenation
    words4 = ["a", "b", "ab", "abc", "c"]
    result4 = sol.findAllConcatenatedWordsInADict(words4)
    assert set(result4) == {"ab", "abc"}

    # Empty input
    assert sol.findAllConcatenatedWordsInADict([]) == []

    print("All tests passed!")


if __name__ == "__main__":
    test()
