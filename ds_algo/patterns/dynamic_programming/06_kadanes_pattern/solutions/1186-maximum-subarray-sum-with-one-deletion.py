"""
1186. Maximum Subarray Sum with One Deletion (Medium)
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

Given an array of integers, return the maximum sum for a non-empty subarray
(contiguous elements) with at most one element deletion. A subarray must
contain at least one element after the deletion.

Pattern: Kadane's with two-state tracking
- no_del[i]: max subarray sum ending at i with no deletion used.
- one_del[i]: max subarray sum ending at i with exactly one deletion used.
- Transitions:
    no_del[i] = max(nums[i], no_del[i-1] + nums[i])
    one_del[i] = max(no_del[i-1], one_del[i-1] + nums[i])
      (either delete nums[i] by taking no_del[i-1], or keep nums[i] and
       carry the deletion from before)
- Answer: max over all i of max(no_del[i], one_del[i]).

Time:  O(n)
Space: O(1) — only track previous values
"""

from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        """Return maximum subarray sum with at most one element deletion.

        Args:
            arr: Array of integers, length >= 1.

        Returns:
            Maximum subarray sum (subarray must be non-empty after deletion).
        """
        no_del = arr[0]
        one_del = float("-inf")
        result = arr[0]

        for i in range(1, len(arr)):
            # Order matters: compute one_del before updating no_del
            one_del = max(no_del, one_del + arr[i])
            no_del = max(arr[i], no_del + arr[i])
            result = max(result, no_del, one_del)

        return result


# ---------- tests ----------
def test_maximum_sum():
    sol = Solution()

    # Example 1: delete -2 -> [1,4,2,3] sum=10; or keep all max subarray
    assert sol.maximumSum([1, -2, 0, 3]) == 4

    # Example 2: [1,-4,-5,-2,5,6] delete -2 -> subarray [5,6]=11 or
    # delete -4 -> [1,-5,-2,5,6] no help. Best: [5,6]=11? Actually 11.
    # Wait the subarray must be contiguous. [5,6] = 11 without deletion.
    # With deletion of -2: subarray [-2,5,6] -> 5+6=11. Same.
    assert sol.maximumSum([1, -4, -5, -2, 5, 6]) == 11

    # All negative: must pick the largest single element
    assert sol.maximumSum([-1, -2, -3]) == -1

    # Single element
    assert sol.maximumSum([5]) == 5

    # Delete the middle negative to bridge two positives
    assert sol.maximumSum([2, -1, 3]) == 5  # delete -1 -> 2+3=5

    # No deletion needed
    assert sol.maximumSum([1, 2, 3, 4]) == 10

    print("All tests passed for 1186. Maximum Subarray Sum with One Deletion")


if __name__ == "__main__":
    test_maximum_sum()
