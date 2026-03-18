"""
1787. Make the XOR of All Segments Equal to Zero
https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

Pattern: 14 - State Machine DP

---
APPROACH: DP on XOR state across groups
- For XOR of every k-length segment to be zero, the array must be periodic
  with period k, i.e., nums[i] = nums[i + k] for all valid i.
- So elements at indices i%k form a "group". There are k groups (0..k-1).
- We need to choose a value for each group position such that the XOR of
  the k chosen values = 0, minimizing total changes.
- Let freq[g][v] = count of value v in group g, size[g] = total elements in group g.
- dp[xor_state] = min changes to assign values to groups 0..g-1 so their
  XOR equals xor_state.
- Transition for group g, choosing value v:
  cost = size[g] - freq[g][v] (change all elements in group g to v)
  dp_new[xor_state ^ v] = min(dp_new[xor_state ^ v], dp[xor_state] + cost)
- Optimization: most values v have freq[g][v] = 0, so their cost = size[g].
  For those, dp_new[any] can be updated from min(dp[*]) + size[g].
  Only iterate explicitly over values that actually appear in group g.

Time: O(n + k * 1024 * max_distinct_per_group)  Space: O(1024)
  where 1024 = 2^10 since 0 <= nums[i] < 1024
---
"""

from typing import List
from collections import Counter


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        """
        Group elements by index % k. DP on cumulative XOR state (0..1023).
        For each group, update DP by trying all values that appear in
        the group (with their specific cost) plus a blanket update for
        values that don't appear (cost = group size).
        """
        MAX_VAL = 1024  # nums[i] in [0, 1023]
        n = len(nums)

        # Build frequency maps per group
        groups = []
        for g in range(k):
            cnt = Counter()
            for i in range(g, n, k):
                cnt[nums[i]] += 1
            groups.append(cnt)

        INF = float('inf')
        # dp[x] = min changes so that XOR of chosen values for groups processed so far = x
        dp = [INF] * MAX_VAL
        dp[0] = 0

        for g in range(k):
            group_size = sum(groups[g].values())
            global_min = min(dp)  # best dp value across all xor states

            new_dp = [INF] * MAX_VAL

            for xor_state in range(MAX_VAL):
                if dp[xor_state] == INF:
                    continue
                # Try each value that actually appears in this group
                for v, freq in groups[g].items():
                    cost = group_size - freq
                    new_xor = xor_state ^ v
                    new_dp[new_xor] = min(new_dp[new_xor], dp[xor_state] + cost)

            # For values NOT in the group, cost = group_size.
            # Best we can do: global_min + group_size -> updates every new_xor state.
            blanket = global_min + group_size
            for x in range(MAX_VAL):
                new_dp[x] = min(new_dp[x], blanket)

            dp = new_dp

        return dp[0]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: nums = [1,2,0,3,0], k = 1
    # Period 1 -> all elements must be equal, XOR of single element = 0 -> all 0
    # Change 1,2,3 -> 3 changes
    assert sol.minChanges([1, 2, 0, 3, 0], 1) == 3

    # Example 2: nums = [3,4,5,2,1,7,3,4,7], k = 3
    assert sol.minChanges([3, 4, 5, 2, 1, 7, 3, 4, 7], 3) == 3

    # Example 3: nums = [1,2,4,1,2,5,1,2,6], k = 3
    assert sol.minChanges([1, 2, 4, 1, 2, 5, 1, 2, 6], 3) == 3

    # All zeros already
    assert sol.minChanges([0, 0, 0], 1) == 0
    assert sol.minChanges([0, 0, 0, 0], 2) == 0

    # k equals length
    assert sol.minChanges([1, 2, 3], 3) == 0  # 1^2^3 = 0 already

    print("Solution: all tests passed")
