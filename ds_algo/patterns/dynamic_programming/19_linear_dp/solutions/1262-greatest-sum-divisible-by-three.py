"""
1262. Greatest Sum Divisible by Three (Medium)

Pattern: 19_linear_dp
- Find the maximum sum of elements from the array such that the sum is divisible by 3.

Approach:
- Track the best sum achievable for each remainder mod 3: dp[0], dp[1], dp[2].
- Initialize dp = [0, -inf, -inf] (remainder 0 starts at 0, others impossible).
- For each number, update: new_dp[r] = max(dp[r], dp[(r - num%3) % 3] + num).
- Answer: dp[0].

Complexity:
- Time:  O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            temp = dp[:]
            for r in range(3):
                new_r = (r + num) % 3
                temp[new_r] = max(temp[new_r], dp[r] + num)
            dp = temp

        return dp[0]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [3,6,5,1,8] -> 18 (3+6+1+8)
    assert sol.maxSumDivThree([3, 6, 5, 1, 8]) == 18

    # Example 2: [4] -> 0 (4 not divisible by 3)
    assert sol.maxSumDivThree([4]) == 0

    # Example 3: [1,2,3,4,4] -> 12
    assert sol.maxSumDivThree([1, 2, 3, 4, 4]) == 12

    # All divisible by 3
    assert sol.maxSumDivThree([3, 6, 9]) == 18

    # Single element divisible
    assert sol.maxSumDivThree([6]) == 6

    print("All tests passed!")


if __name__ == "__main__":
    test()
