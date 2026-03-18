"""
1014. Best Sightseeing Pair
https://leetcode.com/problems/best-sightseeing-pair/

Pattern: 19 - Linear DP

---
APPROACH: Decompose the score and track running max
- Score = values[i] + i + values[j] - j  for i < j.
- As we scan j left to right, maintain max_left = max(values[i] + i) for all
  i < j. Then the best score ending at j is max_left + values[j] - j.
- Update answer and max_left in one pass.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """Return the maximum score of a sightseeing pair (i, j) with i < j."""
        max_left = values[0] + 0  # best values[i] + i seen so far
        best = 0

        for j in range(1, len(values)):
            best = max(best, max_left + values[j] - j)
            max_left = max(max_left, values[j] + j)

        return best


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11  # i=0,j=2: 8+5-2=11
    assert sol.maxScoreSightseeingPair([1, 2]) == 2              # 1+2-1=2
    assert sol.maxScoreSightseeingPair([1, 3, 5]) == 7           # i=1,j=2: 3+5-1=7
    assert sol.maxScoreSightseeingPair([7, 2, 6, 6, 9, 4, 3]) == 14  # i=0,j=4
    assert sol.maxScoreSightseeingPair([1, 1, 1, 1]) == 1

    print("all tests passed")
