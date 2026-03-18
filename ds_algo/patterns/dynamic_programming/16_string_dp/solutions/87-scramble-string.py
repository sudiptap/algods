"""
87. Scramble String
https://leetcode.com/problems/scramble-string/

Pattern: 16 - String DP (recursive split with memoization)

---
APPROACH: Top-down DP with memoization
- For s1[i1:i1+length] and s2[i2:i2+length], try every split point k (1..length-1)
- At each split, two possibilities:
    No swap:  isScramble(s1_left, s2_left) AND isScramble(s1_right, s2_right)
    Swap:     isScramble(s1_left, s2_right) AND isScramble(s1_right, s2_left)

- Pruning: if sorted chars don't match, impossible → return False early

State: (i1, i2, length) — 3 integers
Subproblems: O(n^3) states, each tries O(n) splits → O(n^4) total

Time: O(n^4)  Space: O(n^3)
---
"""

from functools import lru_cache
from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        @lru_cache(maxsize=None)
        def dp(i1: int, i2: int, length: int) -> bool:
            # base case: single char
            if length == 1:
                return s1[i1] == s2[i2]

            # pruning: character frequency must match
            if Counter(s1[i1:i1 + length]) != Counter(s2[i2:i2 + length]):
                return False

            # try every split point
            for k in range(1, length):
                # no swap: s1[:k] matches s2[:k], s1[k:] matches s2[k:]
                if dp(i1, i2, k) and dp(i1 + k, i2 + k, length - k):
                    return True

                # swap: s1[:k] matches s2[length-k:], s1[k:] matches s2[:length-k]
                if dp(i1, i2 + length - k, k) and dp(i1 + k, i2, length - k):
                    return True

            return False

        return dp(0, 0, len(s1))


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.isScramble("great", "rgeat") == True
    assert sol.isScramble("abcde", "caebd") == False
    assert sol.isScramble("a", "a") == True
    assert sol.isScramble("abc", "bca") == True
    assert sol.isScramble("ab", "ba") == True
    assert sol.isScramble("ab", "ab") == True
    assert sol.isScramble("abcd", "bdac") == False

    print("all tests passed")
