"""
898. Bitwise ORs of Subarrays (Medium)
https://leetcode.com/problems/bitwise-ors-of-subarrays/

Given an integer array arr, return the number of distinct bitwise ORs of all
non-empty subarrays.

Pattern: Linear DP
Approach:
- For each position j, maintain the set of all possible OR values for subarrays
  ending at j.
- When moving to j+1: new_set = {x | arr[j+1] for x in prev_set} union {arr[j+1]}.
- OR is monotonic (only adds bits), so the set of distinct values ending at
  any position has at most 32 elements (one per bit position where a new bit appears).
- Collect all values across all positions into a global set.

Time:  O(n * 32) = O(n) — at most 32 distinct values per position.
Space: O(n * 32) = O(n) — for the global result set.
"""

from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """Return count of distinct bitwise OR values of all subarrays.

        Args:
            arr: Integer array, 1 <= len(arr) <= 5*10^4, 0 <= arr[i] <= 10^9.

        Returns:
            Number of distinct OR values.
        """
        result = set()
        cur = set()  # OR values of subarrays ending at current position

        for x in arr:
            cur = {v | x for v in cur} | {x}
            result |= cur

        return len(result)


# ---------- tests ----------
def test_subarray_bitwise_ors():
    sol = Solution()

    # Example 1: [0] -> {0} -> 1
    assert sol.subarrayBitwiseORs([0]) == 1

    # Example 2: [1,1,2] -> subarrays: [1],[1],[2],[1,1]=1,[1,2]=3,[1,1,2]=3
    # distinct: {1, 2, 3} -> 3
    assert sol.subarrayBitwiseORs([1, 1, 2]) == 3

    # Example 3: [1,2,4] -> {1, 2, 4, 3, 6, 7} -> 6
    assert sol.subarrayBitwiseORs([1, 2, 4]) == 6

    # All zeros
    assert sol.subarrayBitwiseORs([0, 0, 0]) == 1

    # Single element
    assert sol.subarrayBitwiseORs([5]) == 1

    # [1, 3] -> {1, 3} -> 2
    assert sol.subarrayBitwiseORs([1, 3]) == 2

    print("All tests passed for 898. Bitwise ORs of Subarrays")


if __name__ == "__main__":
    test_subarray_bitwise_ors()
