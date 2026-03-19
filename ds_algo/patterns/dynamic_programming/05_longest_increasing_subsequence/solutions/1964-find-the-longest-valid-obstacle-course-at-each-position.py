"""
1964. Find the Longest Valid Obstacle Course at Each Position (Hard)
https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

For each position i, find the length of the longest non-decreasing
subsequence ending at i.

Pattern: Longest Increasing Subsequence (with bisect)
Approach:
- Maintain a tails array (like LIS but for non-decreasing).
- For each obstacle, use bisect_right to find insertion point (allows
  equal elements since non-decreasing).
- The answer for position i = insertion_point + 1.
- Update tails at the insertion point.

Time:  O(n log n)
Space: O(n)
"""

from typing import List
from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """Return longest valid obstacle course length ending at each position.

        Args:
            obstacles: Array of obstacle heights.

        Returns:
            Array where ans[i] = longest non-decreasing subsequence ending at i.
        """
        tails = []
        result = []

        for obs in obstacles:
            pos = bisect_right(tails, obs)
            if pos == len(tails):
                tails.append(obs)
            else:
                tails[pos] = obs
            result.append(pos + 1)

        return result


# ---------- tests ----------
def test_longest_obstacle_course():
    sol = Solution()

    # Example 1
    assert sol.longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]

    # Example 2
    assert sol.longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]

    # Example 3
    assert sol.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2]

    # All same
    assert sol.longestObstacleCourseAtEachPosition([5, 5, 5]) == [1, 2, 3]

    # Single element
    assert sol.longestObstacleCourseAtEachPosition([7]) == [1]

    print("All tests passed for 1964. Find the Longest Valid Obstacle Course")


if __name__ == "__main__":
    test_longest_obstacle_course()
