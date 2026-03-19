"""
2901. Longest Unequal Adjacent Groups Subsequence II
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

Pattern: 05 - LIS (LIS-style with hamming distance check)

---
APPROACH: dp[i] = length of longest valid subsequence ending at i.
For each i, check all j < i where groups[j] != groups[i], len(words[j]) ==
len(words[i]), and hamming distance == 1. Track parent pointers for reconstruction.

Time: O(n^2 * L) where L = max word length  Space: O(n)
---
"""

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str],
                                     groups: List[int]) -> List[str]:
        def hamming(a, b):
            if len(a) != len(b):
                return -1
            return sum(x != y for x, y in zip(a, b))

        dp = [1] * n
        parent = [-1] * n

        for i in range(1, n):
            for j in range(i):
                if groups[j] != groups[i] and hamming(words[j], words[i]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

        # Find best ending index
        best = max(range(n), key=lambda i: dp[i])

        # Reconstruct
        result = []
        while best != -1:
            result.append(words[best])
            best = parent[best]
        return result[::-1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.getWordsInLongestSubsequence(3, ["bab", "dab", "cab"], [1, 2, 2]) == ["bab", "dab"]
    r = sol.getWordsInLongestSubsequence(4, ["a", "b", "c", "d"], [1, 2, 3, 4])
    assert len(r) == 4  # a->b->c->d all have hamming dist 1 and different groups

    print("All tests passed!")
