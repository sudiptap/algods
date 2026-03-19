"""
2019. The Score of Students Solving Math Expression (Hard)
https://leetcode.com/problems/the-score-of-students-solving-math-expression/

Given a math expression (single digits, + and *) and student answers,
score: 5 for correct, 2 if the answer is obtainable by any order of
operations (not just standard precedence), 0 otherwise.

Pattern: Interval DP
Approach:
- Compute the correct answer using standard precedence.
- Use interval DP to find all possible results from evaluating
  subexpressions in any order.
- dp[i][j] = set of all possible values from evaluating the
  subexpression from operand i to operand j.
- For each split point k with operator between operand k and k+1,
  combine all pairs from dp[i][k] and dp[k+1][j].
- Cap values at 1000 to limit set sizes.

Time:  O(n^3 * S^2) where S = possible values per interval (bounded by 1000)
Space: O(n^2 * S)
"""

from typing import List


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        """Return total score of student answers.

        Args:
            s: Math expression string.
            answers: List of student answers.

        Returns:
            Total score.
        """
        # Parse operands and operators
        operands = []
        operators = []
        for ch in s:
            if ch.isdigit():
                operands.append(int(ch))
            else:
                operators.append(ch)

        n = len(operands)

        # Correct answer with standard precedence
        correct = eval(s)

        # Interval DP: dp[i][j] = set of possible values
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = {operands[i]}

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    op = operators[k]
                    for a in dp[i][k]:
                        for b in dp[k + 1][j]:
                            if op == '+':
                                val = a + b
                            else:
                                val = a * b
                            if val <= 1000:
                                dp[i][j].add(val)

        all_possible = dp[0][n - 1]

        total = 0
        for ans in answers:
            if ans == correct:
                total += 5
            elif ans in all_possible:
                total += 2

        return total


# ---------- tests ----------
def test_score_of_students():
    sol = Solution()

    # Example 1: "7+3*1*2" correct=13
    assert sol.scoreOfStudents("7+3*1*2", [20, 13, 42]) == 7

    # Example 2: "3+5*2" correct=13
    assert sol.scoreOfStudents("3+5*2", [13, 0, 10, 13, 13, 16, 16]) == 19

    # Example 3
    assert sol.scoreOfStudents("6+0*1", [12, 9, 6, 4, 8, 6]) == 10

    # Simple
    assert sol.scoreOfStudents("1+2", [3]) == 5
    assert sol.scoreOfStudents("1+2", [5]) == 0

    print("All tests passed for 2019. The Score of Students Solving Math Expression")


if __name__ == "__main__":
    test_score_of_students()
