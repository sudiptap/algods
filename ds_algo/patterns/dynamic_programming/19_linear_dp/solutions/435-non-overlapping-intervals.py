"""
435. Non-overlapping Intervals (Medium)

Given an array of intervals where intervals[i] = [start_i, end_i], return the
minimum number of intervals you need to remove to make the rest non-overlapping.

Approach:
    Sort intervals by end time. Greedily keep as many non-overlapping intervals
    as possible by always picking the interval that ends earliest. The answer is
    n - max_non_overlapping.

Time:  O(n log n)  — sorting dominates
Space: O(1)        — aside from sort's internal space
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Return min intervals to remove so the rest are non-overlapping."""
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # sort by end time

        non_overlapping = 1
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:  # no overlap
                non_overlapping += 1
                prev_end = intervals[i][1]

        return len(intervals) - non_overlapping


# ── Tests ──────────────────────────────────────────────────────────────────
def test_example1():
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

def test_example2():
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2

def test_example3():
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0

def test_single():
    assert Solution().eraseOverlapIntervals([[0, 5]]) == 0

def test_empty():
    assert Solution().eraseOverlapIntervals([]) == 0

def test_all_overlap():
    assert Solution().eraseOverlapIntervals([[1, 4], [2, 5], [3, 6]]) == 2

def test_nested():
    assert Solution().eraseOverlapIntervals([[1, 10], [2, 3], [4, 5], [6, 7]]) == 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
