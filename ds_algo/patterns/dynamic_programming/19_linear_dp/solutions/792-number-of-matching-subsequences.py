"""
792. Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/

Pattern: 19 - Linear DP

---
APPROACH: Bucket pointers per starting character
- Group words by their first character into 26 buckets.
- Iterate through each character in s. For each char c, process all
  words in bucket[c]: advance their pointer. If the word is fully
  matched, increment count. Otherwise, move word to the bucket of
  its next needed character.
- This avoids re-scanning s for each word.

Time: O(|s| + sum(|word|))  Space: O(number of words)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Each bucket entry is (word, index_into_word)
        buckets = defaultdict(list)
        for word in words:
            buckets[word[0]].append((word, 0))

        count = 0
        for c in s:
            current = buckets[c]
            buckets[c] = []
            for word, idx in current:
                idx += 1
                if idx == len(word):
                    count += 1
                else:
                    buckets[word[idx]].append((word, idx))

        return count


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) == 3
    assert sol.numMatchingSubseq("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]) == 2
    assert sol.numMatchingSubseq("a", ["a", "b", "a"]) == 2
    assert sol.numMatchingSubseq("abc", ["abc", "ab", "a", "d"]) == 3
    assert sol.numMatchingSubseq("aaaa", ["a", "aa", "aaa", "aaaa", "aaaaa"]) == 4

    print("all tests passed")
