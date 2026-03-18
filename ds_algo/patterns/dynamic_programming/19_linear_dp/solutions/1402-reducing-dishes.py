"""
1402. Reducing Dishes (Hard)
https://leetcode.com/problems/reducing-dishes/

Pattern: Linear DP / Greedy

A chef has satisfaction values for n dishes. The like-time coefficient of a
dish is time[i] * satisfaction[i] where time[i] is the 1-indexed position
in the cooking order. Return the maximum sum of like-time coefficients.
You can discard any number of dishes.

Approach:
    Sort satisfaction in ascending order. Greedily include dishes from the
    highest satisfaction downward. Keep adding while the running suffix sum
    remains positive, because each new dish added at the front shifts all
    existing dishes one position later (adding suffix_sum to the total).

    Concretely:
      - Sort ascending.
      - Iterate from right to left, maintaining suffix_sum.
      - While suffix_sum > 0, it is beneficial to include the next dish.

Time:  O(n log n)  — dominated by sorting.
Space: O(1)  — in-place sort, constant extra space.
"""

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Return the maximum sum of like-time coefficients."""
        satisfaction.sort()
        suffix_sum = 0
        result = 0

        # Iterate from most satisfying dish backward
        for i in range(len(satisfaction) - 1, -1, -1):
            suffix_sum += satisfaction[i]
            if suffix_sum <= 0:
                break
            result += suffix_sum

        return result


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().maxSatisfaction([-1, -8, 0, 5, -9]) == 14

def test_example2():
    assert Solution().maxSatisfaction([4, 3, 2]) == 20

def test_example3():
    assert Solution().maxSatisfaction([-1, -4, -5]) == 0

def test_single_positive():
    assert Solution().maxSatisfaction([5]) == 5

def test_single_negative():
    assert Solution().maxSatisfaction([-3]) == 0

def test_all_zeros():
    assert Solution().maxSatisfaction([0, 0, 0]) == 0

def test_mixed():
    assert Solution().maxSatisfaction([-2, 5, -1, 0, 3, -3]) == 35


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
