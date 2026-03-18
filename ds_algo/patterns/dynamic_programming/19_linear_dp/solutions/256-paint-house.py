"""
256. Paint House (Medium)

Pattern: 19_linear_dp
    Linear DP where each state depends on the previous row's states.

Approach:
    dp[i][c] = min cost to paint house i with color c.
    dp[i][c] = costs[i][c] + min(dp[i-1][other two colors]).
    Optimize to O(1) space by keeping only the previous row's 3 values.

Complexity:
    Time:  O(n) - one pass through houses, 3 colors is constant.
    Space: O(1) - only 3 variables for previous row.
"""

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        prev_r, prev_g, prev_b = costs[0]

        for i in range(1, len(costs)):
            cur_r = costs[i][0] + min(prev_g, prev_b)
            cur_g = costs[i][1] + min(prev_r, prev_b)
            cur_b = costs[i][2] + min(prev_r, prev_g)
            prev_r, prev_g, prev_b = cur_r, cur_g, cur_b

        return min(prev_r, prev_g, prev_b)


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [[17,2,17],[16,16,5],[14,3,19]]
    assert sol.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
    # Paint house 0 green(2), house 1 blue(5), house 2 green(3) => 10

    # Example 2: single house
    assert sol.minCost([[7, 6, 2]]) == 2

    # Empty
    assert sol.minCost([]) == 0

    # Two houses
    assert sol.minCost([[1, 2, 3], [3, 2, 1]]) == 2  # pick 1+1

    # All same cost
    assert sol.minCost([[5, 5, 5], [5, 5, 5]]) == 10

    print("All tests passed!")


if __name__ == "__main__":
    test()
