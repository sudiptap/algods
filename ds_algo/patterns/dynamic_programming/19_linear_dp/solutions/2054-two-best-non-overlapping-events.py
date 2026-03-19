"""
2054. Two Best Non-Overlapping Events (Medium)
https://leetcode.com/problems/two-best-non-overlapping-events/

Given events [start, end, value], attend at most two non-overlapping
events. Return maximum sum of values.

Pattern: Linear DP (Sort + Binary Search)
Approach:
- Sort events by end time.
- Track max value seen so far (prefix max).
- For each event, binary search for the latest event that ends before
  this event starts. Add its prefix max value.
- Answer = max over all events of (value + best_non_overlapping_before).

Time:  O(n log n)
Space: O(n)
"""

from typing import List
from bisect import bisect_right


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """Return max value sum of at most two non-overlapping events.

        Args:
            events: List of [start, end, value].

        Returns:
            Maximum total value.
        """
        events.sort(key=lambda x: x[1])
        n = len(events)

        # ends[i] = end time of event i (sorted)
        ends = [e[1] for e in events]

        # prefix_max[i] = max value among events[0..i]
        prefix_max = [0] * n
        prefix_max[0] = events[0][2]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], events[i][2])

        ans = 0
        for i in range(n):
            start, end, val = events[i]
            ans = max(ans, val)  # take just this event

            # Find latest event ending before start
            idx = bisect_right(ends, start - 1) - 1
            if idx >= 0:
                ans = max(ans, val + prefix_max[idx])

        return ans


# ---------- tests ----------
def test_max_two_events():
    sol = Solution()

    # Example 1
    assert sol.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]) == 4

    # Example 2
    assert sol.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]) == 5

    # Example 3
    assert sol.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]) == 8

    # Single event
    assert sol.maxTwoEvents([[1,2,10]]) == 10

    # Two non-overlapping
    assert sol.maxTwoEvents([[1,2,5],[3,4,5]]) == 10

    print("All tests passed for 2054. Two Best Non-Overlapping Events")


if __name__ == "__main__":
    test_max_two_events()
