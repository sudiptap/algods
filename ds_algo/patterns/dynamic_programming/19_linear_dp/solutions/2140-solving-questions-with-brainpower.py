"""
2140. Solving Questions With Brainpower (Medium)
https://leetcode.com/problems/solving-questions-with-brainpower/

Pattern: Linear DP

You are given a 0-indexed 2D integer array questions where
questions[i] = [points_i, brainpower_i]. If you solve question i, you earn
points_i points but must skip the next brainpower_i questions. Return the
maximum points you can earn.

Approach:
    Work backwards from the last question. For each question i, you have two
    choices: skip it (dp[i] = dp[i+1]) or solve it and jump ahead
    (dp[i] = points[i] + dp[i + brainpower[i] + 1]). Take the max.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """Return the maximum points earned from the exam."""
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            # Index to jump to after solving question i
            nxt = i + brainpower + 1
            solve = points + (dp[nxt] if nxt <= n else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)

        return dp[0]


# ---------- Tests ----------
import unittest


class TestMostPoints(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
        self.assertEqual(self.sol.mostPoints(questions), 5)

    def test_example2(self):
        questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        self.assertEqual(self.sol.mostPoints(questions), 7)

    def test_single(self):
        self.assertEqual(self.sol.mostPoints([[5, 1]]), 5)

    def test_all_skip(self):
        # Best to solve first (10) and skip the rest
        questions = [[10, 5], [1, 0], [1, 0], [1, 0]]
        self.assertEqual(self.sol.mostPoints(questions), 10)

    def test_no_brainpower(self):
        # brainpower=0 means no skip, solve all
        questions = [[1, 0], [2, 0], [3, 0]]
        self.assertEqual(self.sol.mostPoints(questions), 6)


if __name__ == "__main__":
    unittest.main()
