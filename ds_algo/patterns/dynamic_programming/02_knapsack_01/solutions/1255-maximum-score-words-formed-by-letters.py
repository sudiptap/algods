"""
1255. Maximum Score Words Formed by Letters (Hard)

Pattern: 02_knapsack_01
- Select a subset of words (each used at most once) that can be formed from available
  letters, maximizing total score.

Approach:
- Since len(words) <= 14, enumerate all 2^n subsets via bitmask.
- For each subset, check if the total letter usage fits within available letters.
- If valid, compute the total score and track the maximum.
- Precompute letter counts for each word and the available letters.

Complexity:
- Time:  O(2^n * n * 26) where n = len(words), simplified to O(2^n * 26)
- Space: O(n * 26)
"""

from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        avail = Counter(letters)

        # Precompute word counts and scores
        word_counts = []
        word_scores = []
        for w in words:
            cnt = Counter(w)
            word_counts.append(cnt)
            s = sum(score[ord(c) - ord('a')] for c in w)
            word_scores.append(s)

        best = 0
        for mask in range(1 << n):
            total_count = Counter()
            total_score = 0
            valid = True
            for i in range(n):
                if mask & (1 << i):
                    total_count += word_counts[i]
                    total_score += word_scores[i]

            # Check feasibility
            for ch, cnt in total_count.items():
                if cnt > avail.get(ch, 0):
                    valid = False
                    break

            if valid:
                best = max(best, total_score)

        return best


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxScoreWords(
        ["dog", "cat", "dad", "good"],
        ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ) == 23  # "dad" + "good"

    # Example 2
    assert sol.maxScoreWords(
        ["xxxz", "ax", "bx", "cx"],
        ["z", "a", "b", "c", "x", "x", "x"],
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    ) == 27  # "ax" + "bx" + "cx"

    # Example 3
    assert sol.maxScoreWords(
        ["leetcode"],
        ["l", "e", "t", "c", "o", "d"],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ) == 0  # not enough letters (need 2 e's)

    # No words
    assert sol.maxScoreWords([], ["a"], [1] + [0] * 25) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
