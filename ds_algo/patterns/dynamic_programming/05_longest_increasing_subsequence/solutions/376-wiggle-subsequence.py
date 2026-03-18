"""
376. Wiggle Subsequence (Medium)

A wiggle sequence has alternating positive and negative differences between
consecutive elements. Return the length of the longest wiggle subsequence.

Pattern: LIS variant / Greedy.

Approach (Greedy):
    Track two counters:
        up   = length of longest wiggle subsequence ending with a rise
        down = length of longest wiggle subsequence ending with a fall
    Scan through adjacent pairs:
        - If nums[i] > nums[i-1] (rising):  up = down + 1
        - If nums[i] < nums[i-1] (falling): down = up + 1
    Answer is max(up, down).

    This works because extending from the opposite direction always produces
    a valid wiggle, and greedily taking every direction change is optimal.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """Return the length of the longest wiggle subsequence."""
        if len(nums) < 2:
            return len(nums)

        up = 1
        down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
            # equal: do nothing

        return max(up, down)


# ───────────────────────── Tests ─────────────────────────
def test():
    s = Solution()

    # Example 1
    assert s.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6

    # Example 2
    assert s.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7

    # Example 3
    assert s.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2

    # Single element
    assert s.wiggleMaxLength([42]) == 1

    # Two elements, same
    assert s.wiggleMaxLength([5, 5]) == 1

    # Two elements, different
    assert s.wiggleMaxLength([5, 10]) == 2

    # All equal
    assert s.wiggleMaxLength([3, 3, 3, 3]) == 1

    # Alternating perfectly
    assert s.wiggleMaxLength([1, 5, 1, 5, 1]) == 5

    # Empty
    assert s.wiggleMaxLength([]) == 0

    print("All tests passed for 376!")


if __name__ == "__main__":
    test()
