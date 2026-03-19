"""
1478. Allocate Mailboxes (Hard)
https://leetcode.com/problems/allocate-mailboxes/

Problem:
    Given house positions and k mailboxes, place mailboxes to minimize
    the total distance from each house to its nearest mailbox.

Pattern: 07 - Matrix Chain Multiplication

Approach:
    1. Sort houses. Precompute cost[i][j] = min total distance to serve
       houses[i..j] with one mailbox (optimal: place at median).
    2. dp[i][k] = min total distance for first i houses using k mailboxes.
    3. Transition: dp[i][k] = min over j of dp[j][k-1] + cost[j][i-1].
    4. Base: dp[i][1] = cost[0][i-1].

Complexity:
    Time:  O(n^2 * k) for DP + O(n^2) for precomputing costs
    Space: O(n^2 + n * k)
"""

from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # Precompute cost of putting one mailbox for houses[i..j]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                # Optimal: place at median. Cost = sum of distances to median.
                cost[i][j] = cost[i][j - 1] + houses[j] - houses[(i + j) // 2]

        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for m in range(1, min(i, k) + 1):
                for j in range(m - 1, i):
                    dp[i][m] = min(dp[i][m], dp[j][m - 1] + cost[j][i - 1])

        return dp[n][k]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.minDistance([1, 4, 8, 10, 20], 3) == 5, \
        f"Test 1 failed: {sol.minDistance([1, 4, 8, 10, 20], 3)}"

    # Test 2
    assert sol.minDistance([2, 3, 5, 12, 18], 2) == 9, \
        f"Test 2 failed: {sol.minDistance([2, 3, 5, 12, 18], 2)}"

    # Test 3: one mailbox per house
    assert sol.minDistance([1, 5, 10], 3) == 0, "Test 3 failed"

    # Test 4: one mailbox
    assert sol.minDistance([1, 2, 3], 1) == 2, \
        f"Test 4 failed: {sol.minDistance([1, 2, 3], 1)}"

    # Test 5
    assert sol.minDistance([3, 6, 14, 10], 4) == 0, "Test 5 failed"

    print("All tests passed for 1478. Allocate Mailboxes!")


if __name__ == "__main__":
    run_tests()
