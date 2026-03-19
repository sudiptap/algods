"""
978. Longest Turbulent Subarray (Medium)
https://leetcode.com/problems/longest-turbulent-subarray/

A subarray is turbulent if the comparison sign alternates between each pair
of adjacent elements: a[i] < a[i+1] > a[i+2] < ... or a[i] > a[i+1] < a[i+2] > ...

Pattern: Kadane's Pattern
Approach:
- Track two streaks at each position:
  inc = length of turbulent subarray ending at i where arr[i-1] < arr[i].
  dec = length of turbulent subarray ending at i where arr[i-1] > arr[i].
- If arr[i] > arr[i-1]: inc = dec + 1 (alternates from decreasing).
  If arr[i] < arr[i-1]: dec = inc + 1 (alternates from increasing).
  If arr[i] == arr[i-1]: both reset to 1.
- Answer: max of all inc and dec values.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """Return length of longest turbulent subarray.

        Args:
            arr: Integer array, 1 <= len(arr) <= 4*10^4.

        Returns:
            Length of longest turbulent subarray.
        """
        n = len(arr)
        if n == 1:
            return 1

        inc = 1  # length ending with increase
        dec = 1  # length ending with decrease
        ans = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = 1
                dec = 1
            ans = max(ans, inc, dec)

        return ans


# ---------- tests ----------
def test_max_turbulence_size():
    sol = Solution()

    # Example 1: [9,4,2,10,7,8,8,1,9] -> 5 ([4,2,10,7,8])
    assert sol.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5

    # Example 2: [4,8,12,16] -> 2 (strictly increasing, any adjacent pair)
    assert sol.maxTurbulenceSize([4, 8, 12, 16]) == 2

    # Example 3: [100] -> 1
    assert sol.maxTurbulenceSize([100]) == 1

    # All equal
    assert sol.maxTurbulenceSize([5, 5, 5]) == 1

    # Two elements, different
    assert sol.maxTurbulenceSize([1, 2]) == 2

    # Perfect zigzag
    assert sol.maxTurbulenceSize([1, 3, 2, 4, 3, 5]) == 6

    # Strictly decreasing
    assert sol.maxTurbulenceSize([5, 4, 3, 2, 1]) == 2

    print("All tests passed for 978. Longest Turbulent Subarray")


if __name__ == "__main__":
    test_max_turbulence_size()
