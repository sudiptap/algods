"""
1335. Minimum Difficulty of a Job Schedule (Hard)
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

Problem:
    Schedule jobs over d days in order. Each day must have at least one job.
    The difficulty of a day is the max difficulty of jobs done that day.
    Minimize the sum of difficulties over all days.

Pattern: 19 - Linear DP

Approach:
    1. dp[i][d] = minimum total difficulty to schedule first i jobs in d days.
    2. Transition: dp[i][d] = min over j in [d-1, i-1] of
       dp[j][d-1] + max(jobDifficulty[j..i-1]).
    3. Base case: dp[i][1] = max(jobDifficulty[0..i-1]).
    4. If n < d, return -1 (not enough jobs).

Complexity:
    Time:  O(n^2 * d) - for each (i, d) pair, scan back through j values
    Space: O(n * d) for the DP table
"""

from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        INF = float('inf')
        dp = [[INF] * (d + 1) for _ in range(n + 1)]

        # Base: dp[i][1] = max of first i jobs
        cur_max = 0
        for i in range(1, n + 1):
            cur_max = max(cur_max, jobDifficulty[i - 1])
            dp[i][1] = cur_max

        for day in range(2, d + 1):
            for i in range(day, n + 1):
                max_diff = 0
                for j in range(i, day - 1, -1):
                    max_diff = max(max_diff, jobDifficulty[j - 1])
                    dp[i][day] = min(dp[i][day], dp[j - 1][day - 1] + max_diff)

        return dp[n][d]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.minDifficulty([6, 5, 4, 3, 2, 1], 2) == 7, "Test 1 failed"

    # Test 2
    assert sol.minDifficulty([9, 9, 9], 4) == -1, "Test 2 failed"

    # Test 3
    assert sol.minDifficulty([1, 1, 1], 3) == 3, "Test 3 failed"

    # Test 4
    assert sol.minDifficulty([7, 1, 7, 1, 7, 1], 3) == 15, "Test 4 failed"

    # Test 5
    assert sol.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6) == 843, "Test 5 failed"

    # Test 6: single job single day
    assert sol.minDifficulty([5], 1) == 5, "Test 6 failed"

    print("All tests passed for 1335. Minimum Difficulty of a Job Schedule!")


if __name__ == "__main__":
    run_tests()
