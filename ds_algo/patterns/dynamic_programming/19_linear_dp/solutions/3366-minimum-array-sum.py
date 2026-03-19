"""
3366. Minimum Array Sum (Medium)

Pattern: 19_linear_dp
- Given array nums, op1 times you can ceil-divide an element by 2, op2 times you can
  subtract k (if element >= k). Minimize sum. Each element can have at most one of each op.

Approach:
- dp[i][o1][o2] = min sum considering nums[0..i-1] using o1 of op1 and o2 of op2.
- For each element, try 4 options: no op, op1 only, op2 only, op1+op2 (both orders matter:
  ceil(x/2)-k vs ceil((x-k)/2)).

Complexity:
- Time:  O(n * op1 * op2)
- Space: O(op1 * op2)
"""

from typing import List
from math import ceil


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        INF = float('inf')

        # dp[o1][o2] = min sum so far
        dp = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0

        for x in nums:
            new_dp = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
            for o1 in range(op1 + 1):
                for o2 in range(op2 + 1):
                    if dp[o1][o2] == INF:
                        continue
                    base = dp[o1][o2]

                    # No operation
                    new_dp[o1][o2] = min(new_dp[o1][o2], base + x)

                    # Op1 only: ceil(x/2)
                    if o1 < op1:
                        v1 = ceil(x / 2)
                        new_dp[o1 + 1][o2] = min(new_dp[o1 + 1][o2], base + v1)

                    # Op2 only: x - k (if x >= k)
                    if o2 < op2 and x >= k:
                        v2 = x - k
                        new_dp[o1][o2 + 1] = min(new_dp[o1][o2 + 1], base + v2)

                    # Both op1 and op2
                    if o1 < op1 and o2 < op2:
                        # Order 1: op1 first, then op2
                        v1 = ceil(x / 2)
                        if v1 >= k:
                            val1 = v1 - k
                        else:
                            val1 = v1  # can't apply op2

                        # Order 2: op2 first, then op1
                        if x >= k:
                            v2 = ceil((x - k) / 2)
                        else:
                            v2 = ceil(x / 2)  # can't apply op2, just op1

                        best_both = min(val1, v2)
                        # But we need to actually apply both ops only if beneficial
                        # If x >= k: can do op2 then op1
                        # If ceil(x/2) >= k: can do op1 then op2
                        candidates = []
                        # op1 then op2
                        v1_first = ceil(x / 2)
                        if v1_first >= k:
                            candidates.append(v1_first - k)
                        # op2 then op1
                        if x >= k:
                            candidates.append(ceil((x - k) / 2))

                        if candidates:
                            new_dp[o1 + 1][o2 + 1] = min(new_dp[o1 + 1][o2 + 1], base + min(candidates))

            dp = new_dp

        return min(dp[o1][o2] for o1 in range(op1 + 1) for o2 in range(op2 + 1))


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.minArraySum([2, 8, 3, 19, 3], 3, 1, 1) == 23

    # Example 2
    assert sol.minArraySum([2, 4, 3], 3, 2, 1) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
