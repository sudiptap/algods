"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum (Medium)
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

Problem:
    Given array arr of positive integers and target, find two non-overlapping
    sub-arrays each with sum equal to target. Minimize the sum of their lengths.
    Return -1 if impossible.

Pattern: 19 - Linear DP

Approach:
    1. Use sliding window to find all subarrays with sum == target.
    2. best[i] = minimum length of a subarray with sum == target ending at
       or before index i.
    3. For each subarray [l, r] with sum == target, combine with best[l-1]
       (best non-overlapping subarray before it).
    4. Track minimum total length.

Complexity:
    Time:  O(n)
    Space: O(n) for the best array
"""

from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = min length of subarray with sum == target ending at or before i
        best = [INF] * n

        ans = INF
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_sum += arr[right]

            while cur_sum > target:
                cur_sum -= arr[left]
                left += 1

            if cur_sum == target:
                length = right - left + 1
                # Check if there's a valid subarray before this one
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])
                elif left == 0:
                    pass  # no room for another subarray before
                best[right] = min(best[right - 1] if right > 0 else INF, length)
            else:
                best[right] = best[right - 1] if right > 0 else INF

        return ans if ans != INF else -1


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.minSumOfLengths([3, 2, 2, 4, 3], 3) == 2, \
        f"Test 1 failed: {sol.minSumOfLengths([3, 2, 2, 4, 3], 3)}"

    # Test 2
    assert sol.minSumOfLengths([7, 3, 4, 7], 7) == 2, \
        f"Test 2 failed: {sol.minSumOfLengths([7, 3, 4, 7], 7)}"

    # Test 3: impossible
    assert sol.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6) == -1, \
        f"Test 3 failed: {sol.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6)}"

    # Test 4
    assert sol.minSumOfLengths([5, 5, 4, 4, 5], 3) == -1, "Test 4 failed"

    # Test 5
    assert sol.minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3) == 3, \
        f"Test 5 failed: {sol.minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3)}"

    print("All tests passed for 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum!")


if __name__ == "__main__":
    run_tests()
