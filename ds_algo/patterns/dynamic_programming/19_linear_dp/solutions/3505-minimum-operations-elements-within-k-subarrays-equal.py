"""
3505. Minimum Operations to Make Elements Within K Subarrays Equal
https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

Pattern: 19 - Linear DP

---
APPROACH: Sliding median + DP.
- For each window of size x, compute cost to make all equal (sum of abs deviations from median).
- dp[j][i] = min cost to place j non-overlapping windows from first i window positions.
- Use bisect-based sorted list for sliding window median cost.

Time: O(n * x * log x + n * k)  Space: O(n * k)
---
"""

from typing import List
import bisect


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Step 1: compute cost[i] = cost to make nums[i..i+x-1] all equal to median
        num_windows = n - x + 1
        cost_arr = [0] * num_windows

        # Use sorted list with bisect for sliding window
        window = sorted(nums[:x])
        mid = (x - 1) // 2

        def compute_cost(w):
            median = w[(len(w) - 1) // 2]
            return sum(abs(v - median) for v in w)

        cost_arr[0] = compute_cost(window)

        for i in range(1, num_windows):
            # Remove nums[i-1], add nums[i+x-1]
            old = nums[i - 1]
            new = nums[i + x - 1]
            pos = bisect.bisect_left(window, old)
            window.pop(pos)
            bisect.insort(window, new)
            cost_arr[i] = compute_cost(window)

        # Step 2: DP to select k non-overlapping windows
        INF = float('inf')
        # dp[j][i] = min cost to place j windows, last window is at position <= i
        dp = [[INF] * num_windows for _ in range(k + 1)]
        for i in range(num_windows):
            dp[0][i] = 0

        for j in range(1, k + 1):
            for i in range(num_windows):
                # Don't place window at i
                dp[j][i] = dp[j][i - 1] if i > 0 else INF
                # Place window at i as the j-th window
                prev = i - x
                if prev >= 0:
                    if dp[j - 1][prev] < INF:
                        dp[j][i] = min(dp[j][i], dp[j - 1][prev] + cost_arr[i])
                elif j == 1:
                    dp[j][i] = min(dp[j][i], cost_arr[i])

        return dp[k][num_windows - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperations([5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2) == 8
    assert sol.minOperations([1, 1, 1, 1], 2, 2) == 0

    print("Solution: all tests passed")
