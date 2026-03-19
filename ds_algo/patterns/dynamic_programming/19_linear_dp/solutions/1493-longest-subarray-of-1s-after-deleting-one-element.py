"""
1493. Longest Subarray of 1's After Deleting One Element (Medium)
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Problem:
    Given a binary array nums, delete one element and return the size of
    the longest non-empty subarray containing only 1's.

Pattern: 19 - Linear DP

Approach:
    1. Sliding window allowing at most one 0 in the window.
    2. Expand right pointer. When zeros > 1, shrink left pointer.
    3. Answer = max window size - 1 (must delete one element).

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            # Window size - 1 (must delete one element)
            ans = max(ans, right - left)

        return ans


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.longestSubarray([1, 1, 0, 1]) == 3, \
        f"Test 1 failed: {sol.longestSubarray([1, 1, 0, 1])}"

    # Test 2
    assert sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5, \
        f"Test 2 failed: {sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])}"

    # Test 3: all ones -> must delete one
    assert sol.longestSubarray([1, 1, 1]) == 2, \
        f"Test 3 failed: {sol.longestSubarray([1, 1, 1])}"

    # Test 4: all zeros
    assert sol.longestSubarray([0, 0, 0]) == 0, "Test 4 failed"

    # Test 5: single element
    assert sol.longestSubarray([1]) == 0, "Test 5 failed"

    # Test 6
    assert sol.longestSubarray([1, 0, 1]) == 2, "Test 6 failed"

    print("All tests passed for 1493. Longest Subarray of 1's After Deleting One Element!")


if __name__ == "__main__":
    run_tests()
