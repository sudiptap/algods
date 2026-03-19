"""
1187. Make Array Strictly Increasing (Hard)

Pattern: 05_longest_increasing_subsequence
- Minimum replacements to make arr1 strictly increasing, using elements from arr2.

Approach:
- Sort arr2 and remove duplicates.
- dp[i] = dict mapping (last_value -> min_swaps) after processing first i elements.
- For each element arr1[i], we have two choices:
  1. Keep arr1[i]: valid if arr1[i] > prev_value. Cost stays the same.
  2. Replace arr1[i] with smallest value from arr2 that is > prev_value (binary search).
     Cost increases by 1.
- Track all possible (last_value, min_swaps) states, pruning dominated states.
- Answer: minimum swaps among all states after processing all elements. Return -1 if impossible.

Complexity:
- Time:  O(n * m * log m) where n = len(arr1), m = len(arr2) — in practice states are pruned
- Space: O(n + m)
"""

from typing import List
from bisect import bisect_right


class Solution:
    def makeArrayStrictlyIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        # dp: dict of {last_value: min_operations}
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for prev, ops in dp.items():
                # Option 1: keep num if num > prev
                if num > prev:
                    if num not in new_dp or new_dp[num] > ops:
                        new_dp[num] = ops

                # Option 2: replace num with smallest arr2 value > prev
                idx = bisect_right(arr2, prev)
                if idx < len(arr2):
                    val = arr2[idx]
                    if val not in new_dp or new_dp[val] > ops + 1:
                        new_dp[val] = ops + 1

            dp = new_dp
            if not dp:
                return -1

        return min(dp.values())


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.makeArrayStrictlyIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4]) == 1

    # Example 2
    assert sol.makeArrayStrictlyIncreasing([1, 5, 3, 6, 7], [4, 3, 1]) == 2

    # Example 3: impossible
    assert sol.makeArrayStrictlyIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3]) == -1

    # Already sorted
    assert sol.makeArrayStrictlyIncreasing([1, 2, 3], [4, 5]) == 0

    # Single element
    assert sol.makeArrayStrictlyIncreasing([1], [2]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
