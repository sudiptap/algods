"""
2900. Longest Unequal Adjacent Groups Subsequence I
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

Pattern: 05 - LIS (Greedy alternating)

---
APPROACH: Greedily pick words where consecutive groups differ. Just iterate
and pick whenever the group changes from the last picked.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        last_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.getLongestSubsequence(["e", "a", "b"], [0, 0, 1]) == ["e", "b"]
    assert sol.getLongestSubsequence(["a", "b", "c", "d"], [1, 0, 1, 1]) == ["a", "b", "c"]

    print("All tests passed!")
