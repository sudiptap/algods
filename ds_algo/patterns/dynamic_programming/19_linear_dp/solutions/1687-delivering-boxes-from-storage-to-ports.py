"""
1687. Delivering Boxes from Storage to Ports
https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

Pattern: 19 - Linear DP

---
APPROACH: Sliding window DP with trip counting
- dp[i] = minimum trips to deliver first i boxes.
- Each trip can carry at most maxBoxes boxes with total weight <= maxWeight.
- A trip delivering boxes[j..i-1] costs (number of port changes in segment) + 2.
- port changes in [j..i-1] = prefix_diff[i] - prefix_diff[j+1] (where diff[k]=1 if ports differ).
- Rewrite: dp[i] = prefix_diff[i] + 2 + min over valid j of (dp[j] - prefix_diff[j+1]).
- Maintain a sliding window minimum of (dp[j] - prefix_diff[j+1]) using a deque.

Time: O(n)
Space: O(n)
---
"""

from typing import List
from collections import deque


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int,
                      maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        # diff[i] = 1 if boxes[i] and boxes[i-1] go to different ports
        diff = [0] * n
        for i in range(1, n):
            diff[i] = 1 if boxes[i][0] != boxes[i - 1][0] else 0

        # prefix sum of diffs and weights
        prefix_diff = [0] * (n + 1)
        prefix_w = [0] * (n + 1)
        for i in range(n):
            prefix_diff[i + 1] = prefix_diff[i] + diff[i]
            prefix_w[i + 1] = prefix_w[i] + boxes[i][1]

        # dp[i] = min trips for first i boxes
        # dp[i] = prefix_diff[i] + 2 + min_{valid j}(dp[j] - prefix_diff[j+1])
        dp = [0] * (n + 1)
        dq = deque()  # stores indices j; we want min of dp[j] - prefix_diff[j+1]
        # j=0 is always a starting candidate
        dq.append(0)

        j_left = 0  # leftmost valid j

        for i in range(1, n + 1):
            # Shrink window from left if constraints violated
            while i - j_left > maxBoxes or prefix_w[i] - prefix_w[j_left] > maxWeight:
                if dq and dq[0] == j_left:
                    dq.popleft()
                j_left += 1

            # dp[i] using sliding window min
            dp[i] = (dp[dq[0]] - prefix_diff[dq[0] + 1]) + prefix_diff[i] + 2

            # Add i to deque (as a candidate for future j)
            val_i = dp[i] - prefix_diff[i + 1] if i + 1 <= n else float('inf')
            if i < n:  # i can be a valid j for future i' > i
                while dq and (dp[dq[-1]] - prefix_diff[dq[-1] + 1]) >= val_i:
                    dq.pop()
                dq.append(i)

        return dp[n]


# --- Tests ---
def test():
    sol = Solution()

    assert sol.boxDelivering([[1, 1], [2, 1], [1, 1]], 2, 3, 3) == 4
    assert sol.boxDelivering([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], 3, 3, 6) == 6
    assert sol.boxDelivering([[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 7) == 6
    assert sol.boxDelivering([[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]], 5, 5, 7) == 14

    print("All tests passed!")


if __name__ == "__main__":
    test()
