"""
2163. Minimum Difference in Sums After Removal of Elements (Hard)
https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

Given array of 3n elements, remove n elements. First n of remaining
form first part, last n form second part. Minimize sum(first) - sum(second).

Pattern: Linear DP (Heap-based Prefix/Suffix)
Approach:
- For the first part (left n elements), we want minimum sum.
  Use a max-heap of size n scanning left to right.
  left_min[i] = minimum sum of n elements from nums[0..i].
- For the second part (right n elements), we want maximum sum.
  Use a min-heap of size n scanning right to left.
  right_max[i] = maximum sum of n elements from nums[i..3n-1].
- Answer = min over split points i of left_min[i] - right_max[i+1].
- Split at i means first part chosen from nums[0..i], second from nums[i+1..3n-1].
  Valid splits: i from n-1 to 2n-1.

Time:  O(n log n)
Space: O(n)
"""

from typing import List
import heapq


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """Return minimum sum(first_n) - sum(second_n) after removing n elements.

        Args:
            nums: Array of 3n integers.

        Returns:
            Minimum difference.
        """
        total = len(nums)
        n = total // 3

        # left_min[i] = min sum of n elements from nums[0..i]
        left_min = [0] * total
        max_heap = []  # negate for max-heap
        current_sum = 0
        for i in range(total):
            current_sum += nums[i]
            heapq.heappush(max_heap, -nums[i])
            if len(max_heap) > n:
                current_sum += heapq.heappop(max_heap)  # remove largest (negated)
            if len(max_heap) == n:
                left_min[i] = current_sum

        # right_max[i] = max sum of n elements from nums[i..3n-1]
        right_max = [0] * total
        min_heap = []
        current_sum = 0
        for i in range(total - 1, -1, -1):
            current_sum += nums[i]
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > n:
                current_sum -= heapq.heappop(min_heap)  # remove smallest
            if len(min_heap) == n:
                right_max[i] = current_sum

        # Find min of left_min[i] - right_max[i+1] for i in [n-1, 2n-1]
        ans = float('inf')
        for i in range(n - 1, 2 * n):
            ans = min(ans, left_min[i] - right_max[i + 1])

        return ans


# ---------- tests ----------
def test_min_difference():
    sol = Solution()

    # Example 1: [3,1,2] -> n=1, remove 1 element
    assert sol.minimumDifference([3, 1, 2]) == -1

    # Example 2: [7,9,5,8,1,3] -> n=2
    assert sol.minimumDifference([7, 9, 5, 8, 1, 3]) == 1

    # All same
    assert sol.minimumDifference([1, 1, 1]) == 0

    print("All tests passed for 2163. Minimum Difference in Sums After Removal of Elements")


if __name__ == "__main__":
    test_min_difference()
