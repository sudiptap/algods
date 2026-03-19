"""
1986. Minimum Number of Work Sessions to Finish the Tasks (Medium)
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

Given tasks and sessionTime, find the minimum number of work sessions
to complete all tasks. Each session has at most sessionTime duration.

Pattern: Bitmask DP
Approach:
- dp[mask] = (min_sessions, min_remaining_time_in_current_session).
- For each mask, try adding each unset task.
- If task fits in current session, update remaining time.
- Otherwise, start a new session.
- Sort by (sessions, remaining) to minimize sessions first.

Time:  O(2^n * n)
Space: O(2^n)
"""

from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """Return minimum work sessions to finish all tasks.

        Args:
            tasks: Duration of each task.
            sessionTime: Maximum duration of a work session.

        Returns:
            Minimum number of sessions.
        """
        n = len(tasks)
        full = 1 << n
        # dp[mask] = (sessions, time_used_in_current_session)
        INF = (n + 1, 0)
        dp = [INF] * full
        dp[0] = (1, 0)  # 1 session open, 0 time used

        for mask in range(1, full):
            for j in range(n):
                if not (mask & (1 << j)):
                    continue
                prev = mask ^ (1 << j)
                sessions, used = dp[prev]
                if sessions >= INF[0]:
                    continue
                if used + tasks[j] <= sessionTime:
                    candidate = (sessions, used + tasks[j])
                else:
                    candidate = (sessions + 1, tasks[j])
                if candidate < dp[mask]:
                    dp[mask] = candidate

        return dp[full - 1][0]


# ---------- tests ----------
def test_min_sessions():
    sol = Solution()

    # Example 1
    assert sol.minSessions([1, 2, 3], 3) == 2

    # Example 2
    assert sol.minSessions([3, 1, 3, 1, 1], 8) == 2

    # Example 3
    assert sol.minSessions([1, 2, 3, 4, 5], 15) == 1

    # Each task = sessionTime
    assert sol.minSessions([5, 5, 5], 5) == 3

    # Single task
    assert sol.minSessions([3], 5) == 1

    print("All tests passed for 1986. Minimum Number of Work Sessions")


if __name__ == "__main__":
    test_min_sessions()
