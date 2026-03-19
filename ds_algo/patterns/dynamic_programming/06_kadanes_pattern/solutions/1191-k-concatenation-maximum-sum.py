"""
1191. K-Concatenation Maximum Sum (Medium)

Pattern: 06_kadanes_pattern
- Maximum subarray sum in the array repeated k times.

Approach:
- If k == 1: standard Kadane's on the array.
- If k >= 2: run Kadane's on two concatenated copies of the array to capture
  wrap-around subarrays.
- If k >= 3 and total sum > 0: the answer can span (k-2) full copies in the middle
  plus the best wrap-around from two copies. So add (k - 2) * totalSum.
- Result is taken modulo 10^9 + 7. If max sum is negative, return 0.

Complexity:
- Time:  O(n)
- Space: O(1)
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def kadane(seq):
            max_sum = 0
            cur = 0
            for x in seq:
                cur = max(0, cur + x)
                max_sum = max(max_sum, cur)
            return max_sum

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        # Kadane on two copies
        two_copy_max = kadane(arr + arr)

        if total > 0:
            return (two_copy_max + (k - 2) * total) % MOD
        else:
            return two_copy_max % MOD


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.kConcatenationMaxSum([1, 2], 3) == 9

    # Example 2
    assert sol.kConcatenationMaxSum([1, -2, 1], 5) == 2

    # Example 3
    assert sol.kConcatenationMaxSum([-1, -2], 7) == 0

    # Single element positive
    assert sol.kConcatenationMaxSum([5], 3) == 15

    # Wrap-around needed: kadane([2,-1,2,2,-1,2])=6, total=3>0, 6+(3-2)*3=9
    assert sol.kConcatenationMaxSum([2, -1, 2], 3) == 9

    # k=1
    assert sol.kConcatenationMaxSum([1, -1, 1], 1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
