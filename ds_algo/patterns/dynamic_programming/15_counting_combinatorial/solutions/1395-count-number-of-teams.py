"""
1395. Count Number of Teams (Medium)
https://leetcode.com/problems/count-number-of-teams/

Pattern: Counting / Combinatorial DP

Given an array of unique integers `rating`, count the number of teams
(i, j, k) with i < j < k such that:
  - rating[i] < rating[j] < rating[k], OR
  - rating[i] > rating[j] > rating[k].

Approach:
    For each middle element j, count:
      - left_smaller  = elements to the left with rating < rating[j]
      - right_larger  = elements to the right with rating > rating[j]
      - left_larger   = elements to the left with rating > rating[j]
      - right_smaller = elements to the right with rating < rating[j]

    Ascending teams through j  = left_smaller * right_larger
    Descending teams through j = left_larger  * right_smaller

Time:  O(n^2)
Space: O(1)
"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """Count valid ascending or descending teams of size 3."""
        n = len(rating)
        result = 0

        for j in range(n):
            left_smaller = left_larger = 0
            right_smaller = right_larger = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1

            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                elif rating[k] < rating[j]:
                    right_smaller += 1

            result += left_smaller * right_larger + left_larger * right_smaller

        return result


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().numTeams([2, 5, 3, 4, 1]) == 3

def test_example2():
    assert Solution().numTeams([2, 1, 3]) == 0

def test_example3():
    assert Solution().numTeams([1, 2, 3, 4]) == 4

def test_descending():
    assert Solution().numTeams([4, 3, 2, 1]) == 4

def test_three_ascending():
    assert Solution().numTeams([1, 2, 3]) == 1

def test_three_descending():
    assert Solution().numTeams([3, 2, 1]) == 1

def test_minimum_no_team():
    assert Solution().numTeams([1, 2]) == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
