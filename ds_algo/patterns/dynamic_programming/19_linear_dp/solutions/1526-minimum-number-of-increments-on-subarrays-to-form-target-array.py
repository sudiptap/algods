"""
1526. Minimum Number of Increments on Subarrays to Form a Target Array (Hard)
https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-target-array/

Problem:
    Starting from an array of zeros, increment any subarray by 1 in each
    operation. Return the minimum number of operations to form the target array.

Pattern: 19 - Linear DP

Approach:
    1. Each operation increments a contiguous subarray by 1.
    2. The answer equals the sum of positive differences between consecutive
       elements (including the first element vs 0).
    3. When target[i] > target[i-1], we need (target[i] - target[i-1]) new
       operations starting at position i. When target[i] <= target[i-1],
       existing operations from before can extend or stop.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                result += target[i] - target[i - 1]
        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.minNumberOperations([1, 2, 3, 2, 1]) == 3, \
        f"Test 1 failed: {sol.minNumberOperations([1, 2, 3, 2, 1])}"

    # Test 2
    assert sol.minNumberOperations([3, 1, 1, 2]) == 4, \
        f"Test 2 failed: {sol.minNumberOperations([3, 1, 1, 2])}"

    # Test 3
    assert sol.minNumberOperations([3, 1, 5, 4, 2]) == 7, \
        f"Test 3 failed: {sol.minNumberOperations([3, 1, 5, 4, 2])}"

    # Test 4: single element
    assert sol.minNumberOperations([5]) == 5, "Test 4 failed"

    # Test 5: all same
    assert sol.minNumberOperations([3, 3, 3]) == 3, "Test 5 failed"

    # Test 6: increasing
    assert sol.minNumberOperations([1, 2, 3]) == 3, "Test 6 failed"

    print("All tests passed for 1526. Minimum Number of Increments on Subarrays to Form Target Array!")


if __name__ == "__main__":
    run_tests()
