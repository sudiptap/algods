"""
1626. Best Team With No Conflicts (Medium)
https://leetcode.com/problems/best-team-with-no-conflicts/

You are the manager of a basketball team. You want to pick the team with the
highest overall score. The score of the team is the sum of scores of all
players. However, there is a conflict if a younger player has a strictly
higher score than an older player. You must select a team with no conflicts.

Given two lists, scores and ages, return the highest overall score of all
possible teams.

Approach - LIS-style DP:
    1. Sort players by age, breaking ties by score.
    2. dp[i] = max total score of a valid team ending with player i.
    3. For each player i, look at all j < i. If scores[j] <= scores[i]
       (guaranteed no conflict since ages are sorted), we can extend.
       dp[i] = max(dp[j] + scores[i]) over valid j, or just scores[i].
    4. Answer = max(dp).

Time:  O(n^2)
Space: O(n)
"""

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """Return the highest overall score of a team with no conflicts.

        A conflict occurs when a younger player has a strictly higher score
        than an older player. Sort by age then score to reduce to an
        LIS-style problem on scores.

        Args:
            scores: List of player scores, 1 <= len(scores) <= 1000.
            ages: List of player ages, same length as scores.

        Returns:
            Maximum sum of scores for a conflict-free team.
        """
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]  # at minimum, take just this player
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: ages=[1,2,3,4,5], scores=[2,4,5,6,8] -> no conflicts, sum=25? nope
    # Actually: pick all 5 => ages sorted, scores sorted => 1+3+5+4+5=18? Re-read.
    assert sol.bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34

    # Example 2
    assert sol.bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16

    # Example 3
    assert sol.bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) == 6

    # Single player
    assert sol.bestTeamScore([10], [5]) == 10

    # All same age => no age conflicts, pick everyone
    assert sol.bestTeamScore([3, 1, 4, 1, 5], [5, 5, 5, 5, 5]) == 14

    # Two players, conflict
    assert sol.bestTeamScore([10, 5], [1, 2]) == 10  # younger has higher score

    print("All tests passed!")
