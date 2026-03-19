"""
1524. Number of Sub-arrays With Odd Sum (Medium)
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Problem:
    Given an array of integers, return the number of sub-arrays with an
    odd sum, modulo 10^9+7.

Pattern: 19 - Linear DP

Approach:
    1. Track count of even and odd prefix sums seen so far.
    2. If current prefix sum is odd, it pairs with all even prefix sums
       to make odd subarray sums. Vice versa.
    3. Increment even_count or odd_count based on current prefix parity.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even_count = 1  # empty prefix sum = 0 is even
        odd_count = 0
        prefix = 0
        result = 0

        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                # Odd subarray sum = current even prefix - odd prefix
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                # Odd subarray sum = current odd prefix - even prefix
                result = (result + even_count) % MOD
                odd_count += 1

        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.numOfSubarrays([1, 3, 5]) == 4, \
        f"Test 1 failed: {sol.numOfSubarrays([1, 3, 5])}"

    # Test 2
    assert sol.numOfSubarrays([2, 4, 6]) == 0, "Test 2 failed"

    # Test 3
    assert sol.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16, \
        f"Test 3 failed: {sol.numOfSubarrays([1, 2, 3, 4, 5, 6, 7])}"

    # Test 4: single odd
    assert sol.numOfSubarrays([1]) == 1, "Test 4 failed"

    # Test 5: single even
    assert sol.numOfSubarrays([2]) == 0, "Test 5 failed"

    # Test 6
    assert sol.numOfSubarrays([100, 100, 99, 100]) == 6, \
        f"Test 6 failed: {sol.numOfSubarrays([100, 100, 99, 100])}"

    print("All tests passed for 1524. Number of Sub-arrays With Odd Sum!")


if __name__ == "__main__":
    run_tests()
