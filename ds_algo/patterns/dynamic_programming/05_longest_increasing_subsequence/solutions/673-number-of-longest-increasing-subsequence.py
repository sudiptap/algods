"""
673. Number of Longest Increasing Subsequence (Medium)

Given an integer array nums, return the number of longest increasing
subsequences. The answer is guaranteed to fit in a 32-bit integer.

Pattern: Longest Increasing Subsequence
- length[i] = length of the longest increasing subsequence ending at i.
- count[i] = number of LIS ending at i with that length.
- For each j < i where nums[j] < nums[i]:
    - If length[j] + 1 > length[i]: found a longer subsequence, reset count.
    - If length[j] + 1 == length[i]: found another way, add to count.
- Answer = sum of count[i] for all i where length[i] == max_length.

Time: O(n^2)
Space: O(n)
"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """Return the number of longest increasing subsequences in nums."""
        if not nums:
            return 0

        n = len(nums)
        length = [1] * n  # length of LIS ending at i
        count = [1] * n   # count of LIS ending at i

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        return sum(c for l, c in zip(length, count) if l == max_len)


def run_tests():
    sol = Solution()

    # Example 1: [1,3,5,4,7] -> LIS length 4, two subsequences: [1,3,5,7] and [1,3,4,7]
    assert sol.findNumberOfLIS([1, 3, 5, 4, 7]) == 2, \
        f"Expected 2, got {sol.findNumberOfLIS([1, 3, 5, 4, 7])}"

    # Example 2: [2,2,2,2,2] -> each element is an LIS of length 1, count = 5
    assert sol.findNumberOfLIS([2, 2, 2, 2, 2]) == 5, \
        f"Expected 5, got {sol.findNumberOfLIS([2, 2, 2, 2, 2])}"

    # Single element
    assert sol.findNumberOfLIS([1]) == 1, \
        f"Expected 1, got {sol.findNumberOfLIS([1])}"

    # Strictly increasing
    assert sol.findNumberOfLIS([1, 2, 3, 4]) == 1, \
        f"Expected 1, got {sol.findNumberOfLIS([1, 2, 3, 4])}"

    # Decreasing
    assert sol.findNumberOfLIS([4, 3, 2, 1]) == 4, \
        f"Expected 4, got {sol.findNumberOfLIS([4, 3, 2, 1])}"

    # [1, 2, 4, 3, 5, 4, 7, 2]
    assert sol.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3, \
        f"Expected 3, got {sol.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2])}"

    print("All tests passed for 673. Number of Longest Increasing Subsequence!")


if __name__ == "__main__":
    run_tests()
