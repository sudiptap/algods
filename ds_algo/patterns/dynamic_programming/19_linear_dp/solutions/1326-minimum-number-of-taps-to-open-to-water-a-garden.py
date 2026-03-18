"""
1326. Minimum Number of Taps to Open to Water a Garden (Hard)
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

Pattern: 19 - Linear DP

---
APPROACH: Convert to intervals + Jump Game II greedy
- Each tap i with range ranges[i] covers interval [i - ranges[i], i + ranges[i]].
- Convert to a "max reach from each start" array: for each interval [l, r],
  update max_reach[max(0, l)] = max(max_reach[max(0, l)], min(n, r)).
- Then apply the Jump Game II greedy: track current end, farthest reachable,
  and number of jumps (taps opened).

Time:  O(n)
Space: O(n)
---
"""

from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """Return the minimum number of taps to water the entire garden [0, n],
        or -1 if impossible."""
        # max_reach[i] = farthest right we can reach starting from position i
        max_reach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            max_reach[left] = max(max_reach[left], right)

        # Jump Game II greedy
        taps = 0
        cur_end = 0
        farthest = 0

        for i in range(n + 1):
            if i > farthest:
                return -1
            farthest = max(farthest, max_reach[i])
            if i == cur_end and i < n:
                taps += 1
                cur_end = farthest

        return taps


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minTaps(5, [3, 4, 1, 1, 0, 0]) == 1

    # Example 2
    assert sol.minTaps(3, [0, 0, 0, 0]) == -1

    # Single segment covers all
    assert sol.minTaps(3, [0, 0, 3, 0]) == 1

    # n=0, already watered
    assert sol.minTaps(0, [0]) == 0

    # Each tap covers exactly its spot
    assert sol.minTaps(1, [1, 0]) == 1

    # Overlapping taps needed
    assert sol.minTaps(7, [1, 2, 1, 0, 2, 1, 0, 1]) == 3

    print("all tests passed")
