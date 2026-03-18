"""
265. Paint House II (Hard)

Pattern: 19_linear_dp
    Generalization of Paint House to k colors. Key insight: track the two
    smallest costs from the previous row to avoid O(k^2) inner loop.

Approach:
    For each row, track min1 (smallest cost), min2 (second smallest), and
    min1_color (which color achieved min1).
    For current house i with color c:
      - If c != min1_color: dp[i][c] = costs[i][c] + min1
      - If c == min1_color: dp[i][c] = costs[i][c] + min2
    O(1) space by only keeping min1, min2, min1_color across rows.

Complexity:
    Time:  O(n * k) - one pass through houses, k colors per house.
    Space: O(1) - only track min1, min2, min1_color.
"""

from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])
        if k == 1:
            return costs[0][0] if n == 1 else -1  # impossible if n > 1

        # Initialize from first row
        min1 = min2 = float('inf')
        min1_color = -1

        for c in range(k):
            cost = costs[0][c]
            if cost < min1:
                min2 = min1
                min1 = cost
                min1_color = c
            elif cost < min2:
                min2 = cost

        for i in range(1, n):
            new_min1 = new_min2 = float('inf')
            new_min1_color = -1

            for c in range(k):
                prev_min = min2 if c == min1_color else min1
                total = costs[i][c] + prev_min

                if total < new_min1:
                    new_min2 = new_min1
                    new_min1 = total
                    new_min1_color = c
                elif total < new_min2:
                    new_min2 = total

            min1, min2, min1_color = new_min1, new_min2, new_min1_color

        return min1


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.minCostII([[1, 5, 3], [2, 9, 4]]) == 5
    # House 0 color 0 (1) + House 1 color 2 (4) = 5

    # Example 2: single house
    assert sol.minCostII([[1, 3]]) == 1

    # 3 houses, 3 colors (same as Paint House I example)
    assert sol.minCostII([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10

    # k=1 single color, single house
    assert sol.minCostII([[7]]) == 7

    # 4 colors
    assert sol.minCostII([[1, 2, 3, 4], [4, 3, 2, 1]]) == 2
    # pick 1 + 1 (different colors)

    print("All tests passed!")


if __name__ == "__main__":
    test()
