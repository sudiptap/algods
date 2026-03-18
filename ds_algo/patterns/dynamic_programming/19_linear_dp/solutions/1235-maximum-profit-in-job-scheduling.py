"""
1235. Maximum Profit in Job Scheduling (Hard)
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

You have n jobs where job i starts at startTime[i], ends at endTime[i], and
earns profit[i]. Find the maximum profit you can achieve such that no two
selected jobs overlap. A job ending at time X can be followed by one starting
at time X.

Pattern: Linear DP + Binary Search
- Sort jobs by end time.
- dp[i] = maximum profit considering the first i jobs.
- For each job i, binary search for the latest job j that ends <= start of job i.
- Transition: dp[i] = max(dp[i-1], profit[i] + dp[j])
  (either skip job i, or take job i plus best profit from non-overlapping jobs).

Time:  O(n log n)
Space: O(n)
"""

from typing import List
import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Return maximum profit from non-overlapping job selection.

        Args:
            startTime: Start times of each job.
            endTime: End times of each job.
            profit: Profit of each job.

        Returns:
            Maximum achievable profit.
        """
        n = len(startTime)
        jobs = sorted(zip(endTime, startTime, profit))

        # dp[i] = max profit using first i jobs (1-indexed)
        dp = [0] * (n + 1)
        ends = [job[0] for job in jobs]

        for i in range(1, n + 1):
            end_i, start_i, profit_i = jobs[i - 1]
            # Find rightmost job ending <= start_i
            j = bisect.bisect_right(ends, start_i, 0, i - 1)
            dp[i] = max(dp[i - 1], profit_i + dp[j])

        return dp[n]


# ---------- tests ----------
def test_job_scheduling():
    sol = Solution()

    # Example 1: take jobs (1,3,50) and (3,5,40) -> 90, or (1,3,50)+(4,6,70)=120?
    # Jobs: (1,3,50),(2,4,10),(3,5,40),(3,6,70)
    # Best: (1,3,50)+(3,6,70)=120
    assert sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120

    # Example 2
    assert (
        sol.jobScheduling(
            [1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]
        )
        == 150
    )

    # Example 3
    assert sol.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6

    # Single job
    assert sol.jobScheduling([1], [2], [50]) == 50

    # Non-overlapping jobs, take all
    assert sol.jobScheduling([1, 3, 5], [2, 4, 6], [10, 20, 30]) == 60

    # All overlapping, pick the best
    assert sol.jobScheduling([1, 1, 1], [5, 5, 5], [10, 20, 15]) == 20

    print("All tests passed for 1235. Maximum Profit in Job Scheduling")


if __name__ == "__main__":
    test_job_scheduling()
