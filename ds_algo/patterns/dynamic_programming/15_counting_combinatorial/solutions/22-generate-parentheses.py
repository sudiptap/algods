"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Pattern: 15 - Counting/Combinatorial DP (also: Backtracking)

---
APPROACH 1: Backtracking (most natural for interviews)
- At each position, choose '(' or ')'
- Constraints: open < n (can add '('), close < open (can add ')')
- When len(path) == 2*n, we have a valid combination

Time: O(4^n / sqrt(n))  — Catalan number bound
Space: O(n) recursion depth

APPROACH 2: DP (build from smaller subproblems)
- dp[i] = all valid strings with i pairs
- A valid string with i pairs can be written as: "(" + dp[j] + ")" + dp[i-1-j]
  where j ranges from 0 to i-1
- The first '(' must close somewhere, and what's inside is dp[j],
  what's after is dp[i-1-j]

Time: O(4^n / sqrt(n))  Space: O(4^n / sqrt(n)) to store results
---
"""

from typing import List


# ---------- Approach 1: Backtracking ----------
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path: list, open_count: int, close_count: int):
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count)
                path.pop()

            if close_count < open_count:
                path.append(")")
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return result


# ---------- Approach 2: DP ----------
class SolutionDP:
    def generateParenthesis(self, n: int) -> List[str]:
        # dp[i] = list of all valid combos with i pairs
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                # first '(' closes after j pairs inside, then i-1-j pairs after
                for inside in dp[j]:
                    for after in dp[i - 1 - j]:
                        dp[i].append(f"({inside}){after}")

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    expected_3 = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    expected_1 = ["()"]

    for Sol in [Solution, SolutionDP]:
        sol = Sol()

        assert sorted(sol.generateParenthesis(3)) == expected_3
        assert sol.generateParenthesis(1) == expected_1
        assert sol.generateParenthesis(0) == [""] if isinstance(sol, SolutionDP) else True
        assert len(sol.generateParenthesis(4)) == 14  # Catalan(4) = 14

        print(f"{Sol.__name__}: all tests passed")
