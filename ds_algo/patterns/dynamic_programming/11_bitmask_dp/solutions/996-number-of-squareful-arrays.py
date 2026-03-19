"""
996. Number of Squareful Arrays (Hard)

Pattern: 11_bitmask_dp
- Bitmask DP to count permutations where every adjacent pair sums to a perfect square.

Approach:
- Precompute a compatibility matrix: compatible[i][j] = True if A[i]+A[j] is a perfect square.
- dp[mask][last] = number of permutations of the subset indicated by mask, ending with index last.
- Base case: dp[1<<i][i] = 1 for each i.
- Transition: dp[mask | (1<<j)][j] += dp[mask][last] for each j not in mask where compatible[last][j].
- To handle duplicates, divide by factorial of counts of each duplicate value,
  or skip duplicates by only allowing the first unused occurrence of a duplicate value.

Complexity:
- Time:  O(n^2 * 2^n) where n = len(A), n <= 12
- Space: O(n * 2^n)
"""

from typing import List
from math import isqrt


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        # Precompute which pairs are squareful
        def is_square(x):
            s = isqrt(x)
            return s * s == x

        compat = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and is_square(nums[i] + nums[j]):
                    compat[i][j] = True

        full = (1 << n) - 1
        # dp[mask][last]
        dp = [[0] * n for _ in range(1 << n)]

        # Base: pick one element. To avoid counting duplicate starting points,
        # only pick the first occurrence of each value.
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            dp[1 << i][i] = 1

        for mask in range(1, 1 << n):
            for last in range(n):
                if dp[mask][last] == 0:
                    continue
                prev_val = -1
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    if nums[j] == prev_val:
                        continue
                    if not compat[last][j]:
                        continue
                    dp[mask | (1 << j)][j] += dp[mask][last]
                    prev_val = nums[j]

        return sum(dp[full][i] for i in range(n))


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [1,17,8] -> [1,8,17] and [17,8,1] => 2
    assert sol.numSquarefulPerms([1, 17, 8]) == 2

    # Example 2: [2,2,2] -> only [2,2,2] => 1
    assert sol.numSquarefulPerms([2, 2, 2]) == 1

    # Single element
    assert sol.numSquarefulPerms([1]) == 1

    # No squareful pair possible
    assert sol.numSquarefulPerms([1, 2, 3]) == 0

    # Two elements that are squareful: 0+0=0 perfect square
    assert sol.numSquarefulPerms([0, 0]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
