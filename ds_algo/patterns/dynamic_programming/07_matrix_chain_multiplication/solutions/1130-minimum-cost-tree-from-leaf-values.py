"""
1130. Minimum Cost Tree From Leaf Values (Medium)
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

Pattern: 07 - Matrix Chain Multiplication (Interval DP)

Given an array arr of positive integers, build a binary tree such that:
  - Each leaf has a value from arr (in-order).
  - Each non-leaf node's value = product of max of left subtree leaves and
    max of right subtree leaves.
  - Minimise the sum of all non-leaf node values.

Approach 1 – Interval DP (like matrix chain multiplication):
    dp[i][j] = min cost to build a tree from arr[i..j].
    For every split k in [i, j-1]:
        dp[i][j] = min( dp[i][k] + dp[k+1][j] + max(arr[i..k]) * max(arr[k+1..j]) )
    Base: dp[i][i] = 0 (single leaf, no non-leaf node).

Approach 2 – Greedy with monotonic stack (O(n)):
    Greedily remove the smaller of two adjacent elements, adding the
    product to cost. Use a decreasing stack.

    Implemented below (both approaches).

Time:  O(n^3) interval DP / O(n) greedy
Space: O(n^2) / O(n)
"""

from typing import List


# ---------- Approach 1: Interval DP ----------
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """Return the minimum sum of non-leaf node values (interval DP)."""
        n = len(arr)

        # Precompute range maxima
        mx = [[0] * n for _ in range(n)]
        for i in range(n):
            mx[i][i] = arr[i]
            for j in range(i + 1, n):
                mx[i][j] = max(mx[i][j - 1], arr[j])

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):          # subarray length
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k + 1][j] + mx[i][k] * mx[k + 1][j],
                    )

        return dp[0][n - 1]


# ---------- Approach 2: Greedy monotonic stack ----------
class SolutionGreedy:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """Return the minimum sum of non-leaf node values (greedy stack)."""
        stack = [float("inf")]
        cost = 0

        for val in arr:
            while stack[-1] <= val:
                mid = stack.pop()
                cost += mid * min(stack[-1], val)
            stack.append(val)

        # Remaining elements in stack (excluding sentinel)
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]

        return cost


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().mctFromLeafValues([6, 2, 4]) == 32

def test_example1_greedy():
    assert SolutionGreedy().mctFromLeafValues([6, 2, 4]) == 32

def test_two_elements():
    assert Solution().mctFromLeafValues([3, 5]) == 15
    assert SolutionGreedy().mctFromLeafValues([3, 5]) == 15

def test_four_elements():
    arr = [6, 2, 4, 8]
    res_dp = Solution().mctFromLeafValues(arr)
    res_greedy = SolutionGreedy().mctFromLeafValues(arr)
    assert res_dp == res_greedy

def test_sorted_ascending():
    arr = [1, 2, 3, 4]
    assert Solution().mctFromLeafValues(arr) == SolutionGreedy().mctFromLeafValues(arr)

def test_single_element():
    assert Solution().mctFromLeafValues([7]) == 0
    assert SolutionGreedy().mctFromLeafValues([7]) == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
