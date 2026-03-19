"""
553. Optimal Division (Medium)
https://leetcode.com/problems/optimal-division/

Pattern: String DP / Math

Given a list of positive integers, add parentheses to maximize the
result of dividing them sequentially. Return the expression as a string.

Approach:
    Math trick: a / b / c / d / ... is minimized without parentheses.
    To maximize, we want a / (b / c / d / ...) = a * c * d * ... / b.
    So we just wrap everything after the first number in parentheses:
    "a/(b/c/d/...)".

    Special cases: 1 number -> just the number, 2 numbers -> "a/b".

Time:  O(n)
Space: O(n) for output string
"""

from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """Return expression string that maximizes the division result."""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"

        inner = "/".join(str(x) for x in nums[1:])
        return f"{nums[0]}/({inner})"


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().optimalDivision([1000, 100, 10, 2]) == "1000/(100/10/2)"

def test_example2():
    assert Solution().optimalDivision([2, 3, 4]) == "2/(3/4)"

def test_single():
    assert Solution().optimalDivision([5]) == "5"

def test_two():
    assert Solution().optimalDivision([10, 2]) == "10/2"

def test_five_elements():
    assert Solution().optimalDivision([1, 2, 3, 4, 5]) == "1/(2/3/4/5)"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
