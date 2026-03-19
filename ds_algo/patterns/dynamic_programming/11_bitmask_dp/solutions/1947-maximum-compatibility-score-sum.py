"""
1947. Maximum Compatibility Score Sum (Medium)
https://leetcode.com/problems/maximum-compatibility-score-sum/

Given m students and m mentors (each with answers to n questions), assign
each student to a unique mentor to maximize total compatibility score.
Score = number of matching answers.

Pattern: Bitmask DP
Approach:
- Precompute score[i][j] = compatibility of student i with mentor j.
- dp[mask] = max total score when mentors in mask have been assigned
  to the first popcount(mask) students.
- For each mask, pos = popcount(mask) - 1. Try each set bit j in mask
  as the mentor for student pos.
- Base: dp[0] = 0.
- Answer: dp[(1<<m)-1].

Time:  O(2^m * m)
Space: O(2^m)
"""

from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """Return max total compatibility score.

        Args:
            students: m x n binary matrix of student answers.
            mentors: m x n binary matrix of mentor answers.

        Returns:
            Maximum compatibility score sum.
        """
        m = len(students)
        n = len(students[0])

        # Precompute compatibility scores
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(1 for k in range(n) if students[i][k] == mentors[j][k])

        full = 1 << m
        dp = [-1] * full
        dp[0] = 0

        for mask in range(1, full):
            pos = bin(mask).count('1') - 1  # student index (0-based)
            for j in range(m):
                if mask & (1 << j):
                    prev = dp[mask ^ (1 << j)]
                    if prev >= 0:
                        dp[mask] = max(dp[mask], prev + score[pos][j])

        return dp[full - 1]


# ---------- tests ----------
def test_max_compatibility():
    sol = Solution()

    # Example 1
    assert sol.maxCompatibilitySum(
        [[1,1,0],[1,0,1],[0,0,1]],
        [[1,0,0],[0,0,1],[1,1,0]]
    ) == 8

    # Example 2
    assert sol.maxCompatibilitySum(
        [[0,0],[0,0],[0,0]],
        [[1,1],[1,1],[1,1]]
    ) == 0

    # Perfect match
    assert sol.maxCompatibilitySum(
        [[1,0],[0,1]],
        [[1,0],[0,1]]
    ) == 4

    print("All tests passed for 1947. Maximum Compatibility Score Sum")


if __name__ == "__main__":
    test_max_compatibility()
