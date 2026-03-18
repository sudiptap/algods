"""
241. Different Ways to Add Parentheses (Medium)

Pattern: Matrix Chain Multiplication / Divide and Conquer with Memoization
Approach:
    For every operator in the expression, split into left and right sub-expressions.
    Recursively compute all possible results for left and right halves.
    Combine every pair (l, r) using the operator.

    Memoize on the substring to avoid redundant work.

    This mirrors matrix chain multiplication: we try every possible "split point"
    (operator) and combine sub-problem results.

Complexity:
    Time:  O(n * 2^n) in the worst case (Catalan-number-like recursion tree)
    Space: O(n * 2^n) for memoization of all sub-expression results
"""

from typing import List
from functools import lru_cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Parse expression into tokens: numbers and operators
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                tokens.append(int(expression[i:j]))
                i = j
            else:
                tokens.append(expression[i])
                i += 1

        # tokens is like [num, op, num, op, num, ...]
        # numbers are at even indices, operators at odd indices
        nums = tokens[0::2]
        ops = tokens[1::2]
        n = len(nums)

        @lru_cache(maxsize=None)
        def solve(left: int, right: int) -> tuple:
            """Return all possible results for nums[left..right]."""
            if left == right:
                return (nums[left],)

            results = []
            for k in range(left, right):
                left_results = solve(left, k)
                right_results = solve(k + 1, right)
                op = ops[k]
                for l_val in left_results:
                    for r_val in right_results:
                        if op == '+':
                            results.append(l_val + r_val)
                        elif op == '-':
                            results.append(l_val - r_val)
                        else:
                            results.append(l_val * r_val)
            return tuple(results)

        return list(solve(0, n - 1))


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: "2-1-1" -> [0, 2]
    res1 = sorted(sol.diffWaysToCompute("2-1-1"))
    assert res1 == [0, 2], f"Expected [0, 2], got {res1}"

    # Example 2: "2*3-4*5" -> [-34, -14, -10, 10, 34] (unsorted from problem)
    res2 = sorted(sol.diffWaysToCompute("2*3-4*5"))
    assert res2 == [-34, -14, -10, -10, 10], f"Expected [-34, -14, -10, -10, 10], got {res2}"

    # Single number
    res3 = sol.diffWaysToCompute("42")
    assert res3 == [42], f"Expected [42], got {res3}"

    # Two numbers
    res4 = sol.diffWaysToCompute("3+2")
    assert res4 == [5], f"Expected [5], got {res4}"

    # All same operator
    res5 = sorted(sol.diffWaysToCompute("1+1+1+1"))
    assert res5 == [4, 4, 4, 4, 4], f"Expected [4,4,4,4,4], got {res5}"

    print("All tests passed!")


if __name__ == "__main__":
    test()
