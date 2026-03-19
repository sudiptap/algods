"""
3302. Find the Lexicographically Smallest Valid Sequence (Hard)

Pattern: 16_string_dp
- Find lexicographically smallest subsequence indices of word1 that form word2,
  allowing at most one character mismatch.

Approach:
- Precompute suffix[i] = how many chars of word2 (from the end) can be matched
  starting from word1[i] going right. This tells us: from position i in word1,
  we can match word2[len(word2)-suffix[i]:].
- Greedily match from left. At each step, try to match without using the wildcard.
  If we must use wildcard, use it at the earliest position where the remaining
  suffix can still be matched.

Complexity:
- Time:  O(n + m) where n = len(word1), m = len(word2)
- Space: O(n + m)
"""

from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suffix[i] = number of characters of word2 matchable from the end
        # starting at word1[i] going right
        suffix = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suffix[i] = suffix[i + 1] + 1
                j -= 1

        result = []
        wi = 0  # position in word2
        used_wild = False

        for i in range(n):
            if wi >= m:
                break
            remaining = m - wi  # chars of word2 still to match

            if word1[i] == word2[wi]:
                result.append(i)
                wi += 1
            elif not used_wild:
                # Use wildcard here if remaining suffix can cover the rest
                # After using wildcard at position wi, we need to match word2[wi+1:]
                # from word1[i+1:]. suffix[i+1] tells how many from end we can match.
                if suffix[i + 1] >= m - wi - 1:
                    result.append(i)
                    wi += 1
                    used_wild = True

        if len(result) == m:
            return result
        return []


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.validSequence("vbcca", "abc") == [0, 1, 2]

    # Example 2
    assert sol.validSequence("bacdc", "abc") == [1, 2, 4]

    # Example 3
    assert sol.validSequence("aaaaaa", "aaabc") == []

    # Example 4
    assert sol.validSequence("abc", "ab") == [0, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
