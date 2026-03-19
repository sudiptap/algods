"""
2552. Count Increasing Quadruplets
https://leetcode.com/problems/count-increasing-quadruplets/

Pattern: 19 - Linear DP

---
APPROACH: For each (j,k) where nums[j] > nums[k], count valid i and l
- Key insight: iterate k, maintain dp[j] = #{i<j: nums[i]<nums[k]} accumulated
  over previous k values. Actually, use the following O(n^2) approach:
- For each k (3rd element), accumulate contribution.
- Maintain dp[j] = total count of i<j with nums[i]<nums[prev_k_values].
- Better: for each j, sweep k and maintain prefix counts.

Cleaner O(n^2):
- Precompute cnt_less[j] = #{i<j: nums[i]<nums[j]} and
  cnt_greater[k] = #{l>k: nums[l]>nums[k]}.
- For middle pair (j,k): iterate k from left to right.
  Maintain dp[v] = sum of cnt_greater[k'] for all k'<current_k where nums[k']==v.
  Wait, that's not quite right either.

Actually the cleanest O(n^2):
- For each j, sweep k > j. If nums[j] > nums[k]:
  ans += (#{i<j: nums[i]<nums[k]}) * (#{l>k: nums[l]>nums[j]})
- Precompute for each (j, value): #{i<j: nums[i]<value} as a 2D prefix.
- And #{l>k: nums[l]>value} as a 2D suffix.

With n<=4000, a BIT-based approach or direct counting works.

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # For each k, we want sum over j<k (where nums[j]>nums[k]) of
        # #{i<j: nums[i]<nums[k]} * #{l>k: nums[l]>nums[j]}

        # Precompute greater_after[k] = #{l>k: nums[l]>nums[k]}
        # But we need #{l>k: nums[l]>nums[j]}, which depends on j.
        # So precompute for each position and value.

        # greater_suffix[k][v] = #{l>k: nums[l]>v} -- O(n^2) space, acceptable for n<=4000
        # less_prefix[j][v] = #{i<j: nums[i]<v}

        # Build less_prefix: for each j, count elements < v in nums[0..j-1]
        # less_prefix[j] = array where less_prefix[j] = #{i<j: nums[i] < nums[k]}
        # We'll compute on the fly.

        # Use dp approach from editorial:
        # Iterate k from 0 to n-1. For each j < k where nums[j] > nums[k]:
        #   We need to multiply #{i<j: nums[i]<nums[k]} by #{l>k: nums[l]>nums[j]}.
        # This is O(n^2) per pair if done naively = O(n^3).

        # Optimization: precompute for all (pos, val):
        # prefix_less[pos][val] = #{i<pos: nums[i]<val}
        # suffix_greater[pos][val] = #{l>pos: nums[l]>val}

        # Space: O(n^2) which is fine for n<=4000

        # Build prefix_less
        prefix_less = [[0] * (n + 2) for _ in range(n + 1)]
        for j in range(n):
            for v in range(n + 1):
                prefix_less[j + 1][v] = prefix_less[j][v]
            for v in range(nums[j] + 1, n + 2):
                prefix_less[j + 1][v] += 1

        # Build suffix_greater
        suffix_greater = [[0] * (n + 2) for _ in range(n + 1)]
        for k in range(n - 1, -1, -1):
            for v in range(n + 1):
                suffix_greater[k][v] = suffix_greater[k + 1][v]
            for v in range(0, nums[k]):
                suffix_greater[k][v] += 1

        for j in range(1, n - 2):
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    i_count = prefix_less[j][nums[k]]
                    l_count = suffix_greater[k + 1][nums[j]]
                    ans += i_count * l_count

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countQuadruplets([1, 3, 2, 4, 5]) == 2
    assert sol.countQuadruplets([1, 2, 3, 4]) == 0
    assert sol.countQuadruplets([4, 3, 2, 1]) == 0

    print("all tests passed")
