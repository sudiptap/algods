"""
2707. Extra Characters in a String
https://leetcode.com/problems/extra-characters-in-a-string/

Pattern: 16 - String DP

---
APPROACH: Linear DP with dictionary word matching
- dp[i] = minimum number of extra characters in s[:i].
- Base case: dp[0] = 0 (empty prefix has no extra chars).
- Transition: for each position i, either s[i-1] is extra (dp[i] = dp[i-1] + 1),
  or some dictionary word ends at position i-1.
  For each word w in dictionary, if s[i-len(w):i] == w, then dp[i] = min(dp[i], dp[i-len(w)]).
- Using a set for O(1) lookup and checking all possible word lengths.

Time:  O(n * m * L) where m = number of words, L = max word length
Space: O(n + total chars in dictionary)
---
"""

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """Return the minimum number of extra characters left after optimal concatenation."""
        n = len(s)
        word_set = set(dictionary)
        # Collect all unique word lengths for efficient checking
        word_lens = set(len(w) for w in dictionary)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Worst case: character at i-1 is extra
            dp[i] = dp[i - 1] + 1
            # Try every possible word ending at position i
            for wl in word_lens:
                if wl <= i and s[i - wl : i] in word_set:
                    dp[i] = min(dp[i], dp[i - wl])

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minExtraChar("leetscode", ["leet", "code", "leetcode"]) == 1
    # Example 2
    assert sol.minExtraChar("sayhelloworld", ["hello", "world"]) == 3
    # Entire string is one word
    assert sol.minExtraChar("hello", ["hello"]) == 0
    # No matches at all
    assert sol.minExtraChar("abc", ["xyz"]) == 3
    # Single character match
    assert sol.minExtraChar("a", ["a"]) == 0
    # Overlapping words, pick best
    assert sol.minExtraChar("abcd", ["ab", "cd", "abcd"]) == 0

    print("Solution: all tests passed")
