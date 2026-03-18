"""
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

Pattern: 20 - Prefix/Suffix DP (also: Stack)

---
APPROACH 1: DP
- dp[i] = length of longest valid parentheses ENDING at index i
- If s[i] == '(':  dp[i] = 0 (can't end with open paren)
- If s[i] == ')':
    Case 1: s[i-1] == '('  → "()" pair → dp[i] = dp[i-2] + 2
    Case 2: s[i-1] == ')' and s[i - dp[i-1] - 1] == '('
            → the ')' at i closes the '(' just before the valid block ending at i-1
            → dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

Time: O(n)  Space: O(n)

APPROACH 2: Stack
- Push indices onto stack. Bottom of stack = boundary (last unmatched index).
- When we see ')' and can match, length = i - stack[-1]

Time: O(n)  Space: O(n)

APPROACH 3: Two-pass (optimal space)
- Left-to-right: track open/close counts, when equal record length, when close > open reset
- Right-to-left: mirror logic for open > close
- Handles both "(()" and "())" edge cases

Time: O(n)  Space: O(1)
---
"""


# ---------- Approach 1: DP ----------
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # case 1: "....()"
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif dp[i - 1] > 0:
                    # case 2: "....))" — look for matching '(' before inner block
                    j = i - dp[i - 1] - 1  # index of potential matching '('
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)

                max_len = max(max_len, dp[i])

        return max_len


# ---------- Approach 2: Stack ----------
class SolutionStack:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # boundary marker
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # new boundary
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len


# ---------- Approach 3: Two-pass O(1) space ----------
class SolutionTwoPass:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0

        # left to right
        open_count = close_count = 0
        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                close_count += 1
            if open_count == close_count:
                max_len = max(max_len, 2 * close_count)
            elif close_count > open_count:
                open_count = close_count = 0

        # right to left
        open_count = close_count = 0
        for ch in reversed(s):
            if ch == '(':
                open_count += 1
            else:
                close_count += 1
            if open_count == close_count:
                max_len = max(max_len, 2 * open_count)
            elif open_count > close_count:
                open_count = close_count = 0

        return max_len


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionStack, SolutionTwoPass]:
        sol = Sol()

        assert sol.longestValidParentheses("(()") == 2
        assert sol.longestValidParentheses(")()())") == 4
        assert sol.longestValidParentheses("") == 0
        assert sol.longestValidParentheses("()(()") == 2
        assert sol.longestValidParentheses("(()())") == 6
        assert sol.longestValidParentheses("()(())") == 6
        assert sol.longestValidParentheses(")(") == 0

        print(f"{Sol.__name__}: all tests passed")
