"""
1024. Video Stitching
https://leetcode.com/problems/video-stitching/

Pattern: 19 - Linear DP / Greedy

---
APPROACH: Greedy (Jump Game style)
- Sort clips by start time; for equal starts, prefer longer clip (larger end).
- Sweep left to right: maintain current end and farthest reachable end.
- When current position passes current end, we must use a new clip (increment count).
- If at any point farthest <= current end and we still haven't reached time, return -1.

Time:  O(n log n)   (sorting dominates)
Space: O(1)         (ignoring sort space)
---
"""

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """Return minimum number of clips to cover [0, time], or -1 if impossible."""
        clips.sort()
        count = 0
        cur_end = 0
        farthest = 0
        i = 0

        while cur_end < time:
            # Extend farthest with all clips starting <= cur_end
            while i < len(clips) and clips[i][0] <= cur_end:
                farthest = max(farthest, clips[i][1])
                i += 1

            if farthest == cur_end:
                # No clip can extend our coverage
                return -1

            cur_end = farthest
            count += 1

        return count


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.videoStitching(
        [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10
    ) == 3
    assert sol.videoStitching(
        [[0, 1], [1, 2]], 5
    ) == -1
    assert sol.videoStitching(
        [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3],
         [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6],
         [3, 4], [4, 5], [5, 7], [6, 9]], 9
    ) == 3
    assert sol.videoStitching([[0, 4], [2, 8]], 5) == 2
    assert sol.videoStitching([[0, 5]], 5) == 1
    assert sol.videoStitching([[1, 5]], 5) == -1  # doesn't start at 0

    print("Solution: all tests passed")
