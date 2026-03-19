"""
3332. Maximum Points Tourist Can Earn (Medium)

Pattern: 19_linear_dp
- Tourist visits cities over k days. stayScore[i][j] = points staying in city j on day i.
  travelScore[i][j] = points traveling from city i to city j. Maximize total points.

Approach:
- dp[day][city] = max points earned up to this day ending in this city.
- Transition: dp[day+1][j] = max over all cities i of:
  - dp[day][j] + stayScore[day][j] (stay in j)
  - dp[day][i] + travelScore[i][j] (travel from i to j)

Complexity:
- Time:  O(k * n^2)
- Space: O(n) with rolling array
"""

from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n  # dp[city] at current day

        for day in range(k):
            new_dp = [0] * n
            for j in range(n):
                # Stay in j
                new_dp[j] = dp[j] + stayScore[day][j]
                # Travel from i to j
                for i in range(n):
                    if i != j:
                        new_dp[j] = max(new_dp[j], dp[i] + travelScore[i][j])
            dp = new_dp

        return max(dp)


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxScore(2, 1, [[2, 3]], [[0, 2], [1, 0]]) == 3

    # Example 2
    assert sol.maxScore(3, 2, [[3, 4, 2], [2, 1, 2]], [[0, 2, 1], [2, 0, 4], [3, 2, 0]]) == 8

    print("All tests passed!")


if __name__ == "__main__":
    test()
