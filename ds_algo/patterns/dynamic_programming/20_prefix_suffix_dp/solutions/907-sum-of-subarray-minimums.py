"""
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/

Pattern: 20 - Prefix/Suffix DP

---
APPROACH: Monotonic Stack (contribution technique)
- For each element arr[i], find how many subarrays have arr[i] as their minimum.
- Use monotonic stack to compute:
    left[i]  = distance to previous lesser element (strictly less)
    right[i] = distance to next lesser-or-equal element
- Contribution of arr[i] = arr[i] * left[i] * right[i].
- Use <= on one side and < on the other to avoid double-counting duplicates.

Time: O(n)  Space: O(n)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """Return the sum of min(subarray) for every subarray of arr, mod 10^9+7."""
        n = len(arr)
        # left[i]: number of subarrays ending at i where arr[i] is the min
        # right[i]: number of subarrays starting at i where arr[i] is the min
        left = [0] * n
        right = [0] * n

        # Previous Less Element (strictly less)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Next Less-or-Equal Element (to handle duplicates)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.sumSubarrayMins([3, 1, 2, 4]) == 17
    assert sol.sumSubarrayMins([11, 81, 94, 43, 3]) == 444
    assert sol.sumSubarrayMins([1]) == 1
    assert sol.sumSubarrayMins([1, 1, 1]) == 6
    assert sol.sumSubarrayMins([5, 4, 3, 2, 1]) == 35

    print("all tests passed")
