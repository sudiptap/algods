"""
3284. Sum of Consecutive Subarrays (Medium)

Pattern: 06_kadanes_pattern
- Find sum of all subarrays where consecutive elements differ by exactly 1
  (either all +1 or all -1 steps).

Approach:
- Track ascending and descending streaks with their cumulative subarray sums.
- asc_total = sum of all ascending subarray sums ending at current position.
  When extending: asc_total = prev_asc_total + nums[i] * inc_len (each existing subarray
  plus new single-element subarray all gain nums[i]).
  When resetting: asc_total = nums[i], inc_len = 1.
- Similarly for descending. Single-element subarrays counted in both, subtract nums[i].

Complexity:
- Time:  O(n)
- Space: O(1)
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        inc_len = 0
        dec_len = 0
        asc_total = 0
        desc_total = 0

        for i in range(n):
            if i > 0 and nums[i] - nums[i - 1] == 1:
                inc_len += 1
                asc_total = (asc_total + nums[i] * inc_len) % MOD
            else:
                inc_len = 1
                asc_total = nums[i] % MOD

            if i > 0 and nums[i] - nums[i - 1] == -1:
                dec_len += 1
                desc_total = (desc_total + nums[i] * dec_len) % MOD
            else:
                dec_len = 1
                desc_total = nums[i] % MOD

            # Single-element counted in both asc and desc, subtract once
            ans = (ans + asc_total + desc_total - nums[i]) % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [1,2,3] -> subarrays: [1],[2],[3],[1,2],[2,3],[1,2,3]
    # sums: 1+2+3+3+5+6 = 20
    assert sol.getSum([1, 2, 3]) == 20

    # Example 2
    assert sol.getSum([1, 3]) == 4  # only single-element subarrays are consecutive

    # Decreasing
    assert sol.getSum([3, 2, 1]) == 20

    print("All tests passed!")


if __name__ == "__main__":
    test()
