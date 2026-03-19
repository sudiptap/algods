"""
1066. Campus Bikes II (Medium)

Pattern: 11_bitmask_dp
- Assign n workers to n bikes (from m bikes) minimizing total Manhattan distance.

Approach:
- dp[mask] = minimum total distance to assign workers 0..popcount(mask)-1 to the
  bikes indicated by the set bits in mask.
- For each state, the next worker to assign is popcount(mask).
- Transition: for each bike j not in mask, dp[mask | (1<<j)] = min(dp[mask] + dist(worker, bike_j)).
- Answer: min(dp[mask]) where popcount(mask) == n (number of workers).

Complexity:
- Time:  O(2^m * m) where m = number of bikes
- Space: O(2^m)
"""

from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])

        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0

        for mask in range(1 << m):
            worker_idx = bin(mask).count('1')
            if worker_idx >= n:
                continue
            if dp[mask] == INF:
                continue
            for b in range(m):
                if mask & (1 << b):
                    continue
                new_mask = mask | (1 << b)
                dp[new_mask] = min(dp[new_mask], dp[mask] + dist(worker_idx, b))

        ans = INF
        for mask in range(1 << m):
            if bin(mask).count('1') == n:
                ans = min(ans, dp[mask])
        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]]) == 6

    # Example 2
    assert sol.assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]) == 4

    # Example 3
    assert sol.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
                           [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]) == 4995

    # Single worker, single bike
    assert sol.assignBikes([[0, 0]], [[1, 1]]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
